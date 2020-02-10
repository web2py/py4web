import base64
import datetime
import hashlib
import urllib
import uuid

from py4web import redirect, request, response, abort, URL, action
from py4web.core import Fixture, Template
from pydal.validators import IS_EMAIL, CRYPT, IS_NOT_EMPTY, IS_NOT_IN_DB


def b16e(text):
    return base64.b16encode(text.encode()).decode()


def b16d(text):
    return base64.b16decode(text.encode()).decode()


class AuthEnforcer(Fixture):

    """
    Base fixtures that checks if a condition is met
    if not redirects to a different pages or returns HTTP 403
    """

    def __init__(self, auth, condition=None):
        self.__prerequisites__ = [auth]
        self.auth = auth
        self.condition = condition

    def transform(self, output):
        return self.auth.transform(output)

    def abort_or_rediect(self, page):
        """
        return HTTP 403 if content_type is applicaitons/json
        else redirects to page"""
        if request.content_type == "application/json":
            abort(403)
        redirect(URL(self.auth.route, page))

    def on_request(self):
        """check that we have a user in the session and
        the condition is met"""
        user = self.auth.session.get("user")
        if not user or not user.get("id"):
            self.abort_or_rediect("login")
        if callable(self.condition) and not self.condition(user):
            self.abort_or_rediect("not-authorized")


