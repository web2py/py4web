import base64
import calendar
import copy
import hashlib
import random
import re
import time
import uuid

import jwt

from pydal.validators import (
    CRYPT,
    IS_EMAIL,
    IS_EQUAL_TO,
    IS_MATCH,
    IS_NOT_EMPTY,
    IS_NOT_IN_DB,
    IS_STRONG,
)
from yatl.helpers import DIV, A

from py4web import HTTP, URL, Field, action, redirect, request, response
from py4web.core import REGEX_APPJSON, Fixture, Flash, Template, Translator, utcnow
from py4web.utils.form import Form, FormStyleDefault
from py4web.utils.param import Param

"""
[X] Enable and disable plugins
[X] Enable and disable actions
[X] Require passwords of various complexity
[x] Force logout after x hours (WIP)
[X] No re-use of the last n passwords
[ ] Force new password on first login (WIP)
[ ] Two-factor authentication for users with 'administrator' access
[ ] Lock account after x failed login attempts.
[ ] Force new password every x days.
"""


def b16e(text):
    """convert unicode to b16 unicode"""
    return base64.b16encode(text.encode()).decode()


def b16d(text):
    """convert unicode to b16 unicode"""
    return base64.b16decode(text.encode()).decode()


def prevent_open_redirect(url):
    """url must be a valid absolute URL whithout schema"""
    if url and url[0] == "/" and "//" not in url:
        return url
    return None


class AuthEnforcer(Fixture):
    """Base fixture that checks if a condition is met.

    If not it redirects to a different page or returns HTTP 403
    """

    def __init__(self, auth, condition=None):
        self.__prerequisites__ = [auth]
        self.auth = auth
        self.condition = condition

    def on_success(self, context):
        self.auth.on_success(context)

    def abort_or_redirect(self, page, message=""):
        """
        Return HTTP 403 if 'text/htmp' not in HTTP_ACCEPT
        else redirects to specified page
        """

        if "text/html" not in request.headers.get("accept", ""):
            raise HTTP(403, body={"message": message})
        redirect_next = request.fullpath
        if request.query_string:
            redirect_next = redirect_next + "?{}".format(request.query_string)
        self.auth.flash.set(message)
        redirect(
            URL(
                self.auth.route,
                page,
                vars=dict(next=redirect_next),
                use_appname=self.auth.param.use_appname_in_redirects,
            )
        )

    def goto_login(self, message=""):
        """Goes to the proper login page."""
        # If a plugin can handle requests, redirects to the login url for the login.
        for plugin in self.auth.plugins.values():
            if hasattr(plugin, "handle_request"):
                if re.search(REGEX_APPJSON, request.headers.get("accept", "")) and (
                    request.headers.get("json-redirects", "") != "on"
                ):
                    raise HTTP(403)
                redirect_next = request.fullpath
                if request.query_string:
                    redirect_next = redirect_next + "?{}".format(request.query_string)
                redirect(
                    URL(
                        self.auth.route,
                        "plugin",
                        plugin.name,
                        "login",
                        vars=dict(next=redirect_next),
                    )
                )
        # Otherwise, uses the normal login.
        self.abort_or_redirect("login", message=message)

    def on_request(self, context):
        """Checks that we have a user in the session and
        the condition is met"""
        self.auth.on_request(context)

        if "user" not in self.auth.session or "id" not in self.auth.session["user"]:
            self.goto_login(message="Login required")

        if callable(self.condition) and not self.condition(user):
            self.abort_or_redirect("not-authorized", "User not authorized")


