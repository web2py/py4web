import base64
import calendar
import datetime
import hashlib
import re
import time
import urllib
import uuid

from py4web import redirect, request, response, abort, URL, action, Field, HTTP
from py4web.core import Fixture, Template, REGEX_APPJSON
from py4web.utils.form import Form

from pydal.validators import (
    IS_EMAIL,
    CRYPT,
    IS_NOT_EMPTY,
    IS_NOT_IN_DB,
    IS_STRONG,
    IS_MATCH,
)

"""
[X] Enable and disable plugins
[X} Enable and disable actions
[X] Require passwords of various complexity
[x] Force logout after x hours (WIP)
[X] No re-use of the last n passwords
[ ] Force new password on first login (WIP)
[ ] Two-factor authentication for users with 'administrator' access
[ ] Lock account after x failed login attempts.
[ ] Force new password every x days.
"""


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

    def transform(self, output, shared_data):
        return self.auth.transform(output, shared_data)

    def abort_or_redirect(self, page, message=""):
        """
        return HTTP 403 if 'application/json' in HTTP_ACCEPT
        else redirects to page"""
        if re.search(REGEX_APPJSON, request.headers.get("accept", "")):
            abort(403)
        redirect_next = request.fullpath
        if request.query_string:
            redirect_next = redirect_next + "?{}".format(request.query_string)
        redirect(
            URL(
                self.auth.route,
                page,
                vars=dict(next=redirect_next, flash=message),
                use_appname=self.auth.use_appname_in_redirects,
            )
        )

    def on_request(self):
        """check that we have a user in the session and
        the condition is met"""
        user = self.auth.session.get("user")
        if not user or not user.get("id"):
            self.auth.session["recent_activity"] = None
            self.abort_or_redirect("login", "User not logged in")
        activity = self.auth.session.get("recent_activity")
        time_now = calendar.timegm(time.gmtime())
        # enforce the optionl auth session expiration time
        if self.auth.login_expiration_time and activity:
            if time_now - activity > self.auth.login_expiration_time:
                self.abort_or_redirect("login", "Login expired")
        # record the time of the latest activity for logged in user (with throttling)
        if not activity or time_now - activity > 6:
            self.auth.session["recent_activity"] = time_now
        self.auth.session["recent_timestamp"] = datetime.datetime.utcnow().isoformat()
        if callable(self.condition) and not self.condition(user):
            self.abort_or_redirect("not-authorized", "User not authorized")


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
        use_phone_number=False,
        registration_requires_confirmation=True,
        registration_requires_approval=False,
        inject=True,
        extra_fields=[],
        login_expiration_time=3600,  # seconds
        password_complexity={"entropy": 50},
        block_previous_password_num=None,
        allowed_actions=["all"],
        use_appname_in_redirects=True,
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
        self.registration_requires_approval = registration_requires_approval
        self.use_username = use_username  # if False, uses email only
        self.use_phone_number = use_phone_number
        self.login_expiration_time = login_expiration_time
        self.password_complexity = password_complexity
        self.block_previous_password_num = block_previous_password_num
        self.allowed_actions = allowed_actions
        self.use_appname_in_redirects = use_appname_in_redirects
        # The self._link variable is not thread safe (only intended for testing)
        self._link = None
        self.extra_auth_user_fields = extra_fields
        if db and define_tables:
            self.define_tables()
        self.plugins = {}

    def transform(self, output, shared_data):
        if self.inject:
            template_context = shared_data.get("template_context")
            template_context["user"] = self.get_user()
        return output

    def define_tables(self):
        """Defines the auth_user table"""
        db = self.db
        if not "auth_user" in db.tables:
            ne = IS_NOT_EMPTY()
            if self.password_complexity:
                requires = [IS_STRONG(**self.password_complexity), CRYPT()]
            else:
                requires = [CRYPT()]
            auth_fields = [
                Field(
                    "email",
                    requires=(IS_EMAIL(), IS_NOT_IN_DB(db, "auth_user.email")),
                    unique=True,
                ),
                Field(
                    "password",
                    "password",
                    requires=requires,
                    readable=False,
                    writable=False,
                ),
                Field("first_name", requires=ne),
                Field("last_name", requires=ne),
                Field("sso_id", readable=False, writable=False),
                Field("action_token", readable=False, writable=False),
                Field(
                    "last_password_change",
                    "datetime",
                    default=None,
                    readable=False,
                    writable=False,
                ),
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
            if self.use_phone_number:
                auth_fields.insert(
                    2,
                    Field(
                        "phone_number",
                        requires=[
                            ne,
                            IS_MATCH(r"^[+]?(\(\d+\)|\d+)(\(\d+\)|\d+|[ -])+$"),
                        ],
                    ),
                )
            if self.block_previous_password_num is not None:
                auth_fields.append(
                    Field(
                        "past_passwords_hash",
                        "list:string",
                        writable=False,
                        readable=False,
                    )
                )
            db.define_table("auth_user", *auth_fields, *self.extra_auth_user_fields)

    @property
    def signature(self):
        """Returns a list of fields for a table signature"""
        now = lambda: datetime.datetime.utcnow()
        user = lambda s=self: s.get_user().get("id")
        fields = [
            Field("created_on", "datetime", default=now, writable=False, readable=True),
            Field(
                "created_by",
                "reference auth_user",
                default=user,
                writable=False,
                readable=True,
            ),
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
    def is_logged_in(self):
        return self.session.get("user", {}).get("id", None) != None

    @property
    def user_id(self):
        return self.session.get("user", {}).get("id", None)

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
                if path == "api/config":
                    fields = [
                        dict(name=f.name, type=f.type)
                        for f in self.db.auth_user
                        if f.type in ["string", "bool", "integer", "float"]
                        and f.writable
                        and f.readable
                    ]
                    return {
                        "allowed_actions": self.allowed_actions,
                        "plugins": ["local"] + [key for key in self.plugins],
                        "fields": fields,
                    }
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
                                # "email": username + "@localhost",
                                "sso_id": plugin_name + ":" + username,
                            }
                            # and register the user if we have one, just in case
                            if self.db:
                                user = self.get_or_register_user(data)
                                self.store_user_in_session(user["id"])
                        else:
                            data = self._error("Invalid Credentials")
                    # Else use normal login
                    else:
                        user, error = self.login(**vars)
                        if user:
                            self.session["user"] = {"id": user.id}
                            self.session["recent_activity"] = calendar.timegm(
                                time.gmtime()
                            )
                            self.session["uuid"] = str(uuid.uuid1())
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
                        user, vars.get("new_password"), vars.get("old_password")
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
            self.session.clear()
            # Somehow call revoke for active plugin
        elif path == "verify_email" and self.db:
            token = get_vars.get("token")
            if self.verify_email(token):
                next = b16d(token.split("/")[1])
                redirect(
                    next
                    or URL(
                        "auth",
                        "email_verified",
                        use_appname=self.use_appname_in_redirects,
                    )
                )
            else:
                redirect(
                    URL(
                        "auth",
                        "token_expired",
                        use_appname=self.use_appname_in_redirects,
                    )
                )
        env["path"] = path
        return Template("auth.html").transform(env)

    def store_user_in_session(self, user_id):
        self.session["user"] = {"id": user_id}
        self.session["recent_activity"] = calendar.timegm(time.gmtime())
        self.session["uuid"] = str(uuid.uuid1())

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
                    self.route,
                    "verify_email",
                    vars=dict(token=token),
                    scheme=True,
                    use_appname=self.use_appname_in_redirects,
                )
                self.send("verify_email", fields, link=link)
        elif self.registration_requires_approval:
            fields["action_token"] = "pending-approval"
            res = self.db.auth_user.validate_and_insert(**fields)
        else:
            fields["action_token"] = ""
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
        if user.action_token == "account-blocked":
            return (None, "Account is blocked")
        if user.action_token == "pending-approval":
            return (None, "Account needs to be approved")
        if CRYPT()(password)[0] == user.password:
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
                    self.route,
                    "reset_password",
                    vars=dict(token=token),
                    scheme=True,
                    use_appname=self.use_appname_in_redirects,
                )
                self.send("reset_password", user, link=link)
            return token

    def verify_email(self, token):
        if self.registration_requires_approval:
            action_token = "pending-approval"
        else:
            action_token = None
        n = self.db(self._query_from_token(token)).update(action_token=action_token)
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

    def change_password(
        self, user, new_password, old_password=None, check=True, check_old_password=True
    ):
        db = self.db
        if check:
            if check_old_password:
                pwd = CRYPT()(old_password)[0]
                if not pwd == user.password:
                    return {"errors": {"old_password": "invalid current password"}}
            new_pwd, error = db.auth_user.password.validate(new_password)
            if error:
                return {"errors": {"new_password": error}}
            if new_pwd == user.password:
                return {
                    "errors": {
                        "new_password": "new password is the same as previous password"
                    }
                }
            if self.block_previous_password_num:
                past_pwds = (user.past_passwords_hash or [])[
                    : self.block_previous_password_num
                ]
                if any(new_pwd == old_pwd for old_pwd in past_pwds):
                    return {"errors": {"new_password": "new password was already used"}}
                else:
                    past_pwds.insert(0, pwd)
                    db(db.auth_user.id == user.id).update(past_passwords_hash=past_pwds)
        num = db(db.auth_user.id == user.id).update(
            password=new_pwd, last_password_change=datetime.datetime.utcnow()
        )
        return {"updated": num}

    def change_email(self, user, new_email, password=None, check=True):
        db = self.db
        if check and not db.auth_user.password.validate(password)[0] == user.password:
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

    def enable_record_versioning(
        self,
        tables,
        archive_db=None,
        archive_names="%(tablename)s_archive",
        current_record="current_record",
        current_record_label=None,
    ):
        """
        Used to enable full record versioning (including auth tables)::

            auth = Auth(db)
            auth.define_tables()
            # define our own tables
            db.define_table(
                'mything',
                Field('name'),
                auth.signature)
            auth.enable_record_versioning(tables=db)

        tables can be the db (all table) or a list of tables.
        only tables with modified_by and modified_on fiels (as created
        by auth.signature) will have versioning. Old record versions will be
        in table 'mything_archive' automatically defined.
        when you enable enable_record_versioning, records are never
        deleted but marked with is_active=False.

        enable_record_versioning enables a common_filter for
        every table that filters out records with is_active = False

        Note:
            If you use auth.enable_record_versioning,
            do not use auth.archive or you will end up with duplicates.
            auth.archive does explicitly what enable_record_versioning
            does automatically.
        """
        current_record_label = (
            current_record_label or current_record.replace("_", " ").title()
        )
        for table in tables:
            fieldnames = table.fields()
            if (
                "id" in fieldnames
                and "modified_on" in fieldnames
                and current_record not in fieldnames
            ):
                table._enable_record_versioning(
                    archive_db=archive_db,
                    archive_name=archive_names,
                    current_record=current_record,
                    current_record_label=current_record_label,
                )

    def form(self, action_name, **attr):
        # FIXME: check allowed_actions
        if not hasattr(self, "_forms"):
            self._forms = AuthForms(self)
        return getattr(self._forms, action_name)(**attr)