class Auth(Fixture):

    messages = {
        "verify_email": {
            "subject": "Confirm email",
            "body": "Welcome {first_name}, click {link} to confirm your email",
        },
        "reset_password": {
            "subject": "Password reset",
            "body": "Hello {first_name}, click {link} to change password",
        },
        "unsubscribe": {
            "subject": "Unsubscribe confirmation",
            "body": "By {first_name}, you have been erased from our system",
        },
    }

    extra_auth_user_fields = []

    def __init__(
        self,
        session,
        db,
        define_tables=True,
        sender=None,
        use_username=True,
        registration_requires_confirmation=True,
        registration_requires_appoval=False,
        inject=True,
    ):
        """Creates and Auth object responsinble for handling
        authentication and authorization"""
        self.__prerequisites__ = []
        self.inject = inject
        if session:
            self.__prerequisites__.append(session)
        if db:
            self.__prerequisites__.append(db)
        self.db = db
        self.session = session
        self.sender = sender
        self.route = None
        self.registration_requires_confirmation = registration_requires_confirmation
        self.registration_requires_appoval = registration_requires_appoval
        self.use_username = use_username  # if False, uses email only
        # The self._link variable is not thread safe (only intended for testing)
        self._link = None
        if db and define_tables:
            self.define_tables()
        self.plugins = {}

    def transform(self, output):
        if self.inject:
            if isinstance(output, dict) and not 'user' in output:
                output['user'] = self.get_user()
        return output

    def define_tables(self):
        """Defines the auth_user table"""
        db = self.db
        Field = db.Field
        if not "auth_user" in db.tables:
            ne = IS_NOT_EMPTY()
            auth_fields = [
                Field(
                    "email",
                    requires=(IS_EMAIL(), IS_NOT_IN_DB(db, "auth_user.email")),
                    unique=True,
                ),
                Field(
                    "password",
                    "password",
                    requires=CRYPT(),
                    readable=False,
                    writable=False,
                ),
                Field("first_name", requires=ne),
                Field("last_name", requires=ne),
                Field("sso_id", readable=False, writable=False),
                Field("action_token", readable=False, writable=False),
            ]
            if self.use_username:
                auth_fields.insert(
                    0,
                    Field(
                        "username",
                        requires=[ne, IS_NOT_IN_DB(db, "auth_user.username")],
                        unique=True,
                    ),
                )
            db.define_table("auth_user", *auth_fields, *self.extra_auth_user_fields)

    @property
    def signature(self):
        """Returns a list of fields for a table signature"""
        Field = self.db.Field
        now = lambda: datetime.datetime.utcnow()
        user = lambda s=self: s.get_user().get("id")
        fields = [
            Field("created_on", "datetime", default=now, writable=False, readable=True),
            Field("created_by", "reference auth_user", default=user, writable=False, readable=True),
            Field(
                "modified_on",
                "datetime",
                update=now,
                default=now,
                writable=False,
                readable=True,
            ),
            Field(
                "modified_by",
                "reference auth_user",
                default=user,
                update=user,
                writable=False,
                readable=True,
            ),
            Field("is_active", "boolean", default=True, readable=False, writable=False),
        ]
        return fields

    # Validation fixtures
    @property
    def user(self):
        """Use as @action.uses(auth.user)"""
        return AuthEnforcer(self)

    def condition(self, condition):
        """Use as @action.uses(auth.condition(lambda user: True))"""
        return AuthEnforcer(self, condition)

    # utilities
    def get_user(self, safe=True):
        """extracts the user form the session.
        returns {} if no user in the session.
        If session contains only a user['id']
        retrives the other readable user info from auth_user"""
        user = self.session.get("user")
        if not user or not isinstance(user, dict) or not "id" in user:
            return {}
        if len(user) == 1 and self.db:
            user = self.db.auth_user(user["id"])
            if not user:
                return {}
            if safe:
                user = {f.name: user[f.name] for f in self.db.auth_user if f.readable}
        return user

    @property
    def user_id(self):
        return self.session.get("user", {}).get('id', None)

    @property
    def current_user(self):
        return self.get_user()

    def register_plugin(self, plugin):
        """registers an Auth plugin"""
        self.plugins[plugin.name] = plugin

    def enable(self, route="auth/", uses=(), env=None):
        """enables Auth, aka generates login/logout/register/etc pages"""
        self.route = route
        """This assumes the bottle framework and exposes all actions as /{app_name}/auth/{path}"""

        def responder(path, env=env):
            return self.action(
                path, request.method, request.query, request.json, env=env
            )

        action(route + "<path:path>", method=["GET", "POST"])(
            action.uses(self, *uses)(responder)
        )

    # Handle http requests

    def action(self, path, method, get_vars, post_vars, env=None):
        """action that handles all the HTTP requests for Auth"""
        env = env or {}
        if path.startswith("plugin/"):
            parts = path.split("/", 2)
            plugin = self.plugins.get(parts[1])
            if plugin:
                return plugin.handle_request(
                    self, parts[2], request.query, request.json
                )
            else:
                abort(404)
        if path.startswith("api/"):
            data = {}
            if method == "GET":
                # Should we use the username?
                if path == "api/use_username":
                    return {"use_username": self.use_username}
                # Otherwise, we assume the user exists.
                user = self.get_user(safe=True)
                if not user:
                    data = self._error("not authorized", 401)
                if path == "api/profile":
                    return {"user": user}
            elif method == "POST" and self.db:
                vars = dict(post_vars)
                user = self.get_user(safe=False)
                if path == "api/register":
                    data = self.register(vars, send=True).as_dict()
                elif path == "api/login":
                    # Prioritize PAM or LDAP logins if enabled
                    if "pam" in self.plugins or "ldap" in self.plugins:
                        plugin_name = "pam" if "pam" in self.plugins else "ldap"
                        username, password = vars.get("email"), vars.get("password")
                        check = self.plugins[plugin_name].check_credentials(
                            username, password
                        )
                        if check:
                            data = {
                                "username": username,
                                "email": username + "@localhost",
                                "sso_id": plugin_name + ":" + username,
                            }
                            # and register the user if we have one, just in case
                            if self.db:
                                data = self.get_or_register_user(data)
                        else:
                            data = self._error("Invalid Credentials")
                    # Else use normal login
                    else:
                        user, error = self.login(**vars)
                        if user:
                            self.session["user"] = {"id": user.id}
                            user = {
                                f.name: user[f.name]
                                for f in self.db.auth_user
                                if f.readable
                            }
                            data = {"user": user}
                        else:
                            data = self._error(error)
                elif path == "api/request_reset_password":
                    if not self.request_reset_password(**vars):
                        data = self._error("invalid user")
                elif path == "api/reset_password":
                    if not self.reset_password(
                        vars.get("token"), vars.get("new_password")
                    ):
                        data = self._error("invalid token, request expired")
                elif user and path == "api/logout":
                    self.session["user"] = None
                elif user and path == "api/unsubscribe":
                    self.session["user"] = None
                    self.gdpr_unsubscribe(user, send=True)
                elif user and path == "api/change_password":
                    data = self.change_password(
                        user, vars.get("new_password"), vars.get("password")
                    )
                elif user and path == "api/change_email":
                    data = self.change_email(
                        user, vars.get("new_email"), vars.get("password")
                    )
                elif user and path == "api/profile":
                    data = self.update_profile(user, **vars)
                else:
                    data = {"status": "error", "message": "undefined"}
            if not "status" in data and data.get("errors"):
                data.update(status="error", message="validation errors", code=401)
            elif "errors" in data and not data["errors"]:
                del data["errors"]
            data["status"] = data.get("status", "success")
            data["code"] = data.get("code", 200)
            return data
        elif path == "logout":
            self.session["user"] = None
            # Somehow call revoke for active plugin
        elif path == "verify_email" and self.db:
            token = get_vars.get("token")
            if self.verify_email(token):
                next = b16d(token.split("/")[1])
                redirect(next or URL("auth", "email_verified"))
            else:
                redirect(URL("auth", "token_expired"))
        env["path"] = path
        return Template("auth.html").transform(env)

    # Methods that do not assume a user

    def register(self, fields, send=True, next=""):
        if self.use_username:
            fields["username"] = fields.get("username", "").lower()
        fields["email"] = fields.get("email", "").lower()
        if self.registration_requires_confirmation:
            token = str(uuid.uuid4()) + "/" + b16e(next)
            fields["action_token"] = "pending-registration:%s" % token
            res = self.db.auth_user.validate_and_insert(**fields)
            if send and res.get("id"):
                self._link = link = URL(
                    self.route, "verify_email", vars=dict(token=token), scheme=True
                    )
                self.send("verify_email", fields, link=link)
        else:
            fields["action_token"] = ''
            res = self.db.auth_user.validate_and_insert(**fields)
        return res

    def login(self, email, password):
        db = self.db
        value = email.lower()
        if self.use_username:
            query = (
                (db.auth_user.email == value)
                if "@" in value
                else (db.auth_user.username == value)
            )
        else:
            query = db.auth_user.email == value
        user = db(query).select().first()
        if not user:
            return (None, "Invalid email")
        if (user.action_token or "").startswith("pending-registration:"):
            return (None, "Registration is pending")
        if (user.action_token or "").startswith("account-blocked:"):
            return (None, "Account is blocked")
        if db.auth_user.password.requires(password)[0] == user.password:
            return (user, None)
        return None, "Invalid Credentials"

    def request_reset_password(self, email, send=True, next=""):
        db = self.db
        value = email.lower()
        if self.use_username:
            query = (
                (db.auth_user.email == value)
                if "@" in value
                else (db.auth_user.username == value)
            )
        else:
            query = db.auth_user.email == value
        user = db(query).select().first()
        if user and not user.action_token == "account-blocked":
            token = str(uuid.uuid4()) + "/" + b16e(next)
            user.update_record(action_token="reset-password-request:" + token)
            if send:
                self._link = link = URL(
                    self.route, "reset_password", vars=dict(token=token), scheme=True,
                )
                self.send("reset_password", user, link=link)
            return token

    def verify_email(self, token):
        n = self.db(self._query_from_token(token)).update(action_token=None)
        return n > 0

    def reset_password(self, token, new_password):
        db = self.db
        query = self._query_from_token(token)
        user = db(query).select().first()
        if user:
            return (
                db(db.auth_user.id == user.id)
                .validate_and_update(password=new_password)
                .as_dict()
            )

    # Methods that assume a user

    def change_password(self, user, new_password, password=None, check=True):
        db = self.db
        if check and not db.auth_user.password.requires(password)[0] == user.password:
            return {"errors": {"password": "invalid"}}
        return (
            db(db.auth_user.id == user.id)
            .validate_and_update(password=new_password)
            .as_dict()
        )

    def change_email(self, user, new_email, password=None, check=True):
        db = self.db
        if check and not db.auth_user.password.requires(password)[0] == user.password:
            return {"errors": {"password": "invalid"}}
        return (
            db(db.auth_user.id == user.id)
            .validate_and_update(email=new_email)
            .as_dict()
        )

    def update_profile(self, user, **fields):
        db = self.db
        errors = {
            k: "invalid"
            for k in fields
            if k not in db.auth_user.fields or not db.auth_user[k].writable
        }
        if errors:
            return {"errors": errors}
        return db(db.auth_user.id == user.id).validate_and_update(**fields).as_dict()

    def gdpr_unsubscribe(self, user, send=True):
        """GDPR unsubscribe means we delete first_name, last_name,
        then replace email with hash of the actual email and notify the user.

        Essentially we erase the user info yet retain the ability to verify
        that a given email has unsubscribed and maybe restore it if requested.

        Despite unsubscription we retain enough info to be able to comply
        with audit requests for illicit activities.

        I am not a lawyer but I believe this complies,
        Check with your lawyer before using this feature, no warranty expressed or implied.
        """
        user = user.as_dict()
        id = user["id"]
        token = hashlib.sha1(user["email"].lower()).hexdigest()
        db = self.db
        db(db.auth_user.id == id).update(
            email="%s@example.com" % token,
            password=None,
            first_name="anonymous",
            last_name="anonymous",
            sso_id=None,
            action_token="gdpr-unsubscribed",
        )
        if send:
            self.send("unsubscribe", user)

    def is_gdpr_unsubscribed(self, email):
        db = self.db
        token = hashlib.sha1(email.lower()).hexdigest()
        email = "%s@example.com" % token
        return db(db.auth_user.email == email).count() > 0

    def get_or_register_user(self, user):
        db = self.db
        row = db(db.auth_user.sso_id == user["sso_id"]).select(limitby=(0, 1)).first()
        data = user
        if row:
            if any(user[key] != row[key] for key in user):
                row.update_record(**user)
            data["id"] = row["id"]
        else:
            data["id"] = db.auth_user.insert(**db.auth_user._filter_fields(user))
        return data

    # Private methods

    def _query_from_token(self, token):
        query = self.db.auth_user.action_token == "reset-password-request:%s" % token
        query |= self.db.auth_user.action_token == "pending-registration:%s" % token
        return query

    def _error(self, message, code=400):
        return {"status": "error", "message": message, "code": code}

    # Other service methods (that can be overwritten)

    def send(self, name, user, **attrs):
        """Extend the object and override this function to send messages with
        twilio or onesignal or alternative method other than email"""
        message = self.messages[name]
        d = dict(user)
        d.update(**attrs)
        email = user["email"]
        subject = message["subject"].format(**d)
        body = message["body"].format(**d)
        if not self.sender:
            print('Mock send to %s subject "%s" body:\n%s\n' % (email, subject, body))
            return True
        return self.sender.send(email, subject=subject, body=body)