class Auth(Fixture):
    """The Auth object is responsible for handling
    authentication and authorization"""

    MESSAGES = {
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
        "flash": {
            "user-registered": "User registered",
            "password-reset-link-sent": "Password reset link sent",
            "password-changed": "Password changed",
            "profile-saved": "Profile saved",
            "user-logout": "User logout",
            "email-verified": "Email verified",
            "link-expired": "Link invalid or expired",
        },
        "labels": {
            "username": "Username",
            "email": "Email",
            "first_name": "First Name",
            "last_name": "Last Name",
            "phone_number": "Phone Number",
            "username_or_email": "Username or Email",
            "password": "Password",
            "new_password": "New Password",
            "old_password": "Old Password",
            "login_password": "Password",
            "password_again": "Password (again)",
            "created_on": "Created On",
            "created_by": "Created By",
            "modified on": "Modified On",
            "modified by": "Modified By",
            "two_factor": "Authentication Code",
        },
        "buttons": {
            "lost-password": "Lost Password",
            "register": "Register",
            "request": "Request",
            "sign-in": "Sign In",
            "sign-up": "Sign Up",
            "submit": "Submit",
        },
        "errors": {
            "registration_is_pending": "Registration is pending",
            "account_is_blocked": "Account is blocked",
            "account_needs_to_be_approved": "Account needs to be approved",
            "invalid_credentials": "Invalid Credentials",
            "invalid_token": "invalid token",
            "password_doesnt_match": "Password doesn't match",
            "invalid_current_password": "invalid current password",
            "new_password_is_the_same_as_previous_password": "new password is the same as previous password",
            "new_password_was_already_used": "new password was already used",
            "invalid": "invalid",
            "no_post_payload": "no post payload",
            "two_factor": "Verification code does not match",
            "two_factor_max_tries": "Two factor max tries exceeded",
        },
    }

    BUTTON_CLASSES = {
        "lost-password": "white",
        "register": "white",
        "request": "white",
        "sign-in": "white",
        "sign-up": "white",
        "submit": "white",
    }

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
        extra_fields=None,
        extra_form_fields=None,
        login_expiration_time=3600,  # seconds
        password_complexity="default",
        block_previous_password_num=None,
        allowed_actions=None,
        use_appname_in_redirects=None,
        password_in_db=True,
        two_factor_required=None,
        two_factor_send=None,
        two_factor_validate=None,
        template_args=None,
    ):
        # configuration parameters
        self.param = Param(
            registration_requires_confirmation=registration_requires_confirmation,
            registration_requires_approval=registration_requires_approval,
            login_after_registration=False,
            login_expiration_time=login_expiration_time,  # seconds
            password_complexity=(
                {"entropy": 50}
                if password_complexity == "default"
                else password_complexity
            ),
            block_previous_password_num=block_previous_password_num,
            allowed_actions=allowed_actions or ["all"],
            use_appname_in_redirects=use_appname_in_redirects,
            formstyle=FormStyleDefault,
            messages=copy.deepcopy(self.MESSAGES),
            button_classes=copy.deepcopy(self.BUTTON_CLASSES),
            default_login_enabled=True,
            exclude_extra_fields_in_register=None,
            exclude_extra_fields_in_profile=None,
            expose_all_models=True,
            two_factor_required=two_factor_required,
            two_factor_send=two_factor_send,
            two_factor_validate=two_factor_validate,
            two_factor_tries=3,
            auth_enforcer=None,
            template_args=template_args or {},
        )

        # callbacks for forms
        self.on_accept = {}

        self.__prerequisites__ = []
        self.inject = inject
        if session:
            self.__prerequisites__.append(session)
        if db:
            self.__prerequisites__.append(db)
        self.flash = Flash()
        self.__prerequisites__.append(self.flash)
        self.onsuccess = {}
        self.db = db
        self.session = session
        self.sender = sender
        self.route = "auth"
        self.use_username = use_username  # if False, uses email only
        self.password_in_db = password_in_db  # if False, password is never saved in db
        self.use_phone_number = use_phone_number
        # The self._link variable is not thread safe (only intended for testing)
        self.extra_auth_user_fields = extra_fields or []
        self.extra_form_fields = extra_form_fields or {}
        self._link = None
        if db and define_tables:
            self.define_tables()
        # these are plugins like SAML, OAuth2, etc which delegate authentication
        self.plugins = {}
        # these are plugins that can retrieve an existing user from a given token
        self.token_plugins = []
        self.form_source = DefaultAuthForms(self)
        self.fix_actions()

    def on_request(self, context):
        """Checks that we have a user in the session and
        the condition is met"""

        # check if a valid user in session
        user = self.session.get("user")

        # else try if this is an API call with token
        is_token = False
        if not user:
            for plugin in self.token_plugins:
                user = plugin.get_user()
                if user:
                    is_token = True
                    break

        if not is_token:
            # handle the case without a token
            if user:
                activity = self.session.get("recent_activity")
                time_now = calendar.timegm(time.gmtime())
                # enforce the optionl auth session expiration time
                if "id" not in user or (
                    self.param.login_expiration_time
                    and activity
                    and time_now - activity > self.param.login_expiration_time
                ):
                    del self.session["user"]
                elif not activity or time_now - activity > 6:
                    self.session["recent_activity"] = time_now
            self.session["recent_timestamp"] = utcnow().isoformat()
        else:
            # handle the case with a token, no checks required
            self.session["user"] = user

    def allows(self, action_name):
        """Checks if the provided action is allowed on the Auth object"""
        return (
            "all" in self.param.allowed_actions
            or action_name in self.param.allowed_actions
        )

    def fix_actions(self):
        """Cleanup duplicated and expand 'all' allowed_actions on API and Forms"""
        ALL_ALLOWED_ACTIONS = list(
            set(
                AuthAPI.public_api
                + AuthAPI.private_api
                + DefaultAuthForms.public_forms
                + DefaultAuthForms.private_forms
                + DefaultAuthForms.no_forms
            )
        )
        # "login",
        # "logout",
        # "request_reset_password",
        # "reset_password",
        # "change_password",
        # "change_email",
        # "profile",
        # "config",
        # "register",
        # "verify_email",
        # "unsubscribe",

        if "all" in self.param.allowed_actions:
            self.param.allowed_actions = ALL_ALLOWED_ACTIONS
        else:
            # remove duplicates and unknown actions
            self.param.allowed_actions = list(set(self.param.allowed_actions))
            for unknown in self.param.allowed_actions:
                if unknown not in ALL_ALLOWED_ACTIONS:
                    self.param.allowed_actions.remove(unknown)

    def deny_action(self, action_name):
        """Deny the provided action on the Auth object"""

        self.fix_actions()
        if action_name in self.param.allowed_actions:
            self.param.allowed_actions.remove(action_name)

    def on_success(self, context):
        if self.inject:
            context["template_inject"]["user"] = self.get_user()

    def define_tables(self):
        """Defines the auth_user table"""
        db = self.db
        if "auth_user" not in db.tables:
            ne = IS_NOT_EMPTY()
            if self.param.password_complexity:
                requires = [IS_STRONG(**self.param.password_complexity), CRYPT()]
            else:
                requires = [CRYPT()]
            auth_fields = [
                Field(
                    "email",
                    requires=(IS_EMAIL(), IS_NOT_IN_DB(db, "auth_user.email")),
                    unique=True,
                    label=self.param.messages["labels"].get("email"),
                ),
                Field(
                    "password",
                    "password",
                    requires=requires,
                    readable=False,
                    writable=False,
                    label=self.param.messages["labels"].get("password"),
                ),
                Field(
                    "first_name",
                    requires=ne,
                    label=self.param.messages["labels"].get("first_name"),
                ),
                Field(
                    "last_name",
                    requires=ne,
                    label=self.param.messages["labels"].get("last_name"),
                ),
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
                        label=self.param.messages["labels"].get("username"),
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
                        label=self.param.messages["labels"].get("phone_number"),
                    ),
                )
            if self.param.block_previous_password_num is not None:
                auth_fields.append(
                    Field(
                        "past_passwords_hash",
                        "list:string",
                        writable=False,
                        readable=False,
                    )
                )
            db.define_table(
                "auth_user",
                *(auth_fields + self.extra_auth_user_fields),
                format=lambda u: f"{u.first_name} {u.last_name}",
            )

    @property
    def signature(self):
        """Returns a list of fields for a table signature"""
        now = lambda: utcnow()
        user = lambda s=self: s.user_id
        fields = [
            Field(
                "created_on",
                "datetime",
                default=now,
                writable=False,
                readable=True,
                label=self.param.messages["labels"].get("created_on"),
            ),
            Field(
                "created_by",
                "reference auth_user",
                default=user,
                writable=False,
                readable=True,
                label=self.param.messages["labels"].get("created_by"),
            ),
            Field(
                "modified_on",
                "datetime",
                update=now,
                default=now,
                writable=False,
                readable=True,
                label=self.param.messages["labels"].get("modified_on"),
            ),
            Field(
                "modified_by",
                "reference auth_user",
                default=user,
                update=user,
                writable=False,
                readable=True,
                label=self.param.messages["labels"].get("modified_by"),
            ),
            Field(
                "is_active",
                "boolean",
                default=True,
                readable=False,
                writable=False,
                label=self.param.messages["labels"].get("is_active"),
            ),
        ]
        return fields

    # Validation fixtures
    @property
    def user(self):
        """Use as @action.uses(auth.user)"""
        return (
            self.param.auth_enforcer if self.param.auth_enforcer else AuthEnforcer(self)
        )

    def condition(self, condition):
        """Use as @action.uses(auth.condition(lambda user: True))"""
        return (
            self.param.auth_enforcer
            if self.param.auth_enforcer
            else AuthEnforcer(self, condition)
        )

    # utilities
    def get_user(self, safe=True):
        """Extracts the user from the session.

        Returns {} if no user in the session.
        If session contains only a user['id']
        retrives the other readable user info from auth_user
        """
        if not self.session.is_valid() or not self.user_id:
            return {}
        if self.db:
            user = self.db.auth_user(self.user_id)
            if not user:
                return {}
            if safe:
                user = {
                    f.name: user[f.name]
                    for f in self.db.auth_user
                    if f.readable or f.name == "id"
                }
        return user

    @property
    def is_logged_in(self):
        if not self.session.is_valid():
            return False
        return self.session.get("user", {}).get("id", None) is not None

    @property
    def user_id(self):
        if not self.session.is_valid():
            return None
        user = self.session.get("user")
        if not user:
            # handles corner case: session=dict(user=None)
            return None
        else:
            return user.get("id", None)

    @property
    def current_user(self):
        return self.get_user()

    def start_impersonating(self, impersonated_id, next_url):
        """impersonates the new user"""
        user = self.session.get("user")
        if not user or "id" not in user:
            raise RuntimeError("Cannot impersonate if not logged in")
        if "impersonator_id" in user:
            raise RuntimeError("Cannot impersonate while impersonating")
        if impersonated_id == self.user_id:
            raise RuntimeError("Cannot impersonate yourself")
        self.session.clear()
        self.store_user_in_session(impersonated_id)
        self.session["user"]["impersonator_id"] = user["id"]
        redirect(next_url)

    def is_impersonating(self):
        """checks if we are impersonating a user"""
        return self.session.get("user", {}).get("impersonator_id", None) is not None

    def stop_impersonating(self, next_url):
        """stops impersonating a user, assuming we are impersonating one"""
        user = self.session.get("user")
        impersonator_id = (user or {}).get("impersonator_id")
        if impersonator_id is None:
            raise RuntimeError(
                "Cannot stop impersonation because not impersonating anybody"
            )
        self.session.clear()
        self.store_user_in_session(impersonator_id)
        redirect(next_url)

    def register_plugin(self, plugin):
        """Registers an Auth plugin, usually from common.py inside apps"""
        self.plugins[plugin.name] = plugin
        # special parameters values depending on the plugins
        if plugin.name in ["pam", "ldap"]:
            self.password_in_db = False
            self.deny_action("change_password")
            self.deny_action("request_reset_password")

    def store_user_in_session(self, user_id):
        self.session["user"] = {"id": user_id}
        self.session["recent_activity"] = calendar.timegm(time.gmtime())
        self.session["uuid"] = str(uuid.uuid1())

    # Methods that do not assume a user

    def register(self, fields, send=True, next="", validate=True, route=None):
        """Registers a new user after the user's parameters are entered
        in the SignUp form"""
        if "username" in fields:
            fields["username"] = fields["username"].lower()
        fields["email"] = fields.get("email", "").lower()

        def store(fields):
            if validate:
                if self.use_username:
                    self.db.auth_user.username.required = True
                self.db.auth_user.action_token.writable = True
                self.db.auth_user.password.writable = True
                self.db.auth_user.password.required = True
                self.db.auth_user.first_name.required = True
                self.db.auth_user.last_name.required = True
                return self.db.auth_user.validate_and_insert(**fields)
            return dict(id=self.db.auth_user.insert(**fields))

        if self.param.registration_requires_confirmation:
            token = str(uuid.uuid4())
            if next:
                token += "/" + b16e(next)
            fields["action_token"] = "pending-registration:%s" % token
            res = store(fields)
            if send and res.get("id"):
                self._link = link = URL(
                    route or self.route,
                    "verify_email",
                    vars=dict(token=token),
                    scheme=True,
                    use_appname=self.param.use_appname_in_redirects,
                )
                self.send("verify_email", fields, link=link)
        elif self.param.registration_requires_approval:
            fields["action_token"] = "pending-approval"
            res = store(fields)
        else:
            fields["action_token"] = ""
            res = store(fields)
            if self.param.login_after_registration and not res.get("errors"):
                self.store_user_in_session(res["id"])
        return res

    def login(self, email, password):
        """Login a new user after the user's parameters are entered
        in the Login form"""
        db = self.db

        # Default email and password in case they are None or an error will occur.
        email = "" if email is None else email
        password = "" if password is None else password

        user = None
        error = None
        prevent_db_lookup = False
        # first check if we have a plugin that can check credentials

        for plugin in self.plugins.values():
            if not hasattr(plugin, "get_login_url"):
                prevent_db_lookup = True
                if plugin.check_credentials(email, password):
                    # if the creadentials are independently validated
                    # get of create the user (if does not exist)
                    user_info = {}
                    user_info["sso_id"] = plugin.name + ":" + email
                    if self.use_username or "@" not in email:
                        user_info["username"] = email
                    if "@" in email:
                        user_info["email"] = email
                    else:
                        user_info["email"] = email + "@example.com"
                    user = self.get_or_register_user(user_info)
                    break

        # else check against database
        if not prevent_db_lookup:
            value = email.lower()
            field = (
                db.auth_user.email
                if "@" in value or not self.use_username
                else db.auth_user.username
            )
            user = db(field == value).select().first()
            if user and not (CRYPT()(password)[0] == user.password):
                user = None

        # then check for possible login blockers
        if not user:
            error = "invalid_credentials"
        elif (user.get("action_token") or "").startswith("pending-registration:"):
            error = "registration_is_pending"
        elif user.get("action_token") == "account-blocked":
            error = "account_is_blocked"
        elif user.get("action_token") == "pending-approval":
            error = "account_needs_to_be_approved"

        # return the error or the user
        if error:
            return (None, self.param.messages["errors"].get(error, error))
        return (user, None)

    def request_reset_password(self, email, send=True, next="", route=None):
        """Send a mail with token for changing user's password after the user's parameters are entered
        in the request_reset_password form
        """

        db = self.db
        value = email.lower()
        field = (
            db.auth_user.email
            if "@" in value or not self.use_username
            else db.auth_user.username
        )
        user = db(field == value).select().first()
        if user and user.action_token != "account-blocked":
            token = str(uuid.uuid4())
            if next:
                token += "/" + b16e(next)
            user.update_record(action_token="reset-password-request:" + token)
            if send:
                self._link = link = URL(
                    route or self.route,
                    "reset_password",
                    vars=dict(token=token),
                    scheme=True,
                    use_appname=self.param.use_appname_in_redirects,
                )
                self.send("reset_password", user, link=link)
            return token

    def verify_email(self, token):
        if self.param.registration_requires_approval:
            action_token = "pending-approval"
        else:
            action_token = None
        n = self.db(self._query_from_token(token)).update(action_token=action_token)
        return n > 0

    def reset_password(self, token, new_password, new_password2):
        db = self.db
        query = self._query_from_token(token)
        user = db(query).select().first()

        if not user:
            return {
                "errors": {"token": self.param.messages["errors"].get("invalid_token")}
            }

        if new_password != new_password2:
            return {
                "errors": {
                    "new_password2": self.param.messages["errors"].get(
                        "password_doesnt_match"
                    )
                }
            }

        qset = db(db.auth_user.id == user["id"])
        value, error = db.auth_user.password.validate(new_password)
        if error:
            return {"errors": {"new_password": error}}
        qset.update(password=value)
        return {}

    # Methods that assume a user

    def change_password(
        self, user, new_password, old_password=None, check=True, check_old_password=True
    ):
        db = self.db
        if check:
            if check_old_password:
                pwd = CRYPT()(old_password)[0]
                if not (pwd and pwd == user.get("password")):
                    return {
                        "errors": {
                            "old_password": self.param.messages["errors"].get(
                                "invalid_current_password"
                            )
                        }
                    }
            new_pwd, error = db.auth_user.password.validate(new_password)
            if error:
                return {"errors": {"new_password": error}}
            if new_pwd == user.password:
                return {
                    "errors": {
                        "new_password": self.param.messages["errors"].get(
                            "new_password_is_the_same_as_previous_password"
                        )
                    }
                }
            if self.param.block_previous_password_num:
                past_pwds = (user.past_passwords_hash or [])[
                    : self.param.block_previous_password_num
                ]
                if any(new_pwd == old_pwd for old_pwd in past_pwds):
                    return {
                        "errors": {
                            "new_password": self.param.messages["errors"].get(
                                "new_password_was_already_used"
                            )
                        }
                    }
                past_pwds.insert(0, user.get("password"))
                db(db.auth_user.id == user.get("id")).update(
                    past_passwords_hash=past_pwds
                )
        num = db(db.auth_user.id == user.get("id")).update(
            password=new_pwd, last_password_change=utcnow()
        )
        return {"updated": num}

    def change_email(self, user, new_email, password=None, check=True):
        db = self.db
        if check and CRYPT()(password)[0] != user.get("password"):
            return {
                "errors": {"password": self.param.messages["errors"].get("invalid")}
            }
        return db(db.auth_user.id == user.get("id")).validate_and_update(
            email=new_email
        )

    def update_profile(self, user, **fields):
        db = self.db
        errors = {
            k: self.param.messages["errors"].get("invalid")
            for k in fields
            if k not in db.auth_user.fields or not db.auth_user[k].writable
        }
        if errors:
            return {"errors": errors}
        return db(db.auth_user.id == user.get("id")).validate_and_update(**fields)

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

    def get_or_delete_existing_unverified_account(self, email):
        db = self.db
        row = db(db.auth_user.email == email).select(limitby=(0, 1)).first()
        # if we have a user with this email and incomplete registration delete it
        if (
            row
            and row.action_token
            and row.action_token.startswith("pending-registration:")
        ):
            row.delete_record()
            return None
        return row

    def get_or_register_user(self, user):
        db = self.db
        # if we have an sso_id we use it to id the user
        if user.get("sso_id"):
            keyid = "sso_id"
            row = (
                db(db.auth_user.sso_id == user["sso_id"]).select(limitby=(0, 1)).first()
            )
            # the sso source is always more authoritative so update the record
            if row:
                row.update_record(**user)
                # pass the full user
                user = row.as_dict()
        # othrewise we id the user via email
        elif user.get("email"):
            keyid = "email"
            # return a user if exists and has a verified email
            row = self.get_or_delete_existing_unverified_account(user["email"])
            # the database is more authoritative
            if row:
                user.update(**row.as_dict())
        else:
            return None
        # if we do not have a candidate user we create one
        if not row:
            # if we expect a username but not provided, use keyid as username
            if self.use_username:
                if "username" not in user:
                    user["username"] = user[keyid]
                    # make sure the username is unique
                    if db(db.auth_user.username == user["username"]).count():
                        raise HTTP(401, body=f"Conficting {user['username']} accounts")
            # create the user
            user["id"] = db.auth_user.insert(**db.auth_user._filter_fields(user))
        return user

    # Private methods

    def _query_from_token(self, token):
        query = self.db.auth_user.action_token == "reset-password-request:%s" % token
        query |= self.db.auth_user.action_token == "pending-registration:%s" % token
        return query

    def _error(self, message, code=400):
        return {"status": "error", "message": message, "code": code}

    def _success(self, message, code=200):
        return {"status": "success", "message": message, "code": code}

    # Other service methods (that can be overwritten)

    def send(self, name, user, **attrs):
        """Extends the object and override the function to send messages with
        twilio or onesignal or alternative method other than email
        """

        message = self.param.messages[name]
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
        only tables with modified_by and modified_on fields (as created
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

    def enable(self, route="auth", uses=(), env=None, spa=False, allow_api_routes=True):
        """Enables Auth, aka generates login/logout/register/etc API pages"""
        self.route = route = route.rstrip("/")
        env = env or {}
        auth = self

        translators = [fixture for fixture in uses if isinstance(fixture, Translator)]
        if translators:
            T = translators[0]
            for group in self.param.messages.values():
                for key, value in group.items():
                    group[key] = T(value)

        methods = ["GET", "POST", "OPTIONS"]

        # This exposes all API actions as /{app_name}/{route}/api/{name}
        # and API Models as /{app_name}/{route}/api/{name}?@model=true
        exposed_api_routes = []
        if allow_api_routes:
            # Exposed Public APIs
            exposed_api_routes = [
                dict(api_name=api_name, api_route=f"{route}/api/{api_name}", uses=auth)
                for api_name in AuthAPI.public_api
                if self.allows(api_name)
            ]

            # Exposed Private APIs
            exposed_api_routes.extend(
                [
                    dict(
                        api_name=api_name,
                        api_route=f"{route}/api/{api_name}",
                        uses=auth.user,
                    )
                    for api_name in AuthAPI.private_api
                    if self.allows(api_name)
                ]
            )

            for item in exposed_api_routes:
                api_factory = getattr(AuthAPI, item["api_name"])

                @action(item["api_route"], method=methods)
                @action.uses(item["uses"], *uses)
                def _(auth=auth, api_factory=api_factory):
                    return api_factory(auth)

        # This exposes all plugins as /{app_name}/{route}/plugins/{path}
        for name in self.plugins:

            @action(f"{route}/plugin/{name}/<path:path>", method=["GET", "POST"])
            @action.uses(auth, *uses)
            def _(path, plugin=self.plugins[name], name=name):
                return plugin.handle_request(self, path, request.query, request.json)

        # Don't expose the form routes if this is an API based Single Page Application.
        if not spa:
            exposed_form_routes = [
                dict(form_name=form_name, form_route=f"{route}/{form_name}", uses=auth)
                for form_name in self.form_source.public_forms
                if self.allows(form_name)
            ]

            exposed_form_routes.extend(
                [
                    dict(
                        form_name=form_name,
                        form_route=f"{route}/{form_name}",
                        uses=auth.user,
                    )
                    for form_name in self.form_source.private_forms
                    if self.allows(form_name)
                ]
            )

            exposed_form_routes.extend(
                [
                    dict(
                        form_name=form_name,
                        form_route=f"{route}/{form_name}",
                        uses=auth,
                    )
                    for form_name in self.form_source.no_forms
                    if self.allows(form_name)
                ]
            )

            for item in exposed_form_routes:
                form_factory = getattr(self.form_source, item["form_name"])
                template = Template(f"{route}.html", **self.param.template_args)

                @action(item["form_route"], method=["GET", "POST"])
                @action.uses(template, item["uses"], self.flash, *uses)
                def _(
                    auth=auth,
                    form_factory=form_factory,
                    path=item["form_name"],
                    env=env,
                ):
                    return dict(
                        form=form_factory(), path=path, user=auth.get_user(), **env
                    )

    def form(self, name, **attr):
        form_factory = getattr(self.form_source, name, None)
        if not form_factory:
            raise HTTP(404)
        return form_factory()


def api_wrapper(func):
    """Validates API calls"""

    def func_wrapper(auth, func=func):
        data = func(auth) or {}
        if "status" not in data and data.get("errors"):
            data.update(status="error", message="validation errors", code=401)
        elif "errors" in data and not data["errors"]:
            del data["errors"]
        data["status"] = data.get("status", "success")
        response.status = data["code"] = data.get("code", 200)
        return data

    return func_wrapper


class AuthAPI:
    """AuthAPI class.

    Defines all the public and private API methods
    """

    public_api = [
        "all_models",
        "config",
        "register",
        "login",
        "logout",
        "request_reset_password",
        "reset_password",
        "verify_email",
    ]

    private_api = ["profile", "change_password", "change_email", "unsubscribe"]

    model_apis = [
        "register",
        "login",
        "logout",
        "request_reset_password",
        "reset_password",
        "verify_email",
        "profile",
        "change_password",
    ]

    @staticmethod
    @api_wrapper
    def all_models(auth):
        if not auth.param.expose_all_models:
            return HTTP(404)
        available_models = [item for item in AuthAPI.model_apis if auth.allows(item)]
        request.query["@model"] = "true"
        response_remove_fields = ["code", "status"]
        all_models = dict()

        for model in available_models:
            current_model = getattr(AuthAPI, model)(auth)

            for remove in response_remove_fields:
                current_model.pop(remove, None)

            all_models[model] = current_model

        return all_models

    @staticmethod
    def model_request(route):
        return (request.query.get("@model", None) == "true") and (
            route in AuthAPI.model_apis
        )

    @staticmethod
    def get_model(defaultAuthFunction):
        model = defaultAuthFunction(model=True)

        for key, value in model.items():
            if key.lower() == "fields":
                formatted_fields = []

                for field in value:
                    formatted_fields.append(
                        dict(
                            name=field.name,
                            type=field.type,
                            label=field.label,
                            readable=field.readable,
                            writable=field.writable if field.type != "id" else False,
                            required=field.required,
                            regex=field.regex if hasattr(field, "regex") else None,
                            default=(
                                field.default()
                                if callable(field.default)
                                else field.default
                            ),
                            options=field.options,
                        )
                    )

                model[key] = formatted_fields
                break

        return model

    @staticmethod
    @api_wrapper
    def config(auth):
        fields = [
            dict(name=f.name, type=f.type)
            for f in auth.db.auth_user
            if f.type in ["string", "bool", "integer", "float"]
            and f.writable
            and f.readable
        ]
        return {
            "allowed_actions": auth.param.allowed_actions,
            "plugins": ["local"] + [key for key in auth.plugins],
            "fields": fields,
            "use_username": auth.use_username,
        }

    @staticmethod
    @api_wrapper
    def register(auth):
        if AuthAPI.model_request("register"):
            return AuthAPI.get_model(defaultAuthFunction=auth.form_source.register)

        payload = request.POST if (request.json is None) else request.json

        if payload is None:
            return auth._error(auth.param.messages["errors"].get("no_post_payload"))
        auth.get_or_delete_existing_unverified_account(payload.get("email"))
        return auth.register(payload, send=True)

    @staticmethod
    @api_wrapper
    def login(auth):
        if AuthAPI.model_request("login"):
            return AuthAPI.get_model(defaultAuthFunction=auth.form_source.login)

        payload = request.POST if (request.json is None) else request.json

        if payload is None:
            return auth._error(auth.param.messages["errors"].get("no_post_payload"))
        username, password = payload.get("email"), payload.get("password")
        if not all(isinstance(_, str) for _ in [username, password]):
            return auth._error(auth.param.messages["errors"].get("invalid_credentials"))

        # Prioritize PAM or LDAP logins if enabled
        if "pam" in auth.plugins or "ldap" in auth.plugins:
            plugin_name = "pam" if "pam" in auth.plugins else "ldap"
            check = auth.plugins[plugin_name].check_credentials(username, password)
            if check:
                data = {
                    "username": username,
                    # "email": username + "@localhost",
                    "sso_id": plugin_name + ":" + username,
                }
                # and register the user if we have one, just in case
                if auth.db:
                    user = auth.get_or_register_user(data)
                    auth.store_user_in_session(user["id"])
                # else: if we're here - check is OK, but user is not in the session - is it right?
            else:
                data = auth._error(
                    auth.param.messages["errors"].get("invalid_credentials")
                )

        # Else use normal login
        else:
            user, error = auth.login(username, password)
            if user:
                auth.session["user"] = {"id": user.get("id")}
                auth.session["recent_activity"] = calendar.timegm(time.gmtime())
                auth.session["uuid"] = str(uuid.uuid1())
                user = {f.name: user[f.name] for f in auth.db.auth_user if f.readable}
                data = {"user": user}
            else:
                data = auth._error(error)
        return data

    @staticmethod
    @api_wrapper
    def request_reset_password(auth):
        if AuthAPI.model_request("request_reset_password"):
            return AuthAPI.get_model(
                defaultAuthFunction=auth.form_source.request_reset_password
            )

        payload = request.POST if (request.json is None) else request.json

        if payload is None:
            return auth._error(auth.param.messages["errors"].get("no_post_payload"))

        if "email" not in payload:
            payload["email"] = ""

        if not auth.request_reset_password(**payload):
            return auth._error("invalid user")
        return {}

    @staticmethod
    @api_wrapper
    def reset_password(auth):
        if AuthAPI.model_request("reset_password"):
            return AuthAPI.get_model(
                defaultAuthFunction=auth.form_source.reset_password
            )

        payload = request.POST if (request.json is None) else request.json

        # check the new_password2 only if passed
        if payload is None:
            return auth._error(auth.param.messages["errors"].get("no_post_payload"))
        return auth.reset_password(
            payload.get("token"),
            payload.get("new_password"),
            payload.get("new_password2", payload.get("new_password")),
        )

    @staticmethod
    @api_wrapper
    def verify_email(auth):
        if AuthAPI.model_request("verify_email"):
            return AuthAPI.get_model(defaultAuthFunction=auth.form_source.verify_email)

        token = request.query.get("token")
        verified = auth.verify_email(token)

        if not verified:
            return auth._error(auth.param.messages["flash"].get("link-expired"))
        return auth._success(auth.param.messages["flash"].get("email-verified"))

    @staticmethod
    @api_wrapper
    def logout(auth):
        if AuthAPI.model_request("logout"):
            return AuthAPI.get_model(defaultAuthFunction=auth.form_source.logout)

        auth.session.clear()

    @staticmethod
    @api_wrapper
    def unsubscribe(auth):
        # this needs to be refactored, needs some kind of confirmation
        auth.session["user"] = None
        auth.gdpr_unsubscribe(auth.get_user(), send=True)

    @staticmethod
    @api_wrapper
    def change_password(auth):
        if AuthAPI.model_request("change_password"):
            return AuthAPI.get_model(
                defaultAuthFunction=auth.form_source.change_password
            )

        payload = request.POST if (request.json is None) else request.json

        if payload is None:
            return auth._error(auth.param.messages["errors"].get("no_post_payload"))
        return auth.change_password(
            auth.get_user(safe=False),  # refactor make faster
            payload.get("new_password"),
            payload.get("old_password"),
        )

    @staticmethod
    @api_wrapper
    def change_email(auth):
        payload = request.POST if (request.json is None) else request.json

        if payload is None:
            return auth._error(auth.param.messages["errors"].get("no_post_payload"))
        return auth.change_email(
            auth.get_user(safe=False),
            payload.get("new_email"),
            payload.get("password"),
        )

    @staticmethod
    @api_wrapper
    def profile(auth):
        if AuthAPI.model_request("profile"):
            model = AuthAPI.get_model(defaultAuthFunction=auth.form_source.profile)
            model["user"] = auth.get_user()
            return model

        if request.method == "GET":
            return {"user": auth.get_user()}

        payload = request.POST if (request.json is None) else request.json

        if payload is None:
            return auth._error(auth.param.messages["errors"].get("no_post_payload"))
        else:
            return auth.update_profile(auth.get_user(), **payload)


class DefaultAuthForms:
    """Default Forms used for Auth actions"""

    public_forms = [
        "register",
        "login",
        "request_reset_password",
        "reset_password",
        "two_factor",
    ]
    private_forms = ["profile", "change_password"]  # change_email, unsubscribe
    no_forms = ["logout", "verify_email"]

    def __init__(self, auth):
        self.auth = auth

    @property
    def formstyle(self):
        return self.auth.param.formstyle

    def register(self, model=False):
        """SignUp form"""
        if "password" in self.auth.db.auth_user.fields:
            self.auth.db.auth_user.password.writable = True
            if self.auth.password_in_db:
                self.auth.db.auth_user.password.requires = [
                    IS_STRONG(**self.auth.param.password_complexity),
                    CRYPT(),
                ]
            else:
                self.auth.param.password_complexity = {"entropy": 0}
                self.auth.db.auth_user.password.requires = [
                    IS_STRONG(**self.auth.param.password_complexity)
                ]

        fields = [
            field
            for field in self.auth.db.auth_user
            if field.writable and field.type != "id"
        ]

        if self.auth.param.exclude_extra_fields_in_register:
            fields = [
                field
                for field in fields
                if field.name not in self.auth.param.exclude_extra_fields_in_register
            ]
        for k, field in enumerate(fields):
            if field.type == "password" and self.auth.password_in_db:
                fields.insert(
                    k + 1,
                    Field(
                        "password_again",
                        "password",
                        requires=IS_EQUAL_TO(request.forms.get("password")),
                        label=self.auth.param.messages["labels"].get("password_again"),
                    ),
                )
                break
        button_name = self.auth.param.messages["buttons"]["sign-up"]

        if model:
            additional_buttons = []
            if self.auth.allows("login"):
                additional_buttons.append(
                    dict(
                        label=self.auth.param.messages["buttons"]["sign-in"],
                        action="login",
                        href=URL(f"{self.auth.route}/api/login"),
                    )
                )

            if self.auth.allows("request_reset_password"):
                additional_buttons.append(
                    dict(
                        label=self.auth.param.messages["buttons"]["lost-password"],
                        action="request_reset_password",
                        href=URL(f"{self.auth.route}/api/request_reset_password"),
                    )
                )

            return dict(
                public=True,
                hidden=False,
                fields=fields,
                href=URL(f"{self.auth.route}/api/register"),
                submit_label=button_name,
                additional_buttons=additional_buttons,
            )

        # if the form is submitted, before any validation
        # delete any unverified account with the same email
        if request.method == "POST":
            email = request.forms.get("email")
            if email:
                self.auth.get_or_delete_existing_unverified_account(email)
        extra_form_fields = self.auth.extra_form_fields.get("register", [])
        fields += extra_form_fields
        form = Form(fields, submit_value=button_name, formstyle=self.formstyle)
        user = None
        if form.accepted:
            # notice that here the form is alrealdy validated
            if not self.auth.password_in_db:  # password must not be written in db
                # Prioritize PAM or LDAP logins if enabled
                if "pam" in self.auth.plugins or "ldap" in self.auth.plugins:
                    plugin_name = "pam" if "pam" in self.auth.plugins else "ldap"
                    check = self.auth.plugins[plugin_name].check_credentials(
                        form.vars["username"], form.vars["password"]
                    )
                    form.vars["password"] = ""
                    if not check:
                        self._set_flash("Invalid credentials")
                        redirect("register")
            extra_names = set(field.name for field in extra_form_fields)
            vars = {k: v for k, v in form.vars.items() if k not in extra_names}
            res = self.auth.register(vars, validate=False)
            form.errors.update(**res.get("errors", {}))
            form.accepted = not form.errors
        if form.accepted:
            self._set_flash("user-registered")
            self._postprocessing("register", form, user)
            if self.auth.param.login_after_registration:
                redirect("login")
        if self.auth.allows("login"):
            form.param.sidecar.append(
                A(
                    self.auth.param.messages["buttons"]["sign-in"],
                    _href=URL(f"{self.auth.route}/login"),
                    _class=self.auth.param.button_classes["sign-in"],
                    _role="button",
                )
            )
        if self.auth.allows("request_reset_password"):
            form.param.sidecar.append(
                A(
                    self.auth.param.messages["buttons"]["lost-password"],
                    _href=URL(f"{self.auth.route}/request_reset_password"),
                    _class=self.auth.param.button_classes["lost-password"],
                    _role="button",
                )
            )
        return form

    def login_buttons(self):
        """Define auth plugin type button to be displayed in login form"""
        top_buttons = []

        for name, plugin in self.auth.plugins.items():
            #  do not add a button for plugin that do not delegate to url
            if not hasattr(plugin, "get_login_url"):
                continue

            url = URL(f"{self.auth.route}/plugin/{name}/login")

            next_url = prevent_open_redirect(request.query.get("next"))
            if next_url:
                url = f"{url}?next={next_url}"

            top_buttons.append(
                dict(label=f"{plugin.label} Login", action=name, href=url)
            )

        combined_div = DIV(
            *[
                A(item["label"], _href=f"{item['href']}", _role="button")
                for item in top_buttons
            ]
        )

        return dict(buttons=top_buttons, combined_div=combined_div)

    def login(self, model=False):
        """Login form"""
        top_buttons = self.login_buttons()

        # if we do not allow we only display the plugin login buttons
        if not self.auth.param.default_login_enabled:
            if model:
                return top_buttons["buttons"]
            return top_buttons["combined_div"]

        fields = [
            Field(
                "email",
                label=(
                    self.auth.db.auth_user.username.label
                    if self.auth.use_username
                    else self.auth.db.auth_user.email.label
                ),
            ),
            Field(
                "password",
                type="password",
                label=self.auth.param.messages["labels"].get("password"),
            ),
        ]

        button_name = self.auth.param.messages["buttons"]["sign-in"]

        if model:
            additional_buttons = []
            if self.auth.allows("register"):
                additional_buttons.append(
                    dict(
                        label=self.auth.param.messages["buttons"]["sign-up"],
                        action="register",
                        href=URL(f"{self.auth.route}/api/register"),
                    )
                )

            if self.auth.allows("request_reset_password"):
                additional_buttons.append(
                    dict(
                        label=self.auth.param.messages["buttons"]["lost-password"],
                        action="request_reset_password",
                        href=URL(f"{self.auth.route}/api/request_reset_password"),
                    )
                )

            additional_buttons.extend(top_buttons["buttons"])

            return dict(
                public=True,
                hidden=False,
                fields=fields,
                href=URL(f"{self.auth.route}/api/login"),
                submit_label=button_name,
                additional_buttons=additional_buttons,
            )

        extra_form_fields = self.auth.extra_form_fields.get("login", [])
        fields += extra_form_fields
        form = Form(
            fields,
            submit_value=button_name,
            formstyle=self.formstyle,
        )
        user = None
        next_url = prevent_open_redirect(request.query.get("next"))
        self.auth.session["_next_login"] = next_url
        if form.submitted:
            user, error = self.auth.login(
                form.vars.get("email", ""), form.vars.get("password", "")
            )
            form.accepted = not error
            form.errors["password"] = error
        if user:
            #  We will process two_factor if two_factor_send is defined and either
            #  - No two_factor_required defined
            #    OR
            #  - two_factor_required() returns True
            #  If two_factor_required exists and returns False,
            #  then this user bypasses two_factor processing
            if self.auth.param.two_factor_send is not None:
                if (
                    not self.auth.param.two_factor_required
                    or self.auth.param.two_factor_required(user, request)
                ):
                    self.auth.session["auth.2fa_user"] = user["id"]
                    self.auth.session["auth.2fa_next_url"] = next_url
                    redirect(URL(f"{self.auth.route}/two_factor"))
            self.auth.store_user_in_session(user["id"])
            self._postprocessing("login", form, user)

        if self.auth.allows("register"):
            form.param.sidecar.append(
                A(
                    self.auth.param.messages["buttons"]["sign-up"],
                    _href=URL(f"{self.auth.route}/register"),
                    _class=self.auth.param.button_classes["sign-up"],
                    _role="button",
                )
            )
        if self.auth.allows("request_reset_password"):
            form.param.sidecar.append(
                A(
                    self.auth.param.messages["buttons"]["lost-password"],
                    _href=URL(f"{self.auth.route}/request_reset_password"),
                    _class=self.auth.param.button_classes["lost-password"],
                    _role="button",
                )
            )
        form.structure.insert(0, DIV(top_buttons["combined_div"]))
        return form

    def _reset_two_factor(self):
        self.auth.session["auth.2fa_user"] = None
        self.auth.session["auth.2fa_code"] = None
        self.auth.session["auth.2fa_tries_left"] = self.auth.param.two_factor_tries

    def two_factor(self):
        if (self.auth.param.two_factor_send is None) and (
            self.auth.param.two_factor_validate is None
        ):
            raise HTTP(404)

        user_id = self.auth.session.get("auth.2fa_user")
        next_url = self.auth.session.get("auth.2fa_next_url")

        if not user_id:
            redirect(URL("index"))

        user = self.auth.db.auth_user(user_id)
        code = self.auth.session.get("auth.2fa_code")
        if (not code) and (not self.auth.param.two_factor_send is None):
            # generate and send the code
            code = str(random.randint(100000, 999999))
            code = self.auth.param.two_factor_send(user, code)
            # store code in session
            self.auth.session["auth.2fa_code"] = code
            self.auth.session["auth.2fa_tries_left"] = self.auth.param.two_factor_tries
        elif self.auth.session.get("auth.2fa_tries_left") is None:
            self.auth.session["auth.2fa_tries_left"] = self.auth.param.two_factor_tries

        def two_factor_validate(form):
            # external validation outcome
            outcome = None
            if self.auth.param.two_factor_validate:
                outcome = self.auth.param.two_factor_validate(
                    user, form.vars["authentication_code"]
                )
            # outcome:
            #   True: external validation passed
            #   False: external validation failed
            #   None: external validation status unknown - check against the generated code
            if outcome == False or (
                (outcome is None) and (form.vars["authentication_code"] != code)
            ):
                form.errors["authentication_code"] = self.auth.param.messages["errors"][
                    "two_factor"
                ]

        form = Form(
            [
                Field(
                    "authentication_code",
                    label=self.auth.param.messages["labels"]["two_factor"],
                    required=True,
                ),
            ],
            validation=two_factor_validate,
            formstyle=self.auth.param.formstyle,
            form_name="auth_2fa",
            keep_values=True,
            hidden=dict(next_url=next_url),
        )

        if form.accepted:
            # reset the 2f session
            self._reset_two_factor()
            # store user in session
            self.auth.store_user_in_session(user["id"])
            # login user
            self._postprocessing("login", form, user)
            # redirect after login
            redirect(next_url)
        elif form.errors:
            # decrease the retries count
            self.auth.session["auth.2fa_tries_left"] -= 1
            # if 0 retries available, reset, and redirect to login
            if self.auth.session.get("auth.2fa_tries_left") < 1:
                self._reset_two_factor()
                self._set_flash(
                    self.auth.param.messages["errors"]["two_factor_max_tries"]
                )
                redirect(URL(f"{self.auth.route}/login", vars=dict(next=next_url)))
        return form

    def request_reset_password(self, model=False):
        """ "Request reset password form"""
        fields = [
            Field(
                "email",
                label=self.auth.param.messages["labels"].get("username_or_email"),
                requires=IS_NOT_EMPTY(),
            )
        ]

        button_name = self.auth.param.messages["buttons"]["request"]

        if model:
            additional_buttons = []
            if self.auth.allows("login"):
                additional_buttons.append(
                    dict(
                        label=self.auth.param.messages["buttons"]["sign-in"],
                        action="login",
                        href=URL(f"{self.auth.route}/api/login"),
                    )
                )

            if self.auth.allows("register"):
                additional_buttons.append(
                    dict(
                        label=self.auth.param.messages["buttons"]["sign-up"],
                        action="register",
                        href=URL(f"{self.auth.route}/api/register"),
                    )
                )

            return dict(
                public=True,
                hidden=False,
                fields=fields,
                href=URL(f"{self.auth.route}/api/request_reset_password"),
                submit_label=button_name,
                additional_buttons=additional_buttons,
            )

        extra_form_fields = self.auth.extra_form_fields.get(
            "request_reset_password", []
        )
        fields += extra_form_fields

        form = Form(
            fields,
            submit_value=button_name,
            formstyle=self.formstyle,
        )
        if form.accepted:
            email = form.vars.get("email", "")
            self.auth.request_reset_password(email, send=True, next="")
            self._set_flash("password-reset-link-sent")
            self._postprocessing("request_reset_password", form, None)

        if self.auth.allows("login"):
            form.param.sidecar.append(
                A(
                    self.auth.param.messages["buttons"]["sign-in"],
                    _href=URL(f"{self.auth.route}/login"),
                    _class=self.auth.param.button_classes["sign-in"],
                    _role="button",
                )
            )

        if self.auth.allows("register"):
            form.param.sidecar.append(
                A(
                    self.auth.param.messages["buttons"]["sign-up"],
                    _href=URL(f"{self.auth.route}/register"),
                    _class=self.auth.param.button_classes["sign-up"],
                    _role="button",
                )
            )
        return form

    def reset_password(self, model=False):
        """Process reset password form"""

        fields = [
            Field(
                "new_password",
                type="password",
                requires=self.auth.db.auth_user.password.requires,
                label=self.auth.param.messages["labels"].get("new_password"),
            ),
            Field(
                "new_password_again",
                type="password",
                requires=IS_EQUAL_TO(request.forms.get("new_password")),
                label=self.auth.param.messages["labels"].get("password_again"),
            ),
        ]

        button_name = self.auth.param.messages["buttons"]["submit"]

        if model:
            return dict(
                public=True,
                hidden=True,
                fields=fields,
                href=URL(f"{self.auth.route}/api/reset_password"),
                submit_label=button_name,
            )

        user = None
        token = request.query.get("token")
        if token:
            query = self.auth._query_from_token(token)
            user = self.auth.db(query).select().first()
            if not user:
                raise HTTP(404)
        form = Form(
            fields,
            formstyle=self.formstyle,
            submit_value=button_name,
        )
        self._process_change_password_form(form, user, False)
        if form.accepted:
            self._set_flash("password-changed")
            self._postprocessing("reset_password", form, user)
        return form

    def change_password(self, model=False):
        """Request change password form"""
        fields = [
            Field(
                "old_password",
                type="password",
                requires=IS_NOT_EMPTY(),
                label=self.auth.param.messages["labels"].get("old_password"),
            ),
            Field(
                "new_password",
                type="password",
                requires=self.auth.db.auth_user.password.requires,
                label=self.auth.param.messages["labels"].get("new_password"),
            ),
            Field(
                "new_password_again",
                type="password",
                requires=IS_EQUAL_TO(request.forms.get("new_password")),
                label=self.auth.param.messages["labels"].get("password_again"),
            ),
        ]

        button_name = self.auth.param.messages["buttons"]["submit"]

        if model:
            return dict(
                public=False,
                hidden=False,
                fields=fields,
                href=URL(f"{self.auth.route}/api/change_password"),
                submit_label=button_name,
            )

        form = Form(
            fields,
            formstyle=self.formstyle,
            submit_value=button_name,
        )
        user = self.auth.db.auth_user(self.auth.user_id)
        self._process_change_password_form(form, user, True)
        if form.accepted:
            self._set_flash("password-changed")
            self._postprocessing("change_password", form, user)
        return form

    def _process_change_password_form(self, form, user, check_old_password):
        """Process change password form"""
        if form.accepted:
            old_password = request.forms.get("old_password")
            new_password = request.forms.get("new_password")
            res = self.auth.change_password(
                user,
                new_password,
                old_password,
                check=True,
                check_old_password=check_old_password,
            )
            form.errors = res.get("errors", {})
            form.accepted = not form.errors
            if not form.accepted:
                form.vars.clear()

    def profile(self, model=False):
        """Edit profile form"""
        user = self.auth.db.auth_user(self.auth.user_id)
        if "username" in self.auth.db.auth_user.fields:
            self.auth.db.auth_user.username.writable = False
        else:
            self.auth.db.auth_user.email.writable = False
        if self.auth.param.exclude_extra_fields_in_profile:
            for field in self.auth.extra_auth_user_fields:
                if field.name in self.auth.param.exclude_extra_fields_in_profile:
                    field.writable = False
                    field.readable = False

        fields = [
            self.auth.db.auth_user[field]
            for field in self.auth.db.auth_user.fields
            if self.auth.db.auth_user[field].readable
        ]

        button_name = self.auth.param.messages["buttons"]["submit"]
        deletable = False

        if model:
            return dict(
                public=False,
                hidden=False,
                fields=fields,
                href=URL(f"{self.auth.route}/api/profile"),
                submit_label=button_name,
                deletable=deletable,
            )

        form = Form(
            self.auth.db.auth_user,
            user,
            formstyle=self.formstyle,
            deletable=deletable,
            submit_value=button_name,
        )
        if form.accepted:
            self._set_flash("profile-saved")
            self._postprocessing("profile", form, user)
        return form

    def logout(self, model=False):
        if model:
            return dict(
                public=False,
                hidden=False,
                noform=True,
                href=URL(f"{self.auth.route}/api/logout"),
            )

        """Process logout"""
        self.auth.session.clear()
        self._set_flash("user-logout")
        self._postprocessing("logout")
        return ""

    def verify_email(self, model=False):
        if model:
            return dict(
                public=True,
                hidden=True,
                noform=True,
                href=URL(f"{self.auth.route}/api/verify_email"),
            )

        """Process token in email verification"""
        token = request.query.get("token")
        verified = self.auth.verify_email(token)
        self._set_flash("email-verified" if verified else "link-expired")
        self._postprocessing("verify_email")

    def _set_flash(self, key):
        self.auth.flash.set(self.auth.param.messages["flash"].get(key, key))

    def _postprocessing(self, action, form=None, user=None):
        if action in self.auth.on_accept:
            self.auth.on_accept[action](form, user)
        if not form or form.accepted:
            redirect(self.auth.session.get(f"_next_{action}") or URL("index"))


class SimpleTokenPlugin:
    """
    A simble token bearer handler for auth.token_plugins

    Usage:
      1) auth.token_plugins.append(SimpleTokenPlugin(auth))
      2) Use a grid or form to create a db.auth_simple_token record
      3) Use with curl -H "Authorization: Bearer {token}"

    This kind of token needs database access to be verified
    It can therefore be expired server side.

    This is the recommended kind of token.

    You can create a management interface for API tokens with


    @action("tokens/<path:path>")
    @action.uses("generic.html", auth.user)
    def _(path):
        db.auth_simple_token.user_id.default = auth.user_id
        grid = Grid(path, db.auth_simple_token.user_id==auth.user_id, create=True, deletable=True)
        return dict(grid=grid)
    """

    def __init__(self, auth, table=None):
        self.auth = auth
        if table:
            self.table = table
        else:
            self.table = auth.db.define_table(
                "auth_simple_token",
                Field("token", default=uuid.uuid4, unique=True, writable=False),
                Field(
                    "user_id", "reference auth_user", default=auth.user_id, writable=False
                ),
                Field("description"),
                Field("expiration_date", "datetime"),
                auth.signature,
            )

    def get_user(self):
        authorization = request.headers.get("authorization")
        if authorization and authorization.startswith("Bearer "):
            db = self.auth.db
            token = authorization[6:].strip()
            row = self.table(token=token)
            if row and row.expiration_date.isoformat() > utcnow().isoformat():
                user = db.auth_user(row.user_id)
                return user.as_dict()
        return None


class JwtTokenPlugin:
    """
    A simble token bearer handler for auth.token_plugins

    Usage:
      1) myplugin = JwtTokenPlugin(auth)
      2) auth.token_plugins.append(myplugin)
      3) Use token = myplugin.make(user, expiration) to make tokens
      4) Use with curl -H "Authorization: Bearer {token}"

    This kind of token does not need database access to be verified.
    It cannot therefore be expired server side and any server
    side change in the user info is not reflected in the info
    stored in the token.

    This token should only be used when the API needs to be fast
    and it is desirable to aboid any database access.
    Expiration should not be too far in the future.

    When making a token you can put anything you want in user,
    but there must be a user["id"] for authentication to succeed.
    """

    def __init__(self, auth, secret=None, algorithms=["HS256", "RS256"]):
        self.auth = auth
        self.secret = secret or self.auth.session.SECRET
        self.algorithms = algorithms

    def make(self, user, expiration):
        if not isinstance(user, dict):
            user = user.as_dict()
        if not isinstance(expiration, str):
            expiration = expiration.isoformat()
        data = {"user": user, "expiration": expiration}
        token = jwt.encode(data, self.secret, algorithm=self.algorithms[0])
        return token

    def get_user(self):
        authorization = request.headers.get("authorization")
        if authorization and authorization.startswith("Bearer "):
            token = authorization[6:].strip()
            try:
                data = jwt.decode(token, self.secret, algorithms=self.algorithms)
            except Exception:
                return None
            expiration = data.get("expiration")
            if expiration and expiration > utcnow().isoformat():
                user = data.get("user")
                return user
        return None