class AuthForms:
    def __init__(self, auth):
        self.auth = auth

    def register(self):
        self.auth.db.auth_user.password.writable = True
        form = Form(self.auth.db.auth_user, dbio=False)
        user = None
        if form.submitted:
            res = self.auth.register(form.vars)
            form.accepted = not res.get("errors")
            form.errors = res.get("errors")
        self._postprocessng("register", form, user)
        return form

    def login(self):
        form = Form([Field("username"), Field("password", type="password")])
        user = None
        if form.submitted:
            user, error = self.auth.login(
                form.vars.get("username"), form.vars.get("password")
            )
            form.accepted = not error
            form.errors["username"] = error
            if user:
                self.auth.store_user_in_session(user["id"])
        self._postprocessng("login", form, user)
        return form

    def reset_password(self):
        form = Form([Field("password", type="password")])
        user = None
        token = request.query.get("token")
        if token:
            query = self.auth._query_from_token(token)
            user = self.auth.db(query).select().first()
            if not user:
                raise HTTP(404)
        user = self.auth.db.auth_user(self.auth.user_id)
        form = Form(
            [
                Field(
                    "new_password",
                    type="password",
                    requires=self.auth.db.auth_user.password.requires,
                ),
                Field("new_password_again", type="password", requires=IS_NOT_EMPTY()),
            ]
        )
        if form.submitted:
            new_password = form.post_vars.get("new_password")
            if form.post_vars["new_password_again"] != new_password:
                form.errors["new_password_again"] = "Passwords do not match"
                form.accepted = False
            else:
                res = self.auth.change_password(
                    user, new_password, check=True, check_old_password=False
                )
            form.errors = re.get("errors", {})
            form.accepted = not res.get("errors")
        self._postprocessng("profile", form, user)
        return form

    def change_password(self):
        self._check_logged("change_password")
        user = self.auth.db.auth_user(self.auth.user_id)
        form = Form(
            [
                Field("old_password", type="password", requires=IS_NOT_EMPTY()),
                Field(
                    "new_password",
                    type="password",
                    requires=self.auth.db.auth_user.password.requires,
                ),
                Field("new_password_again", type="password", requires=IS_NOT_EMPTY()),
            ]
        )
        if form.submitted:
            old_password = form.post_vars.get("new_password")
            new_password = form.post_vars.get("new_password")
            if form.post_vars["new_password_again"] != new_password:
                form.errors["new_password_again"] = "Passwords do not match"
                form.accepted = False
            else:
                res = self.auth.change_password(
                    user, new_password, old_password, check=True
                )
            form.errors = re.get("errors", {})
            form.accepted = not res.get("errors")
        self._postprocessng("profile", form, user)
        return form

    def profile(self):
        self._check_logged("profile")
        user = self.auth.db.auth_user(self.auth.user_id)
        form = Form(self.auth.db.auth_user, user)
        self._postprocessng("profile", form, user)
        return form

    def _check_logged(self, action):
        if not self.auth.is_logged_in:
            redirect(URL("index"))

    def _postprocessng(self, action, form, user):
        if form.accepted:
            redirect(URL("index"))
