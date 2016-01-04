#!/bin/python
# -*- coding: utf-8 -*-

"""
| This file is part of the web2py Web Framework
| Copyrighted by Massimo Di Pierro <mdipierro@cs.depaul.edu>
| License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)

Auth, Mail, PluginManager and various utilities
------------------------------------------------
"""

import base64
try:
    import cPickle as pickle
except:
    import pickle
import datetime
import sys
import os
import re
import time
import urllib
import hmac
import hashlib
import json

from gluon.serializers import json_parser
from gluon.storage import Storage, Settings, Messages
from gluon.utils import web2py_uuid
from gluon.fileutils import read_file, check_credentials
from gluon import *
from pydal.objects import Row, Set, Query
from gluon.mail import Mail
import gluon.serializers as serializers

Table = DAL.Table
Field = DAL.Field

try:
    # try stdlib (Python 2.6)
    import json as json_parser
except ImportError:
    try:
        # try external module
        import simplejson as json_parser
    except:
        # fallback to pure-Python module
        import gluon.contrib.simplejson as json_parser

__all__ = ['Auth']

DEFAULT = lambda: None


def getarg(position, default=None):
    args = current.request.args
    if position < 0 and len(args) >= -position:
        return args[position]
    elif position >= 0 and len(args) > position:
        return args[position]
    else:
        return default


def callback(actions, form, tablename=None):
    if actions:
        if tablename and isinstance(actions, dict):
            actions = actions.get(tablename, [])
        if not isinstance(actions, (list, tuple)):
            actions = [actions]
        [action(form) for action in actions]


def validators(*a):
    b = []
    for item in a:
        if isinstance(item, (list, tuple)):
            b = b + list(item)
        else:
            b.append(item)
    return b


def call_or_redirect(f, *args):
    if callable(f):
        redirect(f(*args))
    else:
        redirect(f)


def replace_id(url, form):
    if url:
        url = url.replace('[id]', str(form.vars.id))
        if url[0] == '/' or url[:4] == 'http':
            return url
    return URL(url)


class AuthJWT(object):

    """
    If left externally, this needs the usual "singleton" approach.
    Given I (we) don't know if to include in auth yet, let's stick to basics.

    Args:
     - secret_key: the secret. Without salting, an attacker knowing this can impersonate
                   any user
     - algorithm : uses as they are in the JWT specs, HS256, HS384 or HS512 basically means
                   signing with HMAC with a 256, 284 or 512bit hash
     - verify_expiration : verifies the expiration checking the exp claim
     - leeway: allow n seconds of skew when checking for token expiration
     - expiration : how many seconds a token may be valid
     - allow_refresh: enable the machinery to get a refreshed token passing a not-already-expired
                      token
     - refresh_expiration_delta: to avoid continous refresh of the token
     - header_prefix : self-explanatory. "JWT" and "Bearer" seems to be the emerging standards
     - jwt_add_header: a dict holding additional mappings to the header. by default only alg and typ are filled
     - user_param: the name of the parameter holding the username when requesting a token. Can be useful, e.g, for
                   email-based authentication, with "email" as a parameter
     - pass_param: same as above, but for the password
     - realm: self-explanatory
     - salt: can be static or a function that takes the payload as an argument.
             Example:
             def mysalt(payload):
                return payload['hmac_key'].split('-')[0]
     - additional_payload: can be a dict to merge with the payload or a function that takes
                           the payload as input and returns the modified payload
                           Example:
                           def myadditional_payload(payload):
                               payload['my_name_is'] = 'bond,james bond'
                               return payload
     - before_authorization: can be a callable that takes the deserialized token (a dict) as input.
                             Gets called right after signature verification but before the actual
                             authorization takes place. You can raise with HTTP a proper error message
                             Example:
                             def mybefore_authorization(tokend):
                                 if not tokend['my_name_is'] == 'bond,james bond':
                                     raise HTTP(400, u'Invalid JWT my_name_is claim')
     - max_header_length: check max length to avoid load()ing unusually large tokens (could mean crafted, e.g. in a DDoS.)

    Basic Usage:
    in models (or the controller needing it)

        myjwt = AuthJWT(auth, secret_key='secret')

    in the controller issuing tokens

        def login_and_take_token():
            return myjwt.jwt_token_manager()

    A call then to /app/controller/login_and_take_token/auth with username and password returns the token
    A call to /app/controller/login_and_take_token/refresh with the original token returns the refreshed token

    To protect a function with JWT

        @myjwt.allows_jwt()
        @auth.requires_login()
        def protected():
            return '%s$%s' % (request.now, auth.user_id)

    """

    def __init__(self, 
                 auth,
                 secret_key,
                 algorithm='HS256',
                 verify_expiration=True,
                 leeway=30,
                 expiration=60 * 5,
                 allow_refresh=True,
                 refresh_expiration_delta=60 * 60,
                 header_prefix='Bearer',
                 jwt_add_header=None,
                 user_param='username',
                 pass_param='password',
                 realm='Login required',
                 salt=None,
                 additional_payload=None,
                 before_authorization=None,
                 max_header_length=4*1024,
                 ):
        self.secret_key = secret_key
        self.auth = auth
        self.algorithm = algorithm
        if self.algorithm not in ('HS256', 'HS384', 'HS512'):
            raise NotImplementedError('Algoritm %s not allowed' % algorithm)
        self.verify_expiration = verify_expiration
        self.leeway = leeway
        self.expiration = expiration
        self.allow_refresh = allow_refresh
        self.refresh_expiration_delta = refresh_expiration_delta
        self.header_prefix = header_prefix
        self.jwt_add_header = jwt_add_header or {}
        base_header = {'alg': self.algorithm, 'typ': 'JWT'}
        for k, v in self.jwt_add_header.iteritems():
            base_header[k] = v
        self.cached_b64h = self.jwt_b64e(json_parser.dumps(base_header))
        digestmod_mapping = {
            'HS256': hashlib.sha256,
            'HS384': hashlib.sha384,
            'HS512': hashlib.sha512
        }
        self.digestmod = digestmod_mapping[algorithm]
        self.user_param = user_param
        self.pass_param = pass_param
        self.realm = realm
        self.salt = salt
        self.additional_payload = additional_payload
        self.before_authorization = before_authorization
        self.max_header_length = max_header_length

    @staticmethod
    def jwt_b64e(string):
        if isinstance(string, unicode):
            string = string.encode('uft-8', 'strict')
        return base64.urlsafe_b64encode(string).strip(b'=')

    @staticmethod
    def jwt_b64d(string):
        """base64 decodes a single bytestring (and is tolerant to getting
        called with a unicode string).
        The result is also a bytestring.
        """
        if isinstance(string, unicode):
            string = string.encode('ascii', 'ignore')
        return base64.urlsafe_b64decode(string + '=' * (-len(string) % 4))

    def generate_token(self, payload):
        secret = self.secret_key
        if self.salt:
            if callable(self.salt):
                secret = "%s$%s" % (secret, self.salt(payload))
            else:
                secret = "%s$%s" % (secret, self.salt)
            if isinstance(secret, unicode):
                secret = secret.encode('ascii', 'ignore')
        b64h = self.cached_b64h
        b64p = self.jwt_b64e(json_parser.dumps(payload))
        jbody = b64h + '.' + b64p
        mauth = hmac.new(key=secret, msg=jbody, digestmod=self.digestmod)
        jsign = self.jwt_b64e(mauth.digest())
        return jbody + '.' + jsign

    def verify_signature(self, body, signature, secret):
        mauth = hmac.new(key=secret, msg=body, digestmod=self.digestmod)
        return hmac.compare_digest(self.jwt_b64e(mauth.digest()), signature)

    def load_token(self, token):
        if isinstance(token, unicode):
            token = token.encode('utf-8', 'strict')
        body, sig = token.rsplit('.', 1)
        b64h, b64b = body.split('.', 1)
        if b64h != self.cached_b64h:
            # header not the same
            raise HTTP(400, u'Invalid JWT Header')
        secret = self.secret_key
        tokend = json_parser.loads(self.jwt_b64d(b64b))
        if self.salt:
            if callable(self.salt):
                secret = "%s$%s" % (secret, self.salt(tokend))
            else:
                secret = "%s$%s" % (secret, self.salt)
            if isinstance(secret, unicode):
                secret = secret.encode('ascii', 'ignore')
        if not self.verify_signature(body, sig, secret):
            # signature verification failed
            raise HTTP(400, u'Token signature is invalid')
        if self.verify_expiration:
            now = time.mktime(datetime.datetime.utcnow().timetuple())
            if tokend['exp'] + self.leeway < now:
                raise HTTP(400, u'Token is expired')
        if callable(self.before_authorization):
            self.before_authorization(tokend)
        return tokend

    def serialize_auth_session(self, session_auth):
        """
        As bad as it sounds, as long as this is rarely used (vs using the token)
        this is the faster method, even if we ditch session in jwt_token_manager().
        We (mis)use the heavy default auth mechanism to avoid any further computation,
        while sticking to a somewhat-stable Auth API.
        """
        now = time.mktime(datetime.datetime.utcnow().timetuple())
        expires = now + self.expiration
        payload = dict(
            hmac_key=session_auth['hmac_key'],
            user_groups=session_auth['user_groups'],
            user=session_auth['user'].as_dict(),
            iat=now,
            exp=expires
        )
        return payload

    def refresh_token(self, orig_payload):
        now = time.mktime(datetime.datetime.utcnow().timetuple())
        if self.verify_expiration:
            orig_exp = orig_payload['exp']
            if orig_exp + self.leeway < now:
                # token already expired, can't be used for refresh
                raise HTTP(400, u'Token already expired')
        orig_iat = orig_payload.get('orig_iat') or orig_payload['iat']
        if orig_iat + self.refresh_expiration_delta < now:
            # refreshed too long ago
            raise HTTP(400, u'Token issued too long ago')
        expires = now + self.refresh_expiration_delta
        orig_payload.update(
            orig_iat=orig_iat,
            iat=now,
            exp=expires,
            hmac_key=web2py_uuid()
        )
        self.alter_payload(orig_payload)
        return orig_payload

    def alter_payload(self, payload):
        if self.additional_payload:
            if callable(self.additional_payload):
                payload = self.additional_payload(payload)
            elif isinstance(self.additional_payload, dict):
                payload.update(self.additional_payload)
        return payload

    def jwt_token_manager(self):
        """
        The part that issues (and refreshes) tokens.
        Used in a controller, given myjwt is the istantiated class, as

            def api_auth():
                return myjwt.jwt_token_manager()

        Then, a call to /app/c/api_auth/auth with username and password
        returns a token, while /app/c/api_auth/refresh with the current token
        issues another token
        """
        request = current.request
        response = current.response
        session = current.session
        # forget and unlock response
        if request.vars.token:
            if not self.allow_refresh:
                raise HTTP(403, u'Refreshing token is not allowed')
            token = request.vars.token
            tokend = self.load_token(token)
            # verification can fail here
            refreshed = self.refresh_token(tokend)
            ret = {'token':self.generate_token(refreshed)}
        elif self.user_param in request.vars and self.pass_param in request.vars:
            session.forget(response)
            username = request.vars[self.user_param]
            password = request.vars[self.pass_param]
            valid_user = self.auth.login_bare(username, password)
            if valid_user:
                payload = self.serialize_auth_session(current.session.auth)
                self.alter_payload(payload)
                ret = {'token':self.generate_token(payload)}
            else:
                raise HTTP(
                    401, u'Not Authorized', 
                    **{'WWW-Authenticate': u'JWT realm="%s"' % self.realm})
        else:
            raise HTTP(400, u'Must pass token for refresh or username and password for login')
        response.headers['content-type'] = 'application/json'
        return json.dumps(ret)

    def inject_token(self, tokend):
        """
        The real deal, not touching the db but still logging-in the user
        """
        self.auth.user = Storage(tokend['user'])
        self.auth.user_groups = tokend['user_groups']
        self.auth.hmac_key = tokend['hmac_key']

    def allows_jwt(self, otherwise=None):
        """
        The validator that checks for the header or the
        _token var
        """
        request = current.request
        token_in_header = request.env.http_authorization
        if token_in_header:
            parts = token_in_header.split()
            if parts[0].lower() != self.header_prefix.lower():
                raise HTTP(400, u'Invalid JWT header')
            elif len(parts) == 1:
                raise HTTP(400, u'Invalid JWT header, missing token')
            elif len(parts) > 2:
                raise HTTP(400, 'Invalid JWT header, token contains spaces')
            token = parts[1]
        else:
            token = request.vars._token
        if token and len(token) < self.max_header_length:
            tokend = self.load_token(token)
            self.inject_token(tokend)
        return self.auth.requires(True, otherwise=otherwise)


class Auth(object):

    default_settings = dict(
        hideerror=False,
        password_min_length=4,
        cas_maps=None,
        reset_password_requires_verification=False,
        registration_requires_verification=False,
        registration_requires_approval=False,
        bulk_register_enabled=False,
        login_after_registration=False,
        login_after_password_change=True,
        alternate_requires_registration=False,
        create_user_groups="user_%(id)s",
        everybody_group_id=None,
        manager_actions={},
        auth_manager_role=None,
        two_factor_authentication_group = None,
        auth_two_factor_enabled = False,
        auth_two_factor_tries_left = 3,
        login_captcha=None,
        register_captcha=None,
        pre_registration_div=None,
        retrieve_username_captcha=None,
        retrieve_password_captcha=None,
        captcha=None,
        prevent_open_redirect_attacks=True,
        prevent_password_reset_attacks=True,
        expiration=3600,            # one hour
        long_expiration=3600 * 30 * 24,  # one month
        remember_me_form=True,
        allow_basic_login=False,
        allow_basic_login_only=False,
        on_failed_authentication=lambda x: redirect(x),
        formstyle=None,
        label_separator=None,
        logging_enabled = True,
        allow_delete_accounts=False,
        password_field='password',
        table_user_name='auth_user',
        table_group_name='auth_group',
        table_membership_name='auth_membership',
        table_permission_name='auth_permission',
        table_event_name='auth_event',
        table_cas_name='auth_cas',
        table_token_name='auth_token',
        table_user=None,
        table_group=None,
        table_membership=None,
        table_permission=None,
        table_event=None,
        table_cas=None,
        showid=False,
        use_username=False,
        login_email_validate=True,
        login_userfield=None,
        multi_login=False,
        logout_onlogout=None,
        register_fields=None,
        register_verify_password=True,
        profile_fields=None,
        email_case_sensitive=True,
        username_case_sensitive=True,
        update_fields=['email'],
        ondelete="CASCADE",
        client_side=True,
        renew_session_onlogin=True,
        renew_session_onlogout=True,
        keep_session_onlogin=True,
        keep_session_onlogout=False)
        # ## these are messages that can be customized
    default_messages = dict(
        login_button='Log In',
        register_button='Sign Up',
        password_reset_button='Request reset password',
        password_change_button='Change password',
        profile_save_button='Apply changes',
        submit_button='Submit',
        verify_password='Verify Password',
        delete_label='Check to delete',
        function_disabled='Function disabled',
        access_denied='Insufficient privileges',
        registration_verifying='Registration needs verification',
        registration_pending='Registration is pending approval',
        email_taken='This email already has an account',
        invalid_username='Invalid username',
        username_taken='Username already taken',
        login_disabled='Login disabled by administrator',
        logged_in='Logged in',
        email_sent='Email sent',
        unable_to_send_email='Unable to send email',
        email_verified='Email verified',
        logged_out='Logged out',
        registration_successful='Registration successful',
        invalid_email='Invalid email',
        unable_send_email='Unable to send email',
        invalid_login='Invalid login',
        invalid_user='Invalid user',
        invalid_password='Invalid password',
        invalid_two_factor_code = 'Incorrect code. {0} more attempt(s) remaining.',
        is_empty="Cannot be empty",
        mismatched_password="Password fields don't match",
        verify_email='Welcome %(username)s! Click on the link %(link)s to verify your email',
        verify_email_subject='Email verification',
        username_sent='Your username was emailed to you',
        new_password_sent='A new password was emailed to you',
        password_changed='Password changed',
        retrieve_username='Your username is: %(username)s',
        retrieve_username_subject='Username retrieve',
        retrieve_password='Your password is: %(password)s',
        retrieve_password_subject='Password retrieve',
        reset_password='Click on the link %(link)s to reset your password',
        reset_password_subject='Password reset',
        bulk_invite_subject='Invitation to join %(site)s',
        retrieve_two_factor_code='Your temporary login code is {0}',
        retrieve_two_factor_code_subject='Two-step Login Authentication Code',
        bulk_invite_body='You have been invited to join %(site)s, click %(link)s to complete the process',
        invalid_reset_password='Invalid reset password',
        profile_updated='Profile updated',
        new_password='New password',
        old_password='Old password',
        group_description='Group uniquely assigned to user %(id)s',
        register_log='User %(id)s Registered',
        login_log='User %(id)s Logged-in',
        login_failed_log=None,
        logout_log='User %(id)s Logged-out',
        profile_log='User %(id)s Profile updated',
        verify_email_log='User %(id)s Verification email sent',
        retrieve_username_log='User %(id)s Username retrieved',
        retrieve_password_log='User %(id)s Password retrieved',
        reset_password_log='User %(id)s Password reset',
        change_password_log='User %(id)s Password changed',
        add_group_log='Group %(group_id)s created',
        del_group_log='Group %(group_id)s deleted',
        add_membership_log=None,
        del_membership_log=None,
        has_membership_log=None,
        add_permission_log=None,
        del_permission_log=None,
        has_permission_log=None,
        impersonate_log='User %(id)s is impersonating %(other_id)s',
        label_first_name='First name',
        label_last_name='Last name',
        label_username='Username',
        label_email='E-mail',
        label_password='Password',
        label_registration_key='Registration key',
        label_reset_password_key='Reset Password key',
        label_registration_id='Registration identifier',
        label_role='Role',
        label_description='Description',
        label_user_id='User ID',
        label_group_id='Group ID',
        label_name='Name',
        label_table_name='Object or table name',
        label_record_id='Record ID',
        label_time_stamp='Timestamp',
        label_client_ip='Client IP',
        label_origin='Origin',
        label_remember_me="Remember me (for 30 days)",
        label_two_factor='Authentication code',
        two_factor_comment = 'This code was emailed to you and is required for login.',
        verify_password_comment='please input your password again',
    )

    """
    Class for authentication, authorization, role based access control.

    Includes:

    - registration and profile
    - login and logout
    - username and password retrieval
    - event logging
    - role creation and assignment
    - user defined group/role based permission

    Args:

        environment: is there for legacy but unused (awful)
        db: has to be the database where to create tables for authentication
        mailer: `Mail(...)` or None (no mailer) or True (make a mailer)
        hmac_key: can be a hmac_key or hmac_key=Auth.get_or_create_key()
        controller: (where is the user action?)
        cas_provider: (delegate authentication to the URL, CAS2)

    Authentication Example::

        from gluon.contrib.utils import *
        mail=Mail()
        mail.settings.server='smtp.gmail.com:587'
        mail.settings.sender='you@somewhere.com'
        mail.settings.login='username:password'
        auth=Auth(db)
        auth.settings.mailer=mail
        # auth.settings....=...
        auth.define_tables()
        def authentication():
            return dict(form=auth())

    Exposes:

    - `http://.../{application}/{controller}/authentication/login`
    - `http://.../{application}/{controller}/authentication/logout`
    - `http://.../{application}/{controller}/authentication/register`
    - `http://.../{application}/{controller}/authentication/verify_email`
    - `http://.../{application}/{controller}/authentication/retrieve_username`
    - `http://.../{application}/{controller}/authentication/retrieve_password`
    - `http://.../{application}/{controller}/authentication/reset_password`
    - `http://.../{application}/{controller}/authentication/profile`
    - `http://.../{application}/{controller}/authentication/change_password`

    On registration a group with role=new_user.id is created
    and user is given membership of this group.

    You can create a group with::

        group_id=auth.add_group('Manager', 'can access the manage action')
        auth.add_permission(group_id, 'access to manage')

    Here "access to manage" is just a user defined string.
    You can give access to a user::

        auth.add_membership(group_id, user_id)

    If user id is omitted, the logged in user is assumed

    Then you can decorate any action::

        @auth.requires_permission('access to manage')
        def manage():
            return dict()

    You can restrict a permission to a specific table::

        auth.add_permission(group_id, 'edit', db.sometable)
        @auth.requires_permission('edit', db.sometable)

    Or to a specific record::

        auth.add_permission(group_id, 'edit', db.sometable, 45)
        @auth.requires_permission('edit', db.sometable, 45)

    If authorization is not granted calls::

        auth.settings.on_failed_authorization

    Other options::

        auth.settings.mailer=None
        auth.settings.expiration=3600 # seconds

        ...

        ### these are messages that can be customized
        ...

    """

    @staticmethod
    def get_or_create_key(filename=None, alg='sha512'):
        request = current.request
        if not filename:
            filename = os.path.join(request.folder, 'private', 'auth.key')
        if os.path.exists(filename):
            key = open(filename, 'r').read().strip()
        else:
            key = alg + ':' + web2py_uuid()
            open(filename, 'w').write(key)
        return key

    def url(self, f=None, args=None, vars=None, scheme=False):
        if args is None:
            args = []
        if vars is None:
            vars = {}
        return URL(c=self.settings.controller,
                   f=f, args=args, vars=vars, scheme=scheme)

    def here(self):
        return URL(args=current.request.args, vars=current.request.get_vars)

    def __init__(self, environment=None, db=None, mailer=True,
                 hmac_key=None, controller='default', function='user',
                 cas_provider=None, signature=True, secure=False,
                 csrf_prevention=True, propagate_extension=None,
                 url_index=None, jwt=None):

        ## next two lines for backward compatibility
        if not db and environment and isinstance(environment, DAL):
            db = environment
        self.db = db
        self.environment = current
        self.csrf_prevention = csrf_prevention
        request = current.request
        session = current.session
        auth = session.auth
        self.user_groups = auth and auth.user_groups or {}
        if secure:
            request.requires_https()
        now = request.now
        # if we have auth info
        #    if not expired it, used it
        #    if expired, clear the session
        # else, only clear auth info in the session
        if auth:
            delta = datetime.timedelta(days=0, seconds=auth.expiration)
            if auth.last_visit and auth.last_visit + delta > now:
                self.user = auth.user
                # this is a trick to speed up sessions to avoid many writes
                if (now - auth.last_visit).seconds > (auth.expiration / 10):
                    auth.last_visit = request.now
            else:
                self.user = None
                if session.auth:
                    del session.auth
                session.renew(clear_session=True)
        else:
            self.user = None
            if session.auth:
                del session.auth
        # ## what happens after login?

        url_index = url_index or URL(controller, 'index')
        url_login = URL(controller, function, args='login',
                        extension = propagate_extension)
        # ## what happens after registration?

        settings = self.settings = Settings()
        settings.update(Auth.default_settings)
        settings.update(
            cas_domains=[request.env.http_host],
            enable_tokens=False,
            cas_provider=cas_provider,
            cas_actions=dict(login='login',
                             validate='validate',
                             servicevalidate='serviceValidate',
                             proxyvalidate='proxyValidate',
                             logout='logout'),
            extra_fields={},
            actions_disabled=[],
            controller=controller,
            function=function,
            login_url=url_login,
            logged_url=URL(controller, function, args='profile'),
            download_url=URL(controller, 'download'),
            mailer=(mailer is True) and Mail() or mailer,
            on_failed_authorization=URL(controller, function, args='not_authorized'),
            login_next=url_index,
            login_onvalidation=[],
            login_onaccept=[],
            login_onfail=[],
            login_methods=[self],
            login_form=self,
            logout_next=url_index,
            logout_onlogout=None,
            register_next=url_index,
            register_onvalidation=[],
            register_onaccept=[],
            verify_email_next=url_login,
            verify_email_onaccept=[],
            profile_next=url_index,
            profile_onvalidation=[],
            profile_onaccept=[],
            retrieve_username_next=url_index,
            retrieve_password_next=url_index,
            request_reset_password_next=url_login,
            reset_password_next=url_index,
            change_password_next=url_index,
            change_password_onvalidation=[],
            change_password_onaccept=[],
            retrieve_password_onvalidation=[],
            request_reset_password_onvalidation=[],
            request_reset_password_onaccept=[],
            reset_password_onvalidation=[],
            reset_password_onaccept=[],
            hmac_key=hmac_key,
            formstyle=None, #current.response.formstyle, # FIX THIS
            label_separator=None, #current.response.form_label_separator,
            two_factor_methods = [],
            two_factor_onvalidation = [],
        )
        settings.lock_keys = True
        # ## these are messages that can be customized
        messages = self.messages = Messages(current.T)
        messages.update(Auth.default_messages)
        messages.update(ajax_failed_authentication=
                        DIV(H4('NOT AUTHORIZED'),
                            'Please ',
                            A('login',
                              _href=self.settings.login_url +
                                    ('?_next=' + urllib.quote(current.request.env.http_web2py_component_location))
                              if current.request.env.http_web2py_component_location else ''),
                            ' to view this content.',
                            _class='not-authorized alert alert-block'))
        messages.lock_keys = True

        # for "remember me" option
        response = current.response
        if auth and auth.remember_me:
            # when user wants to be logged in for longer
            response.session_cookie_expires = auth.expiration
        if signature:
            self.define_signature()
        else:
            self.signature = None
        
        self.jwt_handler = jwt and AuthJWT(self, **jwt)

    def get_vars_next(self):
        next = current.request.vars._next
        if isinstance(next, (list, tuple)):
            next = next[0]
        if next and self.settings.prevent_open_redirect_attacks:
            # Prevent an attacker from adding an arbitrary url after the
            # _next variable in the request.
            items = next.split('/')
            if '//' in next and items[2] != current.request.env.http_host:
                next = None
        return next

    def _get_user_id(self):
        """accessor for auth.user_id"""
        return self.user and self.user.id or None

    user_id = property(_get_user_id, doc="user.id or None")

    def table_user(self):
        return self.db[self.settings.table_user_name]

    def table_group(self):
        return self.db[self.settings.table_group_name]

    def table_membership(self):
        return self.db[self.settings.table_membership_name]

    def table_permission(self):
        return self.db[self.settings.table_permission_name]

    def table_event(self):
        return self.db[self.settings.table_event_name]

    def table_cas(self):
        return self.db[self.settings.table_cas_name]

    def table_token(self):
        return self.db[self.settings.table_token_name]

    def _HTTP(self, *a, **b):
        """
        only used in lambda: self._HTTP(404)
        """

        raise HTTP(*a, **b)

    def __call__(self):
        """
        Example:
            Use as::

                def authentication():
                    return dict(form=auth())

        """

        request = current.request
        args = request.args

        if not args:
            redirect(self.url(args='login', vars=request.vars))
        elif args[0] in self.settings.actions_disabled:
            raise HTTP(404)
        if args[0] in ('login', 'logout', 'register', 'verify_email',
                       'retrieve_username', 'retrieve_password',
                       'reset_password', 'request_reset_password',
                       'change_password', 'profile', 'groups',
                       'impersonate', 'not_authorized', 'confirm_registration',
                       'bulk_register','manage_tokens','jwt'):
            if len(request.args) >= 2 and args[0] == 'impersonate':
                return getattr(self, args[0])(request.args[1])
            else:
                return getattr(self, args[0])()
        elif args[0] == 'cas' and not self.settings.cas_provider and len(args)>1:
            if args(1) == self.settings.cas_actions['login']:
                return self.cas_login(version=2)
            elif args(1) == self.settings.cas_actions['validate']:
                return self.cas_validate(version=1)
            elif args(1) == self.settings.cas_actions['servicevalidate']:
                return self.cas_validate(version=2, proxy=False)
            elif args(1) == self.settings.cas_actions['proxyvalidate']:
                return self.cas_validate(version=2, proxy=True)
            elif args(1) == self.settings.cas_actions['logout']:
                return self.logout(next=request.vars.service or DEFAULT)        
        else:
            raise HTTP(404)

    def __get_migrate(self, tablename, migrate=True):

        if type(migrate).__name__ == 'str':
            return (migrate + tablename + '.table')
        elif migrate == False:
            return False
        else:
            return True

    def enable_record_versioning(self,
                                 tables,
                                 archive_db=None,
                                 archive_names='%(tablename)s_archive',
                                 current_record='current_record',
                                 current_record_label=None):
        """
        Used to enable full record versioning (including auth tables)::

            auth = Auth(db)
            auth.define_tables(signature=True)
            # define our own tables
            db.define_table('mything',Field('name'),auth.signature)
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
        current_record_label = current_record_label or current.T(
            current_record.replace('_', ' ').title())
        for table in tables:
            fieldnames = table.fields()
            if ('id' in fieldnames and
                'modified_on' in fieldnames and
                not current_record in fieldnames):
                table._enable_record_versioning(
                    archive_db=archive_db,
                    archive_name=archive_names,
                    current_record=current_record,
                    current_record_label=current_record_label)

    def define_signature(self):
        db = self.db
        settings = self.settings
        request = current.request
        T = current.T
        reference_user = 'reference %s' % settings.table_user_name

        def lazy_user(auth=self):
            return auth.user_id

        def represent(id, record=None, s=settings):
            try:
                user = s.table_user(id)
                return '%s %s' % (user.get("first_name", user.get("email")),
                                  user.get("last_name", ''))
            except:
                return id
        ondelete = self.settings.ondelete
        self.signature = Table(
            self.db, 'auth_signature',
            Field('is_active', 'boolean',
                  default=True,
                  readable=False, writable=False,
                  label=T('Is Active')),
            Field('created_on', 'datetime',
                  default=request.now,
                  writable=False, readable=False,
                  label=T('Created On')),
            Field('created_by',
                  reference_user,
                  default=lazy_user, represent=represent,
                  writable=False, readable=False,
                  label=T('Created By'), ondelete=ondelete),
            Field('modified_on', 'datetime',
                  update=request.now, default=request.now,
                  writable=False, readable=False,
                  label=T('Modified On')),
            Field('modified_by',
                  reference_user, represent=represent,
                  default=lazy_user, update=lazy_user,
                  writable=False, readable=False,
                  label=T('Modified By'),  ondelete=ondelete))

    def define_tables(self, username=None, signature=None, enable_tokens=False,
                      migrate=None, fake_migrate=None):
        """
        To be called unless tables are defined manually

        Examples:
            Use as::

                # defines all needed tables and table files
                # 'myprefix_auth_user.table', ...
                auth.define_tables(migrate='myprefix_')

                # defines all needed tables without migration/table files
                auth.define_tables(migrate=False)

        """

        db = self.db
        if migrate is None:
            migrate = db._migrate
        if fake_migrate is None:
            fake_migrate = db._fake_migrate
        settings = self.settings
        if username is None:
            username = settings.use_username
        else:
            settings.use_username = username
        settings.enable_tokens = enable_tokens
        if not self.signature:
            self.define_signature()
        if signature:
            signature_list = [self.signature]
        elif not signature:
            signature_list = []
        elif isinstance(signature, Table):
            signature_list = [signature]
        else:
            signature_list = signature
        is_not_empty = IS_NOT_EMPTY(error_message=self.messages.is_empty)
        is_crypted = CRYPT(key=settings.hmac_key,
                           min_length=settings.password_min_length)
        is_unique_email = [
            IS_EMAIL(error_message=self.messages.invalid_email),
            IS_NOT_IN_DB(db, '%s.email' % settings.table_user_name,
                         error_message=self.messages.email_taken)]
        if not settings.email_case_sensitive:
            is_unique_email.insert(1, IS_LOWER())
        if settings.table_user_name not in db.tables:
            passfield = settings.password_field
            extra_fields = settings.extra_fields.get(
                settings.table_user_name, []) + signature_list
            if username or settings.cas_provider:
                is_unique_username = \
                    [IS_MATCH('[\w\.\-]+', strict=True,
                              error_message=self.messages.invalid_username),
                     IS_NOT_IN_DB(db, '%s.username' % settings.table_user_name,
                                  error_message=self.messages.username_taken)]
                if not settings.username_case_sensitive:
                    is_unique_username.insert(1, IS_LOWER())
                db.define_table(
                    settings.table_user_name,
                    Field('first_name', length=128, default='',
                          label=self.messages.label_first_name,
                          requires=is_not_empty),
                    Field('last_name', length=128, default='',
                          label=self.messages.label_last_name,
                          requires=is_not_empty),
                    Field('email', length=512, default='',
                          label=self.messages.label_email,
                          requires=is_unique_email),
                    Field('username', length=128, default='',
                          label=self.messages.label_username,
                          requires=is_unique_username),
                    Field(passfield, 'password', length=512,
                          readable=False, label=self.messages.label_password,
                          requires=[is_crypted]),
                    Field('registration_key', length=512,
                          writable=False, readable=False, default='',
                          label=self.messages.label_registration_key),
                    Field('reset_password_key', length=512,
                          writable=False, readable=False, default='',
                          label=self.messages.label_reset_password_key),
                    Field('registration_id', length=512,
                          writable=False, readable=False, default='',
                          label=self.messages.label_registration_id),
                    *extra_fields,
                    **dict(
                        migrate=self.__get_migrate(settings.table_user_name,
                                                   migrate),
                        fake_migrate=fake_migrate,
                        format='%(username)s'))
            else:
                db.define_table(
                    settings.table_user_name,
                    Field('first_name', length=128, default='',
                          label=self.messages.label_first_name,
                          requires=is_not_empty),
                    Field('last_name', length=128, default='',
                          label=self.messages.label_last_name,
                          requires=is_not_empty),
                    Field('email', length=512, default='',
                          label=self.messages.label_email,
                          requires=is_unique_email),
                    Field(passfield, 'password', length=512,
                          readable=False, label=self.messages.label_password,
                          requires=[is_crypted]),
                    Field('registration_key', length=512,
                          writable=False, readable=False, default='',
                          label=self.messages.label_registration_key),
                    Field('reset_password_key', length=512,
                          writable=False, readable=False, default='',
                          label=self.messages.label_reset_password_key),
                    Field('registration_id', length=512,
                          writable=False, readable=False, default='',
                          label=self.messages.label_registration_id),
                    *extra_fields,
                    **dict(
                        migrate=self.__get_migrate(settings.table_user_name,
                                                   migrate),
                        fake_migrate=fake_migrate,
                        format='%(first_name)s %(last_name)s (%(id)s)'))
        reference_table_user = 'reference %s' % settings.table_user_name
        if settings.table_group_name not in db.tables:
            extra_fields = settings.extra_fields.get(
                settings.table_group_name, []) + signature_list
            db.define_table(
                settings.table_group_name,
                Field('role', length=512, default='',
                      label=self.messages.label_role,
                      requires=IS_NOT_IN_DB(db, '%s.role' % settings.table_group_name)),
                Field('description', 'text',
                      label=self.messages.label_description),
                *extra_fields,
                **dict(
                    migrate=self.__get_migrate(
                        settings.table_group_name, migrate),
                    fake_migrate=fake_migrate,
                    format='%(role)s (%(id)s)'))
        reference_table_group = 'reference %s' % settings.table_group_name
        if settings.table_membership_name not in db.tables:
            extra_fields = settings.extra_fields.get(
                settings.table_membership_name, []) + signature_list
            db.define_table(
                settings.table_membership_name,
                Field('user_id', reference_table_user,
                      label=self.messages.label_user_id),
                Field('group_id', reference_table_group,
                      label=self.messages.label_group_id),
                *extra_fields,
                **dict(
                    migrate=self.__get_migrate(
                        settings.table_membership_name, migrate),
                    fake_migrate=fake_migrate))
        if settings.table_permission_name not in db.tables:
            extra_fields = settings.extra_fields.get(
                settings.table_permission_name, []) + signature_list
            db.define_table(
                settings.table_permission_name,
                Field('group_id', reference_table_group,
                      label=self.messages.label_group_id),
                Field('name', default='default', length=512,
                      label=self.messages.label_name,
                      requires=is_not_empty),
                Field('table_name', length=512,
                      label=self.messages.label_table_name),
                Field('record_id', 'integer', default=0,
                      label=self.messages.label_record_id,
                      requires=IS_INT_IN_RANGE(0, 10 ** 9)),
                *extra_fields,
                **dict(
                    migrate=self.__get_migrate(
                        settings.table_permission_name, migrate),
                    fake_migrate=fake_migrate))
        if settings.table_event_name not in db.tables:
            db.define_table(
                settings.table_event_name,
                Field('time_stamp', 'datetime',
                      default=current.request.now,
                      label=self.messages.label_time_stamp),
                Field('client_ip',
                      default=current.request.client,
                      label=self.messages.label_client_ip),
                Field('user_id', reference_table_user, default=None,
                      label=self.messages.label_user_id),
                Field('origin', default='auth', length=512,
                      label=self.messages.label_origin,
                      requires=is_not_empty),
                Field('description', 'text', default='',
                      label=self.messages.label_description,
                      requires=is_not_empty),
                *settings.extra_fields.get(settings.table_event_name, []),
                **dict(
                    migrate=self.__get_migrate(
                        settings.table_event_name, migrate),
                    fake_migrate=fake_migrate))
        now = current.request.now
        if settings.cas_domains:
            if settings.table_cas_name not in db.tables:
                db.define_table(
                    settings.table_cas_name,
                    Field('user_id', reference_table_user, default=None,
                          label=self.messages.label_user_id),
                    Field('created_on', 'datetime', default=now),
                    Field('service', requires=IS_URL()),
                    Field('ticket'),
                    Field('renew', 'boolean', default=False),
                    *settings.extra_fields.get(settings.table_cas_name, []),
                    **dict(
                        migrate=self.__get_migrate(
                            settings.table_cas_name, migrate),
                        fake_migrate=fake_migrate))
        if settings.enable_tokens:
            extra_fields = settings.extra_fields.get(
                settings.table_token_name, []) + signature_list
            if settings.table_token_name not in db.tables:
                db.define_table(
                    settings.table_token_name,
                    Field('user_id', reference_table_user, default=None,
                          label=self.messages.label_user_id),
                    Field('expires_on', 'datetime', default=datetime.datetime(2999,12,31)),
                    Field('token',writable=False,default=web2py_uuid,unique=True),
                    *extra_fields,
                    **dict(
                        migrate=self.__get_migrate(
                            settings.table_token_name, migrate),
                        fake_migrate=fake_migrate))
        if not db._lazy_tables:
            settings.table_user = db[settings.table_user_name]
            settings.table_group = db[settings.table_group_name]
            settings.table_membership = db[settings.table_membership_name]
            settings.table_permission = db[settings.table_permission_name]
            settings.table_event = db[settings.table_event_name]
            if settings.cas_domains:
                settings.table_cas = db[settings.table_cas_name]

        if settings.cas_provider:  # THIS IS NOT LAZY
            settings.actions_disabled = \
                ['profile', 'register', 'change_password',
                 'request_reset_password', 'retrieve_username']
            from gluon.contrib.login_methods.cas_auth import CasAuth
            maps = settings.cas_maps
            if not maps:
                table_user = self.table_user()
                maps = dict((name, lambda v, n=name: v.get(n, None)) for name in
                            table_user.fields if name != 'id'
                            and table_user[name].readable)
                maps['registration_id'] = \
                    lambda v, p=settings.cas_provider: '%s/%s' % (p, v['user'])
            actions = [settings.cas_actions['login'],
                       settings.cas_actions['servicevalidate'],
                       settings.cas_actions['logout']]
            settings.login_form = CasAuth(
                casversion=2,
                urlbase=settings.cas_provider,
                actions=actions,
                maps=maps)
        return self

    def log_event(self, description, vars=None, origin='auth'):
        """
        Examples:
            Use as::

                auth.log_event(description='this happened', origin='auth')

        """
        if not self.settings.logging_enabled or not description:
            return
        elif self.is_logged_in():
            user_id = self.user.id
        else:
            user_id = None  # user unknown
        vars = vars or {}
        # log messages should not be translated
        if type(description).__name__ == 'lazyT':
            description = description.m
        self.table_event().insert(
            description=str(description % vars),
            origin=origin, user_id=user_id)

    def get_or_create_user(self, keys, update_fields=['email'],
                           login=True, get=True):
        """
        Used for alternate login methods:
        If the user exists already then password is updated.
        If the user doesn't yet exist, then they are created.
        """
        table_user = self.table_user()
        user = None
        checks = []
        # make a guess about who this user is
        for fieldname in ['registration_id', 'username', 'email']:
            if fieldname in table_user.fields() and \
                    keys.get(fieldname, None):
                checks.append(fieldname)
                value = keys[fieldname]
                user = table_user(**{fieldname: value})
                if user:
                    break
        if not checks:
            return None
        if 'registration_id' not in keys:
            keys['registration_id'] = keys[checks[0]]
        # if we think we found the user but registration_id does not match,
        # make new user
        if 'registration_id' in checks \
                and user \
                and user.registration_id \
                and ('registration_id' not in keys or user.registration_id != str(keys['registration_id'])):
            user = None  # THINK MORE ABOUT THIS? DO WE TRUST OPENID PROVIDER?
        if user:
            if not get:
                # added for register_bare to avoid overwriting users
                return None
            update_keys = dict(registration_id=keys['registration_id'])
            for key in update_fields:
                if key in keys:
                    update_keys[key] = keys[key]
            user.update_record(**update_keys)
        elif checks:
            if not 'first_name' in keys and 'first_name' in table_user.fields:
                guess = keys.get('email', 'anonymous').split('@')[0]
                keys['first_name'] = keys.get('username', guess)
            form = table_user._filter_fields(keys)
            user_id = table_user.insert(**form)
            user = table_user[user_id]
            if self.settings.create_user_groups:
                group_id = self.add_group(
                    self.settings.create_user_groups % user)
                self.add_membership(group_id, user_id)
            if self.settings.everybody_group_id:
                self.add_membership(self.settings.everybody_group_id, user_id)
            if login:
                self.user = user
            if self.settings.register_onaccept:
                callback(self.settings.register_onaccept, form)
        return user

    def basic(self, basic_auth_realm=False):
        """
        Performs basic login.

        Args:
            basic_auth_realm: optional basic http authentication realm. Can take
                str or unicode or function or callable or boolean.

        reads current.request.env.http_authorization
        and returns basic_allowed,basic_accepted,user.

        if basic_auth_realm is defined is a callable it's return value
        is used to set the basic authentication realm, if it's a string
        its content is used instead.  Otherwise basic authentication realm
        is set to the application name.
        If basic_auth_realm is None or False (the default) the behavior
        is to skip sending any challenge.

        """
        if not self.settings.allow_basic_login:
            return (False, False, False)
        basic = current.request.env.http_authorization
        if basic_auth_realm:
            if callable(basic_auth_realm):
                basic_auth_realm = basic_auth_realm()
            elif isinstance(basic_auth_realm, (unicode, str)):
                basic_realm = unicode(basic_auth_realm)
            elif basic_auth_realm is True:
                basic_realm = u'' + current.request.application
            http_401 = HTTP(401, u'Not Authorized', **{'WWW-Authenticate': u'Basic realm="' + basic_realm + '"'})
        if not basic or not basic[:6].lower() == 'basic ':
            if basic_auth_realm:
                raise http_401
            return (True, False, False)
        (username, sep, password) = base64.b64decode(basic[6:]).partition(':')
        is_valid_user = sep and self.login_bare(username, password)
        if not is_valid_user and basic_auth_realm:
            raise http_401
        return (True, True, is_valid_user)

    def login_user(self, user):
        """
        Logins the `user = db.auth_user(id)`
        """
        if False: # FIX THIS global_settings.web2py_runtime_gae:
            user = Row(self.table_user()._filter_fields(user, id=True))
            delattr(user, 'password')
        else:
            user = Row(user)
            for key, value in user.items():
                if callable(value) or key == 'password':
                    delattr(user, key)
        if self.settings.renew_session_onlogin:
            current.session.renew(clear_session=not self.settings.keep_session_onlogin)
        current.session.auth = Storage(user=user,
                                       last_visit=current.request.now,
                                       expiration=self.settings.expiration,
                                       hmac_key=web2py_uuid())
        self.user = user
        self.update_groups()

    def _get_login_settings(self):
        table_user = self.table_user()
        userfield = self.settings.login_userfield or 'username' \
            if 'username' in table_user.fields else 'email'
        passfield = self.settings.password_field
        return Storage({'table_user': table_user,
                        'userfield': userfield,
                        'passfield': passfield})

    def login_bare(self, username, password):
        """
        Logins user as specified by username (or email) and password
        """
        settings = self._get_login_settings()
        user = settings.table_user(**{settings.userfield: username})
        if user and user.get(settings.passfield, False):
            password = settings.table_user[
                settings.passfield].validate(password)[0]
            if ((user.registration_key is None or
                 not user.registration_key.strip()) and
                password == user[settings.passfield]):
                self.login_user(user)
                return user
        else:
            # user not in database try other login methods
            for login_method in self.settings.login_methods:
                if login_method != self and login_method(username, password):
                    self.user = user
                    return user
        return False

    def register_bare(self, **fields):
        """
        Registers a user as specified by username (or email)
        and a raw password.
        """
        settings = self._get_login_settings()
        # users can register_bare even if no password is provided,
        # in this case they will have to reset their password to login
        if fields.get(settings.passfield):
            fields[settings.passfield] = \
                settings.table_user[settings.passfield].validate(fields[settings.passfield])[0]
        if not fields.get(settings.userfield):
            raise ValueError('register_bare: ' +
                             'userfield not provided or invalid')
        user = self.get_or_create_user(fields, login=False, get=False,
                                       update_fields=self.settings.update_fields)
        if not user:
            # get or create did not create a user (it ignores duplicate records)
            return False
        return user

    def cas_login(self,
                  next=DEFAULT,
                  onvalidation=DEFAULT,
                  onaccept=DEFAULT,
                  log=DEFAULT,
                  version=2,
                  ):
        request = current.request
        response = current.response
        session = current.session
        db, table = self.db, self.table_cas()
        session._cas_service = request.vars.service or session._cas_service
        if request.env.http_host not in self.settings.cas_domains or \
                not session._cas_service:
            raise HTTP(403, 'not authorized')

        def allow_access(interactivelogin=False):
            row = table(service=session._cas_service, user_id=self.user.id)
            if row:
                ticket = row.ticket
            else:
                ticket = 'ST-' + web2py_uuid()
                table.insert(service=session._cas_service,
                             user_id=self.user.id,
                             ticket=ticket,
                             created_on=request.now,
                             renew=interactivelogin)
            service = session._cas_service
            query_sep = '&' if '?' in service else '?'
            del session._cas_service
            if 'warn' in request.vars and not interactivelogin:
                response.headers[
                    'refresh'] = "5;URL=%s" % service + query_sep + "ticket=" + ticket
                return A("Continue to %s" % service,
                         _href=service + query_sep + "ticket=" + ticket)
            else:
                redirect(service + query_sep + "ticket=" + ticket)
        if self.is_logged_in() and not 'renew' in request.vars:
            return allow_access()
        elif not self.is_logged_in() and 'gateway' in request.vars:
            redirect(session._cas_service)

        def cas_onaccept(form, onaccept=onaccept):
            if not onaccept is DEFAULT:
                onaccept(form)
            return allow_access(interactivelogin=True)
        return self.login(next, onvalidation, cas_onaccept, log)

    def cas_validate(self, version=2, proxy=False):
        request = current.request
        db, table = self.db, self.table_cas()
        current.response.headers['Content-Type'] = 'text'
        ticket = request.vars.ticket
        renew = 'renew' in request.vars
        row = table(ticket=ticket)
        success = False
        if row:
            userfield = self.settings.login_userfield or 'username' \
                if 'username' in table.fields else 'email'
            # If ticket is a service Ticket and RENEW flag respected
            if ticket[0:3] == 'ST-' and \
                    not ((row.renew and renew) ^ renew):
                user = self.table_user()(row.user_id)
                row.delete_record()
                success = True

        def build_response(body):
            return '<?xml version="1.0" encoding="UTF-8"?>\n' +\
                TAG['cas:serviceResponse'](
                    body, **{'_xmlns:cas': 'http://www.yale.edu/tp/cas'}).xml()
        if success:
            if version == 1:
                message = 'yes\n%s' % user[userfield]
            else:  # assume version 2
                username = user.get('username', user[userfield])
                message = build_response(
                    TAG['cas:authenticationSuccess'](
                        TAG['cas:user'](username),
                        *[TAG['cas:' + field.name](user[field.name])
                          for field in self.table_user()
                          if field.readable]))
        else:
            if version == 1:
                message = 'no\n'
            elif row:
                message = build_response(TAG['cas:authenticationFailure']())
            else:
                message = build_response(
                    TAG['cas:authenticationFailure'](
                        'Ticket %s not recognized' % ticket,
                        _code='INVALID TICKET'))
        raise HTTP(200, message)

    def _reset_two_factor_auth(self, session):
        """
        When two-step authentication is enabled, this function is used to
        clear the session after successfully completing second challenge
        or when the maximum number of tries allowed has expired.
        """
        session.auth_two_factor_user = None
        session.auth_two_factor = None
        session.auth_two_factor_enabled = False
        # Set the number of attempts. It should be more than 1.
        session.auth_two_factor_tries_left = self.settings.auth_two_factor_tries_left

    def when_is_logged_in_bypass_next_in_url(self, next, session):
        """
        This function should be use when someone want to avoid asking for user
        credentials when loaded page contains "user/login?_next=NEXT_COMPONENT"
        in the URL is refresh but user is already authenticated.
        """
        if self.is_logged_in():
            if next == session._auth_next:
                del session._auth_next
            redirect(next, client_side=self.settings.client_side)

    def login(self,
              next=DEFAULT,
              onvalidation=DEFAULT,
              onaccept=DEFAULT,
              log=DEFAULT,
              ):
        """
        Returns a login form
        """
        settings = self.settings
        request = current.request
        response = current.response
        session = current.session

        ### use session for federated login
        snext = self.get_vars_next()

        if snext:
            session._auth_next = snext
        elif session._auth_next:
            snext = session._auth_next
        ### pass

        if next is DEFAULT:
            # important for security
            next = settings.login_next
            if callable(next):
                next = next()
            user_next = snext
            if user_next:
                external = user_next.split('://')
                if external[0].lower() in ['http', 'https', 'ftp']:
                    host_next = user_next.split('//', 1)[-1].split('/')[0]
                    if host_next in settings.cas_domains:
                        next = user_next
                else:
                    next = user_next
                    # Avoid asking unnecessary user credentials when user is logged in
                    self.when_is_logged_in_bypass_next_in_url(next=next, session=session)

        # Moved here to avoid unnecessary execution in case of redirection to next in case of logged in user
        table_user = self.table_user()
        if 'username' in table_user.fields or \
                not settings.login_email_validate:
            tmpvalidator = IS_NOT_EMPTY(error_message=self.messages.is_empty)
            if not settings.username_case_sensitive:
                tmpvalidator = [IS_LOWER(), tmpvalidator]
        else:
            tmpvalidator = IS_EMAIL(error_message=self.messages.invalid_email)
            if not settings.email_case_sensitive:
                tmpvalidator = [IS_LOWER(), tmpvalidator]

        passfield = settings.password_field
        try:
            table_user[passfield].requires[-1].min_length = 0
        except:
            pass

        if onvalidation is DEFAULT:
            onvalidation = settings.login_onvalidation
        if onaccept is DEFAULT:
            onaccept = settings.login_onaccept
        if log is DEFAULT:
            log = self.messages['login_log']

        onfail = settings.login_onfail

        user = None  # default

        # Setup the default field used for the form
        multi_login = False
        if self.settings.login_userfield:
            username = self.settings.login_userfield
        else:
            if 'username' in table_user.fields:
                username = 'username'
            else:
                username = 'email'
            if self.settings.multi_login:
                multi_login = True
        old_requires = table_user[username].requires
        table_user[username].requires = tmpvalidator

        # If two-factor authentication is enabled, and the maximum
        # number of tries allowed is used up, reset the session to
        # pre-login state with two-factor auth
        if session.auth_two_factor_enabled and session.auth_two_factor_tries_left < 1:
            # Exceeded maximum allowed tries for this code. Require user to enter
            # username and password again.
            user = None
            accepted_form = False
            self._reset_two_factor_auth(session)
            # Redirect to the default 'next' page without logging
            # in. If that page requires login, user will be redirected
            # back to the main login form
            redirect(next, client_side=settings.client_side)

        # Before showing the default login form, check whether
        # we are already on the second step of two-step authentication.
        # If we are, then skip this login form and use the form for the
        # second challenge instead.
        # Note to devs: The code inside the if-block is unchanged from the
        # previous version of this file, other than for indentation inside
        # to put it inside the if-block
        if session.auth_two_factor_user is None:

            if settings.remember_me_form:
                extra_fields = [
                    Field('remember_me', 'boolean', default=False,
                          label=self.messages.label_remember_me)]
            else:
                extra_fields = []

            # do we use our own login form, or from a central source?
            if settings.login_form == self:
                form = Form([table_user[username],table_user[passfield]],
                            hidden=dict(_next=next),
                            #showid=settings.showid, # FIX THESE
                            #submit_button=self.messages.login_button,
                            #delete_label=self.messages.delete_label,
                            #formstyle=settings.formstyle,
                            #separator=settings.label_separator,
                            #extra_fields=extra_fields,
                            )

                captcha = settings.login_captcha or \
                    (settings.login_captcha != False and settings.captcha)
                if captcha:
                    addrow(form, captcha.label, captcha, captcha.comment,
                           settings.formstyle, 'captcha__row')
                accepted_form = False

                if form.accepted:

                    accepted_form = True
                    # check for username in db
                    entered_username = form.vars[username]
                    if multi_login and '@' in entered_username:
                        # if '@' in username check for email, not username
                        user = table_user(email=entered_username)
                    else:
                        user = table_user(**{username: entered_username})
                    print user
                    if user:
                        # user in db, check if registration pending or disabled
                        temp_user = user                        
                        if (temp_user.registration_key or '').startswith('pending'):
                            response.flash = self.messages.registration_pending
                            return form
                        elif temp_user.registration_key in ('disabled', 'blocked'):
                            response.flash = self.messages.login_disabled
                            return form
                        elif (temp_user.registration_key is not None
                              and temp_user.registration_key.strip()):
                            response.flash = \
                                self.messages.registration_verifying
                            return form
                        # try alternate logins 1st as these have the
                        # current version of the password
                        user = None
                        for login_method in settings.login_methods:
                            if login_method != self and \
                                    login_method(request.vars[username],
                                                 request.vars[passfield]):
                                if self not in settings.login_methods:
                                    # do not store password in db
                                    form.vars[passfield] = None
                                user = self.get_or_create_user(
                                    form.vars, settings.update_fields)
                                break
                        if not user:
                            # alternates have failed, maybe because service inaccessible
                            if settings.login_methods[0] == self:
                                # try logging in locally using cached credentials
                                if form.vars.get(passfield, '') == temp_user[passfield]:
                                    # success
                                    user = temp_user
                    else:
                        # user not in db
                        if not settings.alternate_requires_registration:
                            # we're allowed to auto-register users from external systems
                            for login_method in settings.login_methods:
                                if login_method != self and \
                                        login_method(request.vars[username],
                                                     request.vars[passfield]):
                                    if self not in settings.login_methods:
                                        # do not store password in db
                                        form.vars[passfield] = None
                                    user = self.get_or_create_user(
                                        form.vars, settings.update_fields)
                                    break
                    if not user:
                        self.log_event(self.messages['login_failed_log'],
                                       request.post_vars)
                        # invalid login
                        session.flash = self.messages.invalid_login
                        callback(onfail, None)
                        redirect(
                            self.url(args=request.args, vars=request.get_vars),
                            client_side=settings.client_side)

            else:  # use a central authentication server
                cas = settings.login_form
                cas_user = cas.get_user()

                if cas_user:
                    cas_user[passfield] = None
                    user = self.get_or_create_user(
                        table_user._filter_fields(cas_user),
                        settings.update_fields)
                elif hasattr(cas, 'login_form'):
                    return cas.login_form()
                else:
                    # we need to pass through login again before going on
                    next = self.url(settings.function, args='login')
                    redirect(cas.login_url(next),
                             client_side=settings.client_side)

        # Extra login logic for two-factor authentication
        #################################################
        # If the 'user' variable has a value, this means that the first
        # authentication step was successful (i.e. user provided correct
        # username and password at the first challenge).
        # Check if this user is signed up for two-factor authentication
        # If auth.settings.auth_two_factor_enabled it will enable two factor
        # for all the app. Another way to anble two factor is that the user
        # must be part of a group that is called auth.settings.two_factor_authentication_group
        if user and self.settings.auth_two_factor_enabled == True:
            session.auth_two_factor_enabled = True
        elif user and self.settings.two_factor_authentication_group:
            role = self.settings.two_factor_authentication_group
            session.auth_two_factor_enabled = self.has_membership(user_id=user.id, role=role)
        # challenge
        if session.auth_two_factor_enabled:
            form = Form([Field('authentication_code',
                          label=self.messages.label_two_factor,required=True,
                          comment=self.messages.two_factor_comment)],
                        hidden=dict(_next=next),
                        #formstyle=settings.formstyle, # FIX THESE
                        #separator=settings.label_separator
            )
            # accepted_form is used by some default web2py code later in the
            # function that handles running specified functions before redirect
            # Set it to False until the challenge form is accepted.
            accepted_form = False
            # Handle the case when a user has submitted the login/password
            # form successfully, and the password has been validated, but
            # the two-factor form has not been displayed or validated yet.
            if session.auth_two_factor_user is None and user is not None:
                session.auth_two_factor_user = user  # store the validated user and associate with this session
                session.auth_two_factor = random.randint(100000, 999999)
                session.auth_two_factor_tries_left = self.settings.auth_two_factor_tries_left
                # Set the way we generate the code or we send the code. For example using SMS...
                two_factor_methods = self.settings.two_factor_methods

                if two_factor_methods == []:
                    # TODO: Add some error checking to handle cases where email cannot be sent
                    self.settings.mailer.send(
                        to=user.email,
                        subject=self.messages.retrieve_two_factor_code_subject,
                        message=self.messages.retrieve_two_factor_code.format(session.auth_two_factor))
                else:
                    #Check for all method. It is possible to have multiples
                    for two_factor_method in two_factor_methods:
                        try:
                            # By default we use session.auth_two_factor generated before.
                            session.auth_two_factor = two_factor_method(user, session.auth_two_factor)
                        except:
                            pass
                        else:
                            break

            if form.accepted:
                accepted_form = True

                accepted_form = True

                '''
                The lists is executed after form validation for each of the corresponding action.
                For example, in your model:

                In your models copy and paste:

                #Before define tables, we add some extra field to auth_user
                auth.settings.extra_fields['auth_user'] = [
                    Field('motp_secret', 'password', length=512, default='', label='MOTP Secret'),
                    Field('motp_pin', 'string', length=128, default='', label='MOTP PIN')]

                OFFSET = 60 #Be sure is the same in your OTP Client

                #Set session.auth_two_factor to None. Because the code is generated by external app.
                # This will avoid to use the default setting and send a code by email.
                def _set_two_factor(user, auth_two_factor):
                    return None

                def verify_otp(user, otp):
                import time
                from hashlib import md5
                epoch_time = int(time.time())
                time_start = int(str(epoch_time - OFFSET)[:-1])
                time_end = int(str(epoch_time + OFFSET)[:-1])
                for t in range(time_start - 1, time_end + 1):
                    to_hash = str(t) + user.motp_secret + user.motp_pin
                    hash = md5(to_hash).hexdigest()[:6]
                    if otp == hash:
                    return hash

                auth.settings.auth_two_factor_enabled = True
                auth.messages.two_factor_comment = "Verify your OTP Client for the code."
                auth.settings.two_factor_methods = [lambda user, auth_two_factor: _set_two_factor(user, auth_two_factor)]
                auth.settings.two_factor_onvalidation = [lambda user, otp: verify_otp(user, otp)]

                '''
                if self.settings.two_factor_onvalidation != []:

                    for two_factor_onvalidation in self.settings.two_factor_onvalidation:
                        try:
                            session.auth_two_factor = two_factor_onvalidation(session.auth_two_factor_user, form.vars['authentication_code'])
                        except:
                            pass
                        else:
                            break

                if form.vars['authentication_code'] == str(session.auth_two_factor):
                    # Handle the case when the two-factor form has been successfully validated
                    # and the user was previously stored (the current user should be None because
                    # in this case, the previous username/password login form should not be displayed.
                    # This will allow the code after the 2-factor authentication block to proceed as
                    # normal.
                    if user is None or user == session.auth_two_factor_user:
                        user = session.auth_two_factor_user
                    # For security, because the username stored in the
                    # session somehow does not match the just validated
                    # user. Should not be possible without session stealing
                    # which is hard with SSL.
                    elif user != session.auth_two_factor_user:
                        user = None
                    # Either way, the user and code associated with this session should
                    # be removed. This handles cases where the session login may have
                    # expired but browser window is open, so the old session key and
                    # session usernamem will still exist
                    self._reset_two_factor_auth(session)
                else:
                    session.auth_two_factor_tries_left -= 1
                    # If the number of retries are higher than auth_two_factor_tries_left
                    # Require user to enter username and password again.
                    if session.auth_two_factor_enabled and session.auth_two_factor_tries_left < 1:
                        # Exceeded maximum allowed tries for this code. Require user to enter
                        # username and password again.
                        user = None
                        accepted_form = False
                        self._reset_two_factor_auth(session)
                        # Redirect to the default 'next' page without logging
                        # in. If that page requires login, user will be redirected
                        # back to the main login form
                        redirect(next, client_side=settings.client_side)
                    response.flash = self.messages.invalid_two_factor_code.format(session.auth_two_factor_tries_left)
                    return form
            else:
                return form
        # End login logic for two-factor authentication

        # process authenticated users
        if user:
            user = Row(table_user._filter_fields(user, id=True))
            print user
            # process authenticated users
            # user wants to be logged in for longer
            self.login_user(user)
            session.auth.expiration = \
                request.post_vars.remember_me and \
                settings.long_expiration or \
                settings.expiration
            session.auth.remember_me = 'remember_me' in request.post_vars
            self.log_event(log, user)
            session.flash = self.messages.logged_in

        # how to continue
        if settings.login_form == self:
            if accepted_form:
                callback(onaccept, form)
                if next == session._auth_next:
                    session._auth_next = None
                next = replace_id(next, form)
                redirect(next, client_side=settings.client_side)

            table_user[username].requires = old_requires
            return form
        elif user:
            callback(onaccept, None)

        if next == session._auth_next:
            del session._auth_next
        redirect(next, client_side=settings.client_side)

    def logout(self, next=DEFAULT, onlogout=DEFAULT, log=DEFAULT):
        """
        Logouts and redirects to login
        """

        # Clear out 2-step authentication information if user logs
        # out. This information is also cleared on successful login.
        self._reset_two_factor_auth(current.session)

        if next is DEFAULT:
            next = self.get_vars_next() or self.settings.logout_next
        if onlogout is DEFAULT:
            onlogout = self.settings.logout_onlogout
        if onlogout:
            onlogout(self.user)
        if log is DEFAULT:
            log = self.messages['logout_log']
        if self.user:
            self.log_event(log, self.user)
        if self.settings.login_form != self:
            cas = self.settings.login_form
            cas_user = cas.get_user()
            if cas_user:
                next = cas.logout_url(next)

        current.session.auth = None
        if self.settings.renew_session_onlogout:
            current.session.renew(clear_session=not self.settings.keep_session_onlogout)
        current.session.flash = self.messages.logged_out
        if next is not None:
            redirect(next)

    def register(self,
                 next=DEFAULT,
                 onvalidation=DEFAULT,
                 onaccept=DEFAULT,
                 log=DEFAULT,
                 ):
        """
        Returns a registration form
        """

        table_user = self.table_user()
        request = current.request
        response = current.response
        session = current.session
        if self.is_logged_in():
            redirect(self.settings.logged_url,
                     client_side=self.settings.client_side)
        if next is DEFAULT:
            next = self.get_vars_next() or self.settings.register_next
        if onvalidation is DEFAULT:
            onvalidation = self.settings.register_onvalidation
        if onaccept is DEFAULT:
            onaccept = self.settings.register_onaccept
        if log is DEFAULT:
            log = self.messages['register_log']

        table_user = self.table_user()
        if self.settings.login_userfield:
            username = self.settings.login_userfield
        elif 'username' in table_user.fields:
            username = 'username'
        else:
            username = 'email'

        # Ensure the username field is unique.
        unique_validator = IS_NOT_IN_DB(self.db, table_user[username])
        if not table_user[username].requires:
            table_user[username].requires = unique_validator
        elif isinstance(table_user[username].requires, (list, tuple)):
            if not any([isinstance(validator, IS_NOT_IN_DB) for validator in
                        table_user[username].requires]):
                if isinstance(table_user[username].requires, list):
                    table_user[username].requires.append(unique_validator)
                else:
                    table_user[username].requires += (unique_validator, )
        elif not isinstance(table_user[username].requires, IS_NOT_IN_DB):
            table_user[username].requires = [table_user[username].requires,
                                             unique_validator]

        passfield = self.settings.password_field
        formstyle = self.settings.formstyle
        try: # Make sure we have our original minimum length as other auth forms change it
            table_user[passfield].requires[-1].min_length = self.settings.password_min_length
        except:
            pass

        if self.settings.register_verify_password:
            if self.settings.register_fields is None:
                self.settings.register_fields = [f.name for f in table_user if f.writable]
                k = self.settings.register_fields.index("password")
                self.settings.register_fields.insert(k+1, "password_two")
            extra_fields = [
                Field("password_two", "password",
                      requires=IS_EQUAL_TO(request.post_vars.get(passfield, None),
                                           error_message=self.messages.mismatched_password),
                      label=current.T("Confirm Password"))]
        else:
            extra_fields = []
        if self.settings.register_fields:
            for field in table_user: field.writable = (field.name in self.settings.register_fields)
        form = Form(table_user,
                    hidden=dict(_next=next),
                    # showid=self.settings.showid,
                    # submit_button=self.messages.register_button,
                    # delete_label=self.messages.delete_label,
                    # formstyle=formstyle,
                    # separator=self.settings.label_separator,
                    # extra_fields=extra_fields
                    )

        captcha = self.settings.register_captcha or self.settings.captcha
        if captcha:
            addrow(form, captcha.label, captcha,
                   captcha.comment, self.settings.formstyle, 'captcha__row')

        # Add a message if specified
        if self.settings.pre_registration_div:
            addrow(form, '',
                   DIV(_id="pre-reg", *self.settings.pre_registration_div),
                   '', formstyle, '')

        key = web2py_uuid()
        if self.settings.registration_requires_approval:
            key = 'pending-'+key

        table_user.registration_key.default = key
        if form.accepted:
            description = self.messages.group_description % form.vars
            if self.settings.create_user_groups:
                group_id = self.add_group(
                    self.settings.create_user_groups % form.vars, description)
                self.add_membership(group_id, form.vars.id)
            if self.settings.everybody_group_id:
                self.add_membership(
                    self.settings.everybody_group_id, form.vars.id)
            if self.settings.registration_requires_verification:
                link = self.url(
                    self.settings.function, args=('verify_email', key), scheme=True)
                d = dict(form.vars)
                d.update(dict(key=key, link=link, username=form.vars[username]))
                if not (self.settings.mailer and self.settings.mailer.send(
                        to=form.vars.email,
                        subject=self.messages.verify_email_subject,
                        message=self.messages.verify_email % d)):
                    self.db.rollback()
                    response.flash = self.messages.unable_send_email
                    return form
                session.flash = self.messages.email_sent
            if self.settings.registration_requires_approval and \
               not self.settings.registration_requires_verification:
                table_user[form.vars.id] = dict(registration_key='pending')
                session.flash = self.messages.registration_pending
            elif (not self.settings.registration_requires_verification or
                      self.settings.login_after_registration):
                if not self.settings.registration_requires_verification:
                    table_user[form.vars.id] = dict(registration_key='')
                session.flash = self.messages.registration_successful
                user = table_user(**{username: form.vars[username]})
                self.login_user(user)
                session.flash = self.messages.logged_in
            self.log_event(log, form.vars)
            callback(onaccept, form)
            if not next:
                next = self.url(args=request.args)
            else:
                next = replace_id(next, form)
            redirect(next, client_side=self.settings.client_side)

        return form

    def is_logged_in(self):
        """
        Checks if the user is logged in and returns True/False.
        If so user is in auth.user as well as in session.auth.user
        """

        if self.user:
            return True
        return False

    def verify_email(self,
                     next=DEFAULT,
                     onaccept=DEFAULT,
                     log=DEFAULT,
                     ):
        """
        Action used to verify the registration email
        """

        key = getarg(-1)
        table_user = self.table_user()
        user = table_user(registration_key=key)
        if not user:
            redirect(self.settings.login_url)
        if self.settings.registration_requires_approval:
            user.update_record(registration_key='pending')
            current.session.flash = self.messages.registration_pending
        else:
            user.update_record(registration_key='')
            current.session.flash = self.messages.email_verified
        # make sure session has same user.registrato_key as db record
        if current.session.auth and current.session.auth.user:
            current.session.auth.user.registration_key = user.registration_key
        if log is DEFAULT:
            log = self.messages['verify_email_log']
        if next is DEFAULT:
            next = self.settings.verify_email_next
        if onaccept is DEFAULT:
            onaccept = self.settings.verify_email_onaccept
        self.log_event(log, user)
        callback(onaccept, user)
        redirect(next)

    def retrieve_username(self,
                          next=DEFAULT,
                          onvalidation=DEFAULT,
                          onaccept=DEFAULT,
                          log=DEFAULT,
                          ):
        """
        Returns a form to retrieve the user username
        (only if there is a username field)
        """

        table_user = self.table_user()
        if 'username' not in table_user.fields:
            raise HTTP(404)
        request = current.request
        response = current.response
        session = current.session
        captcha = self.settings.retrieve_username_captcha or \
                  (self.settings.retrieve_username_captcha != False and self.settings.captcha)
        if not self.settings.mailer:
            response.flash = self.messages.function_disabled
            return ''
        if next is DEFAULT:
            next = self.get_vars_next() or self.settings.retrieve_username_next
        if onvalidation is DEFAULT:
            onvalidation = self.settings.retrieve_username_onvalidation
        if onaccept is DEFAULT:
            onaccept = self.settings.retrieve_username_onaccept
        if log is DEFAULT:
            log = self.messages['retrieve_username_log']
        old_requires = table_user.email.requires
        table_user.email.requires = [IS_IN_DB(self.db, table_user.email,
                                              error_message=self.messages.invalid_email)]
        form = Form([table_user['email']],                    
                    hidden=dict(_next=next),
                    #showid=self.settings.showid,
                    #submit_button=self.messages.submit_button,
                    #delete_label=self.messages.delete_label,
                    #  formstyle=self.settings.formstyle,
                    #   separator=self.settings.label_separator
                    )
        if captcha:
            addrow(form, captcha.label, captcha,
                   captcha.comment, self.settings.formstyle, 'captcha__row')

        if form.accepted:
            users = table_user._db(table_user.email == form.vars.email).select()
            if not users:
                current.session.flash = \
                    self.messages.invalid_email
                redirect(self.url(args=request.args))
            username = ', '.join(u.username for u in users)
            self.settings.mailer.send(to=form.vars.email,
                                      subject=self.messages.retrieve_username_subject,
                                      message=self.messages.retrieve_username % dict(username=username))
            session.flash = self.messages.email_sent
            for user in users:
                self.log_event(log, user)
            callback(onaccept, form)
            if not next:
                next = self.url(args=request.args)
            else:
                next = replace_id(next, form)
            redirect(next)
        table_user.email.requires = old_requires
        return form

    def random_password(self):
        import string
        import random
        password = ''
        specials = r'!#$*'
        for i in range(0, 3):
            password += random.choice(string.lowercase)
            password += random.choice(string.uppercase)
            password += random.choice(string.digits)
            password += random.choice(specials)
        return ''.join(random.sample(password, len(password)))

    def reset_password_deprecated(self,
                                  next=DEFAULT,
                                  onvalidation=DEFAULT,
                                  onaccept=DEFAULT,
                                  log=DEFAULT,
                                  ):
        """
        Returns a form to reset the user password (deprecated)
        """

        table_user = self.table_user()
        request = current.request
        response = current.response
        session = current.session
        if not self.settings.mailer:
            response.flash = self.messages.function_disabled
            return ''
        if next is DEFAULT:
            next = self.get_vars_next() or self.settings.retrieve_password_next
        if onvalidation is DEFAULT:
            onvalidation = self.settings.retrieve_password_onvalidation
        if onaccept is DEFAULT:
            onaccept = self.settings.retrieve_password_onaccept
        if log is DEFAULT:
            log = self.messages['retrieve_password_log']
        old_requires = table_user.email.requires
        table_user.email.requires = [IS_IN_DB(self.db, table_user.email,
                                              error_message=self.messages.invalid_email)]
        form = Form([table_user['email']],
                    hidden=dict(_next=next),
                    #   showid=self.settings.showid,
                    #   submit_button=self.messages.submit_button,
                    #   delete_label=self.messages.delete_label,
                    #   formstyle=self.settings.formstyle,
                    #   separator=self.settings.label_separator
                    )
        if form.accepted:
            user = table_user(email=form.vars.email)
            key = user.registration_key
            if not user:
                current.session.flash = \
                    self.messages.invalid_email
                redirect(self.url(args=request.args))
            elif key in ('pending', 'disabled', 'blocked') or (key or '').startswith('pending'):
                current.session.flash = \
                    self.messages.registration_pending
                redirect(self.url(args=request.args))
            password = self.random_password()
            passfield = self.settings.password_field
            d = {
                passfield: str(table_user[passfield].validate(password)[0]),
                'registration_key': ''
                }
            user.update_record(**d)
            if self.settings.mailer and \
               self.settings.mailer.send(to=form.vars.email,
                                         subject=self.messages.retrieve_password_subject,
                                         message=self.messages.retrieve_password % dict(password=password)):
                session.flash = self.messages.email_sent
            else:
                session.flash = self.messages.unable_to_send_email
            self.log_event(log, user)
            callback(onaccept, form)
            if not next:
                next = self.url(args=request.args)
            else:
                next = replace_id(next, form)
            redirect(next)
        table_user.email.requires = old_requires
        return form

    def confirm_registration(self,
                             next=DEFAULT,
                             onvalidation=DEFAULT,
                             onaccept=DEFAULT,
                             log=DEFAULT,
                             ):
        """
        Returns a form to confirm user registration
        """

        table_user = self.table_user()
        request = current.request
        # response = current.response
        session = current.session

        if next is DEFAULT:
            next = self.get_vars_next() or self.settings.reset_password_next

        if self.settings.prevent_password_reset_attacks:
            key = request.vars.key
            if not key and len(request.args)>1:
                key = request.args[-1]
            if key:
                session._reset_password_key = key
                redirect(self.url(args='confirm_registration'))
            else:
                key = session._reset_password_key
        else:
            key = request.vars.key or getarg(-1)
        try:
            t0 = int(key.split('-')[0])
            if time.time() - t0 > 60 * 60 * 24:
                raise Exception
            user = table_user(reset_password_key=key)
            if not user:
                raise Exception
        except Exception as e:
            session.flash = self.messages.invalid_reset_password
            redirect(self.url('login', vars=dict(test=e)))
            redirect(next, client_side=self.settings.client_side)
        passfield = self.settings.password_field
        form = Form([
                Field('first_name',
                      label='First Name',
                      required=True),
                Field('last_name',
                      label='Last Name',
                      required=True),
                Field('new_password', 'password',
                      label=self.messages.new_password,
                      requires=self.table_user()[passfield].requires),
                Field('new_password2', 'password',
                      label=self.messages.verify_password,
                  requires=[IS_EXPR('value==%s' % repr(request.vars.new_password),
                                    self.messages.mismatched_password)])],
                    #submit_button='Confirm Registration',
                    hidden=dict(_next=next),
                    #formstyle=self.settings.formstyle,
                    #separator=self.settings.label_separator
                    )
        if form.accepted:
            user.update_record(
                **{passfield: str(form.vars.new_password),
                   'first_name': str(form.vars.first_name),
                   'last_name': str(form.vars.last_name),
                   'registration_key': '',
                   'reset_password_key': ''})
            session.flash = self.messages.password_changed
            if self.settings.login_after_password_change:
                self.login_user(user)
            redirect(next, client_side=self.settings.client_side)
        return form

    def email_registration(self, subject, body, user):
        """
        Sends and email invitation to a user informing they have been registered with the application
        """
        reset_password_key = str(int(time.time())) + '-' + web2py_uuid()
        link = self.url(self.settings.function,
                        args=('confirm_registration',), vars={'key': reset_password_key},
                        scheme=True)
        d = dict(user)
        d.update(dict(key=reset_password_key, link=link, site=current.request.env.http_host))
        if self.settings.mailer and self.settings.mailer.send(
            to=user.email,
            subject=subject % d,
                message=body % d):
            user.update_record(reset_password_key=reset_password_key)
            return True
        return False

    def bulk_register(self, max_emails=100):
        """
        Creates a form for ther user to send invites to other users to join
        """
        if not self.user:
            redirect(self.settings.login_url)
        if not self.settings.bulk_register_enabled:
            return HTTP(404)

        form = Form([
                Field('subject', 'string', default=self.messages.bulk_invite_subject, requires=IS_NOT_EMPTY()),
                Field('emails', 'text', requires=IS_NOT_EMPTY()),
                Field('message', 'text', default=self.messages.bulk_invite_body, requires=IS_NOT_EMPTY()),
                ])

        if form.accepted:
            emails = re.compile('[^\s\'"@<>,;:]+\@[^\s\'"@<>,;:]+').findall(form.vars.emails)
            # send the invitations
            emails_sent = []
            emails_fail = []
            emails_exist = []
            for email in emails[:max_emails]:
                if self.table_user()(email=email):
                    emails_exist.append(email)
                else:
                    user = self.register_bare(email=email)
                    if self.email_registration(form.vars.subject, form.vars.message, user):
                        emails_sent.append(email)
                    else:
                        emails_fail.append(email)
            emails_fail += emails[max_emails:]
            form = DIV(H4('Emails sent'), UL(*[A(x, _href='mailto:'+x) for x in emails_sent]),
                       H4('Emails failed'), UL(*[A(x, _href='mailto:'+x) for x in emails_fail]),
                       H4('Emails existing'), UL(*[A(x, _href='mailto:'+x) for x in emails_exist]))
        return form

    def manage_tokens(self):
        if not self.user:
            redirect(self.settings.login_url)
        table_token =self.table_token()
        table_token.user_id.writable = False
        table_token.user_id.default = self.user.id
        table_token.token.writable = False
        if current.request.args and current.request.args[1] == 'new':
            table_token.token.readable = False
        # form = SQLFORM.grid(table_token, args=['manage_tokens'])  # FIX THIS - NO MORE GRID
        return form

    def reset_password(self,
                       next=DEFAULT,
                       onvalidation=DEFAULT,
                       onaccept=DEFAULT,
                       log=DEFAULT,
                       ):
        """
        Returns a form to reset the user password
        """

        table_user = self.table_user()
        request = current.request
        # response = current.response
        session = current.session

        if next is DEFAULT:
            next = self.get_vars_next() or self.settings.reset_password_next

        if self.settings.prevent_password_reset_attacks:
            key = request.vars.key
            if key:
                session._reset_password_key = key
                redirect(self.url(args='reset_password'))
            else:
                key = session._reset_password_key
        else:
            key = request.vars.key
        try:
            t0 = int(key.split('-')[0])
            if time.time() - t0 > 60 * 60 * 24:
                raise Exception
            user = table_user(reset_password_key=key)
            if not user:
                raise Exception
        except Exception:
            session.flash = self.messages.invalid_reset_password
            redirect(next, client_side=self.settings.client_side)
        
        key = user.registration_key
        if key in ('pending', 'disabled', 'blocked') or (key or '').startswith('pending'):
            session.flash = self.messages.registration_pending
            redirect(next, client_side=self.settings.client_side)

        if onvalidation is DEFAULT:
            onvalidation = self.settings.reset_password_onvalidation
        if onaccept is DEFAULT:
            onaccept = self.settings.reset_password_onaccept

        passfield = self.settings.password_field
        form = Form([
                Field('new_password', 'password',
                      label=self.messages.new_password,
                      requires=self.table_user()[passfield].requires),
                Field('new_password2', 'password',
                      label=self.messages.verify_password,
                      requires=[IS_EXPR(
                            'value==%s' % repr(request.vars.new_password),
                            self.messages.mismatched_password)])],
                    #submit_button=self.messages.password_reset_button,
                    hidden=dict(_next=next),
                    #formstyle=self.settings.formstyle,
                    #separator=self.settings.label_separator
                    )
        if form.accepted:
            user.update_record(
                **{passfield: str(form.vars.new_password),
                   'registration_key': '',
                   'reset_password_key': ''})
            session.flash = self.messages.password_changed
            if self.settings.login_after_password_change:
                self.login_user(user)
            callback(onaccept, form)
            redirect(next, client_side=self.settings.client_side)
        return form

    def request_reset_password(self,
                               next=DEFAULT,
                               onvalidation=DEFAULT,
                               onaccept=DEFAULT,
                               log=DEFAULT,
                               ):
        """
        Returns a form to reset the user password
        """
        table_user = self.table_user()
        request = current.request
        response = current.response
        session = current.session
        captcha = self.settings.retrieve_password_captcha or \
                (self.settings.retrieve_password_captcha != False and self.settings.captcha)

        if next is DEFAULT:
            next = self.get_vars_next() or self.settings.request_reset_password_next
        if not self.settings.mailer:
            response.flash = self.messages.function_disabled
            return ''
        if onvalidation is DEFAULT:
            onvalidation = self.settings.request_reset_password_onvalidation
        if onaccept is DEFAULT:
            onaccept = self.settings.request_reset_password_onaccept
        if log is DEFAULT:
            log = self.messages['reset_password_log']
        userfield = self.settings.login_userfield or 'username' \
            if 'username' in table_user.fields else 'email'
        if userfield == 'email':
            table_user.email.requires = [
                IS_EMAIL(error_message=self.messages.invalid_email),
                IS_IN_DB(self.db, table_user.email,
                         error_message=self.messages.invalid_email)]
            if not self.settings.email_case_sensitive:
                table_user.email.requires.insert(0, IS_LOWER())
        else:
            table_user.username.requires = [
                IS_IN_DB(self.db, table_user.username,
                         error_message=self.messages.invalid_username)]
            if not self.settings.username_case_sensitive:
                table_user.username.requires.insert(0, IS_LOWER())

        form = Form([table_user['userfield']],
                    hidden=dict(_next=next),
                    #showid=self.settings.showid,
                    # submit_button=self.messages.password_reset_button,
                    # delete_label=self.messages.delete_label,
                    # formstyle=self.settings.formstyle,
                    # separator=self.settings.label_separator
                    )
        if captcha:
            addrow(form, captcha.label, captcha,
                   captcha.comment, self.settings.formstyle, 'captcha__row')
        if form.accepted:
            user = table_user(**{userfield:form.vars.get(userfield)})
            key = user.registration_key 
            if not user:
                session.flash = self.messages['invalid_%s' % userfield]
                redirect(self.url(args=request.args),
                         client_side=self.settings.client_side)
            elif key in ('pending', 'disabled', 'blocked') or (key or '').startswith('pending'):
                session.flash = self.messages.registration_pending
                redirect(self.url(args=request.args),
                         client_side=self.settings.client_side)
            if self.email_reset_password(user):
                session.flash = self.messages.email_sent
            else:
                session.flash = self.messages.unable_to_send_email
            self.log_event(log, user)
            callback(onaccept, form)
            if not next:
                next = self.url(args=request.args)
            else:
                next = replace_id(next, form)
            redirect(next, client_side=self.settings.client_side)
        # old_requires = table_user.email.requires
        return form

    def email_reset_password(self, user):
        reset_password_key = str(int(time.time())) + '-' + web2py_uuid()
        link = self.url(self.settings.function,
                        args=('reset_password',), vars={'key': reset_password_key},
                        scheme=True)
        d = dict(user)
        d.update(dict(key=reset_password_key, link=link))
        if self.settings.mailer and self.settings.mailer.send(
            to=user.email,
            subject=self.messages.reset_password_subject,
                message=self.messages.reset_password % d):
            user.update_record(reset_password_key=reset_password_key)
            return True
        return False

    def retrieve_password(self,
                          next=DEFAULT,
                          onvalidation=DEFAULT,
                          onaccept=DEFAULT,
                          log=DEFAULT,
                          ):
        if self.settings.reset_password_requires_verification:
            return self.request_reset_password(next, onvalidation, onaccept, log)
        else:
            return self.reset_password_deprecated(next, onvalidation, onaccept, log)

    def change_password(self,
                        next=DEFAULT,
                        onvalidation=DEFAULT,
                        onaccept=DEFAULT,
                        log=DEFAULT,
                        ):
        """
        Returns a form that lets the user change password
        """

        if not self.is_logged_in():
            redirect(self.settings.login_url,
                     client_side=self.settings.client_side)
        db = self.db
        table_user = self.table_user()
        s = db(table_user.id == self.user.id)

        request = current.request
        session = current.session
        if next is DEFAULT:
            next = self.get_vars_next() or self.settings.change_password_next
        if onvalidation is DEFAULT:
            onvalidation = self.settings.change_password_onvalidation
        if onaccept is DEFAULT:
            onaccept = self.settings.change_password_onaccept
        if log is DEFAULT:
            log = self.messages['change_password_log']
        passfield = self.settings.password_field
        requires = table_user[passfield].requires
        if not isinstance(requires, (list, tuple)):
            requires = [requires]
        requires = filter(lambda t: isinstance(t, CRYPT), requires)
        if requires:
            requires[0].min_length = 0
        form = Form([
                    Field('old_password', 'password', requires=requires,
                          label=self.messages.old_password),
                    Field('new_password', 'password',
                          label=self.messages.new_password,
                          requires=table_user[passfield].requires),
                    Field('new_password2', 'password',
                          label=self.messages.verify_password,
                          requires=[IS_EXPR('value==%s' % repr(request.vars.new_password),
                                            self.messages.mismatched_password)])],
                    #submit_button=self.messages.password_change_button,
                    hidden=dict(_next=next),
                    #formstyle=self.settings.formstyle,
                    #separator=self.settings.label_separator
        )
        if form.accepted:
            current_user = s.select(limitby=(0, 1), orderby_on_limitby=False).first()
            if not form.vars['old_password'] == current_user[passfield]:
                form.errors['old_password'] = self.messages.invalid_password
            else:
                d = {passfield: str(form.vars.new_password)}
                s.update(**d)
                session.flash = self.messages.password_changed
                self.log_event(log, self.user)
                callback(onaccept, form)
                if not next:
                    next = self.url(args=request.args)
                else:
                    next = replace_id(next, form)
                redirect(next, client_side=self.settings.client_side)
        return form

    def profile(self,
                next=DEFAULT,
                onvalidation=DEFAULT,
                onaccept=DEFAULT,
                log=DEFAULT,
                ):
        """
        Returns a form that lets the user change his/her profile
        """

        table_user = self.table_user()
        if not self.is_logged_in():
            redirect(self.settings.login_url,
                     client_side=self.settings.client_side)
        passfield = self.settings.password_field
        table_user[passfield].writable = False
        request = current.request
        session = current.session
        if next is DEFAULT:
            next = self.get_vars_next() or self.settings.profile_next
        if onvalidation is DEFAULT:
            onvalidation = self.settings.profile_onvalidation
        if onaccept is DEFAULT:
            onaccept = self.settings.profile_onaccept
        if log is DEFAULT:
            log = self.messages['profile_log']
        fields=self.settings.profile_fields
        if fields:
            for field in table_user: field.writable = (field.name in fields)
        form = Form(
                table_user,
                self.user.id,
                hidden=dict(_next=next),
                #showid=self.settings.showid,
                #submit_button=self.messages.profile_save_button,
                #delete_label=self.messages.delete_label,
                #upload=self.settings.download_url,
                #formstyle=self.settings.formstyle,
                #separator=self.settings.label_separator,
                deletable=self.settings.allow_delete_accounts,
            )
        if form.accepted:
            self.user.update(table_user._filter_fields(form.vars))
            session.flash = self.messages.profile_updated
            self.log_event(log, self.user)
            callback(onaccept, form)
            if form.deleted:
                return self.logout()
            if not next:
                next = self.url(args=request.args)
            else:
                next = replace_id(next, form)
            redirect(next, client_side=self.settings.client_side)
        return form

    def run_login_onaccept(self):
        onaccept = self.settings.login_onaccept
        if onaccept:
            form = Storage(dict(vars=self.user))
            if not isinstance(onaccept, (list, tuple)):
                onaccept = [onaccept]
            for callback in onaccept:
                callback(form)

    def jwt(self):
        """
        To use JWT authentication:
        1) instantiate auth with

            auth = Auth(db, jwt = {'secret_key':'secret'})

        where 'secret' is your own secret string. 

        2) Secorate functions that require login but should accept the JWT token credentials:

            @auth.allows_jwt()
            @auth.requires_login()
            def myapi(): return 'hello %s' % auth.user.email
    
        Notice jwt is allowed but not required. if user is logged in, myapi is accessible.

        3) Use it!

        Now API users can obtain a token with

            http://.../app/default/user/jwt?username=...&password=....

        (returns json object with a token attribute)
        API users can refresh an existing token with

            http://.../app/default/user/jwt?token=...

        they can authenticate themselves when calling http:/.../myapi by injecting a header

            Authorization: Bearer <the jwt token>

        Any additional attributes in the jwt argument of Auth() below:

           auth = Auth(db, jwt = {...})

        are passed to the constructor of class AuthJWT. Look there for documentation.
        """
        if not self.jwt_handler:
            raise HTTP(400, "Not authorized")
        else:
            current.response.headers['content-type'] = 'application/json'
            raise HTTP(200, self.jwt_handler.jwt_token_manager())
        
    def is_impersonating(self):
        return self.is_logged_in() and 'impersonator' in current.session.auth

    def impersonate(self, user_id=DEFAULT):
        """
        To use this make a POST to
        `http://..../impersonate request.post_vars.user_id=<id>`

        Set request.post_vars.user_id to 0 to restore original user.

        requires impersonator is logged in and::

            has_permission('impersonate', 'auth_user', user_id)

        """
        request = current.request
        session = current.session
        auth = session.auth
        table_user = self.table_user()
        if not self.is_logged_in():
            raise HTTP(401, "Not Authorized")
        current_id = auth.user.id
        requested_id = user_id
        if user_id is DEFAULT:
            user_id = current.request.post_vars.user_id
        if user_id and user_id != self.user.id and user_id != '0':
            if not self.has_permission('impersonate',
                                       self.table_user(),
                                       user_id):
                raise HTTP(403, "Forbidden")
            user = table_user(user_id)
            if not user:
                raise HTTP(401, "Not Authorized")
            auth.impersonator = pickle.dumps(session, pickle.HIGHEST_PROTOCOL)
            auth.user.update(
                table_user._filter_fields(user, True))
            self.user = auth.user
            self.update_groups()
            log = self.messages['impersonate_log']
            self.log_event(log, dict(id=current_id, other_id=auth.user.id))
            self.run_login_onaccept()
        elif user_id in (0, '0'):
            if self.is_impersonating():
                session.clear()
                session.update(pickle.loads(auth.impersonator))
                self.user = session.auth.user
                self.update_groups()
                self.run_login_onaccept()
            return None
        if requested_id is DEFAULT and not request.post_vars:
            return Form([Field('user_id', 'integer')])
        return Form(table_user, user.id, readonly=True)

    def update_groups(self):
        if not self.user:
            return
        user_groups = self.user_groups = {}
        if current.session.auth:
            current.session.auth.user_groups = self.user_groups
        table_group = self.table_group()
        table_membership = self.table_membership()
        memberships = self.db(
            table_membership.user_id == self.user.id).select()
        for membership in memberships:
            group = table_group(membership.group_id)
            if group:
                user_groups[membership.group_id] = group.role

    def groups(self):
        """
        Displays the groups and their roles for the logged in user
        """

        if not self.is_logged_in():
            redirect(self.settings.login_url)
        table_membership = self.table_membership()
        memberships = self.db(
            table_membership.user_id == self.user.id).select()
        table = TABLE()
        for membership in memberships:
            table_group = self.table_group()
            groups = self.db(table_group.id == membership.group_id).select()
            if groups:
                group = groups[0]
                table.append(TR(H3(group.role, '(%s)' % group.id)))
                table.append(TR(P(group.description)))
        if not memberships:
            return None
        return table

    def not_authorized(self):
        """
        You can change the view for this page to make it look as you like
        """
        if current.request.is_ajax:
            raise HTTP(403, 'ACCESS DENIED')
        return self.messages.access_denied

    def allows_jwt(self, otherwise=None):
        if not self.jwt_handler:
            raise HTTP(400, "Not authorized")
        else:
            return self.jwt_handler.allows_jwt()

    def requires(self, condition, requires_login=True, otherwise=None):
        """
        Decorator that prevents access to action if not logged in
        """

        def decorator(action):

            def f(*a, **b):

                basic_allowed, basic_accepted, user = self.basic()
                user = user or self.user

                login_required = requires_login
                if callable(login_required):
                    login_required = login_required()

                if login_required:
                    if not user:
                        if current.request.is_ajax:
                            raise HTTP(401, self.messages.ajax_failed_authentication)
                        elif not otherwise is None:
                            if callable(otherwise):
                                return otherwise()
                            redirect(otherwise)
                        elif self.settings.allow_basic_login_only or \
                                basic_accepted or current.request.is_restful:
                            raise HTTP(403, "Not authorized")
                        else:
                            next = self.here()
                            current.session.flash = current.response.flash
                            return call_or_redirect(
                                self.settings.on_failed_authentication,
                                self.settings.login_url +
                                    '?_next=' + urllib.quote(next))

                if callable(condition):
                    flag = condition()
                else:
                    flag = condition
                if not flag:
                    current.session.flash = self.messages.access_denied
                    return call_or_redirect(
                        self.settings.on_failed_authorization)
                return action(*a, **b)
            f.__doc__ = action.__doc__
            f.__name__ = action.__name__
            f.__dict__.update(action.__dict__)
            return f

        return decorator

    def requires_login(self, otherwise=None):
        """
        Decorator that prevents access to action if not logged in
        """
        return self.requires(True, otherwise=otherwise)

    def requires_login_or_token(self, otherwise=None):
        if self.settings.enable_tokens == True:
            user = None
            request = current.request
            token = request.env.http_web2py_user_token or request.vars._token
            table_token = self.table_token()
            table_user = self.table_user()
            #from gluon.settings import global_settings
            if False: # FIX THIS global_settings.web2py_runtime_gae:
                row = table_token(token=token)
                if row:
                    user = table_user(row.user_id)
            else:
                row = self.db(table_token.token == token)(table_user.id == table_token.user_id).select().first()
                if row:
                    user = row[table_user._tablename]
            if user:
                self.login_user(user)
        return self.requires(True, otherwise=otherwise)

    def requires_membership(self, role=None, group_id=None, otherwise=None):
        """
        Decorator that prevents access to action if not logged in or
        if user logged in is not a member of group_id.
        If role is provided instead of group_id then the
        group_id is calculated.
        """
        def has_membership(self=self, group_id=group_id, role=role):
            return self.has_membership(group_id=group_id, role=role)
        return self.requires(has_membership, otherwise=otherwise)

    def requires_permission(self, name, table_name='', record_id=0,
                            otherwise=None):
        """
        Decorator that prevents access to action if not logged in or
        if user logged in is not a member of any group (role) that
        has 'name' access to 'table_name', 'record_id'.
        """
        def has_permission(self=self, name=name, table_name=table_name, record_id=record_id):
            return self.has_permission(name, table_name, record_id)
        return self.requires(has_permission, otherwise=otherwise)

    def requires_signature(self, otherwise=None, hash_vars=True):
        """
        Decorator that prevents access to action if not logged in or
        if user logged in is not a member of group_id.
        If role is provided instead of group_id then the
        group_id is calculated.
        """
        def verify():
            return URL.verify(current.request, user_signature=True, hash_vars=hash_vars)
        return self.requires(verify, otherwise)

    def add_group(self, role, description=''):
        """
        Creates a group associated to a role
        """

        group_id = self.table_group().insert(
            role=role, description=description)
        self.log_event(self.messages['add_group_log'],
                       dict(group_id=group_id, role=role))
        return group_id

    def del_group(self, group_id):
        """
        Deletes a group
        """
        self.db(self.table_group().id == group_id).delete()
        self.db(self.table_membership().group_id == group_id).delete()
        self.db(self.table_permission().group_id == group_id).delete()
        if group_id in self.user_groups: del self.user_groups[group_id]
        self.log_event(self.messages.del_group_log, dict(group_id=group_id))

    def id_group(self, role):
        """
        Returns the group_id of the group specified by the role
        """
        rows = self.db(self.table_group().role == role).select()
        if not rows:
            return None
        return rows[0].id

    def user_group(self, user_id=None):
        """
        Returns the group_id of the group uniquely associated to this user
        i.e. `role=user:[user_id]`
        """
        return self.id_group(self.user_group_role(user_id))

    def user_group_role(self, user_id=None):
        if not self.settings.create_user_groups:
            return None
        if user_id:
            user = self.table_user()[user_id]
        else:
            user = self.user
        return self.settings.create_user_groups % user

    def has_membership(self, group_id=None, user_id=None, role=None):
        """
        Checks if user is member of group_id or role
        """

        group_id = group_id or self.id_group(role)
        try:
            group_id = int(group_id)
        except:
            group_id = self.id_group(group_id)  # interpret group_id as a role
        if not user_id and self.user:
            user_id = self.user.id
        membership = self.table_membership()
        if group_id and user_id and self.db((membership.user_id == user_id)
                    & (membership.group_id == group_id)).select():
            r = True
        else:
            r = False
        self.log_event(self.messages['has_membership_log'],
                       dict(user_id=user_id, group_id=group_id, check=r))
        return r

    def add_membership(self, group_id=None, user_id=None, role=None):
        """
        Gives user_id membership of group_id or role
        if user is None than user_id is that of current logged in user
        """

        group_id = group_id or self.id_group(role)
        try:
            group_id = int(group_id)
        except:
            group_id = self.id_group(group_id)  # interpret group_id as a role
        if not user_id and self.user:
            user_id = self.user.id
        membership = self.table_membership()
        db = membership._db
        record = db((membership.user_id==user_id)&
                    (membership.group_id==group_id),
                    ignore_common_filters=True).select().first()
        if record:
            if hasattr(record, 'is_active') and not record.is_active:
                record.update_record(is_active=True)
            return record.id
        else:
            id = membership.insert(group_id=group_id, user_id=user_id)
        if role:
            self.user_groups[group_id] = role
        else:
            self.update_groups()
        self.log_event(self.messages['add_membership_log'],
                       dict(user_id=user_id, group_id=group_id))
        return id

    def del_membership(self, group_id=None, user_id=None, role=None):
        """
        Revokes membership from group_id to user_id
        if user_id is None than user_id is that of current logged in user
        """

        group_id = group_id or self.id_group(role)
        if not user_id and self.user:
            user_id = self.user.id
        membership = self.table_membership()
        self.log_event(self.messages['del_membership_log'],
                       dict(user_id=user_id, group_id=group_id))
        ret = self.db(membership.user_id
                      == user_id)(membership.group_id
                                  == group_id).delete()
        if group_id in self.user_groups: del self.user_groups[group_id]
        return ret

    def has_permission(self,
                       name='any',
                       table_name='',
                       record_id=0,
                       user_id=None,
                       group_id=None,
                       ):
        """
        Checks if user_id or current logged in user is member of a group
        that has 'name' permission on 'table_name' and 'record_id'
        if group_id is passed, it checks whether the group has the permission
        """

        if not group_id and self.settings.everybody_group_id and \
                self.has_permission(
            name, table_name, record_id, user_id=None,
            group_id=self.settings.everybody_group_id):
                return True

        if not user_id and not group_id and self.user:
            user_id = self.user.id
        if user_id:
            membership = self.table_membership()
            rows = self.db(membership.user_id
                           == user_id).select(membership.group_id)
            groups = set([row.group_id for row in rows])
            if group_id and group_id not in groups:
                return False
        else:
            groups = set([group_id])
        permission = self.table_permission()
        rows = self.db(permission.name == name)(permission.table_name
                 == str(table_name))(permission.record_id
                 == record_id).select(permission.group_id)
        groups_required = set([row.group_id for row in rows])
        if record_id:
            rows = self.db(permission.name
                            == name)(permission.table_name
                     == str(table_name))(permission.record_id
                     == 0).select(permission.group_id)
            groups_required = groups_required.union(set([row.group_id
                    for row in rows]))
        if groups.intersection(groups_required):
            r = True
        else:
            r = False
        if user_id:
            self.log_event(self.messages['has_permission_log'],
                           dict(user_id=user_id, name=name,
                                table_name=table_name, record_id=record_id))
        return r

    def add_permission(self,
                       group_id,
                       name='any',
                       table_name='',
                       record_id=0,
                       ):
        """
        Gives group_id 'name' access to 'table_name' and 'record_id'
        """

        permission = self.table_permission()
        if group_id == 0:
            group_id = self.user_group()
        record = self.db((permission.group_id == group_id)&
                         (permission.name == name)&
                         (permission.table_name == str(table_name))&
                         (permission.record_id == long(record_id)),
                          ignore_common_filters=True).select(
            limitby=(0, 1), orderby_on_limitby=False).first()
        if record:
            if hasattr(record, 'is_active') and not record.is_ctive:
                record.update_record(is_active=True)
            id = record.id
        else:
            id = permission.insert(group_id=group_id, name=name,
                                   table_name=str(table_name),
                                   record_id=long(record_id))
        self.log_event(self.messages['add_permission_log'],
                       dict(permission_id=id, group_id=group_id,
                            name=name, table_name=table_name,
                            record_id=record_id))
        return id

    def del_permission(self,
                       group_id,
                       name='any',
                       table_name='',
                       record_id=0,
                       ):
        """
        Revokes group_id 'name' access to 'table_name' and 'record_id'
        """

        permission = self.table_permission()
        self.log_event(self.messages['del_permission_log'],
                       dict(group_id=group_id, name=name,
                            table_name=table_name, record_id=record_id))
        return self.db(permission.group_id == group_id)(permission.name
                 == name)(permission.table_name
                           == str(table_name))(permission.record_id
                 == long(record_id)).delete()

    def accessible_query(self, name, table, user_id=None):
        """
        Returns a query with all accessible records for user_id or
        the current logged in user
        this method does not work on GAE because uses JOIN and IN

        Example:
            Use as::

                db(auth.accessible_query('read', db.mytable)).select(db.mytable.ALL)

        """
        if not user_id:
            user_id = self.user_id
        db = self.db
        if isinstance(table, str) and table in self.db.tables():
            table = self.db[table]
        elif isinstance(table, (Set, Query)):
            # experimental: build a chained query for all tables
            if isinstance(table, Set):
                cquery = table.query
            else:
                cquery = table
            tablenames = db._adapter.tables(cquery)
            for tablename in tablenames:
                cquery &= self.accessible_query(name, tablename,
                                                user_id=user_id)
            return cquery
        if not isinstance(table, str) and\
                self.has_permission(name, table, 0, user_id):
            return table.id > 0
        membership = self.table_membership()
        permission = self.table_permission()
        query = table.id.belongs(
            db(membership.user_id == user_id)
                (membership.group_id == permission.group_id)
                (permission.name == name)
                (permission.table_name == table)
                ._select(permission.record_id))
        if self.settings.everybody_group_id:
            query |= table.id.belongs(
                db(permission.group_id == self.settings.everybody_group_id)
                    (permission.name == name)
                    (permission.table_name == table)
                    ._select(permission.record_id))
        return query

    @staticmethod
    def archive(form,
                archive_table=None,
                current_record='current_record',
                archive_current=False,
                fields=None):
        """
        If you have a table (db.mytable) that needs full revision history you
        can just do::

            form=crud.update(db.mytable,myrecord,onaccept=auth.archive)

        or::

            form=Form(db.mytable,myrecord)
            if form.accepted: auth.archive(form)

        crud.archive will define a new table "mytable_archive" and store
        a copy of the current record (if archive_current=True)
        or a copy of the previous record (if archive_current=False)
        in the newly created table including a reference
        to the current record.

        fields allows to specify extra fields that need to be archived.

        If you want to access such table you need to define it yourself
        in a model::

            db.define_table('mytable_archive',
                Field('current_record',db.mytable),
                db.mytable)

        Notice such table includes all fields of db.mytable plus one: current_record.
        crud.archive does not timestamp the stored record unless your original table
        has a fields like::

            db.define_table(...,
                Field('saved_on','datetime',
                     default=request.now,update=request.now,writable=False),
                Field('saved_by',auth.user,
                     default=auth.user_id,update=auth.user_id,writable=False),

        there is nothing special about these fields since they are filled before
        the record is archived.

        If you want to change the archive table name and the name of the reference field
        you can do, for example::

            db.define_table('myhistory',
                Field('parent_record',db.mytable),
                db.mytable)

        and use it as::

            form=crud.update(db.mytable,myrecord,
                             onaccept=lambda form:crud.archive(form,
                             archive_table=db.myhistory,
                             current_record='parent_record'))

        """
        if not archive_current and not form.record:
            return None
        table = form.table
        if not archive_table:
            archive_table_name = '%s_archive' % table
            if not archive_table_name in table._db:
                table._db.define_table(
                    archive_table_name,
                    Field(current_record, table),
                    *[field.clone(unique=False) for field in table])
            archive_table = table._db[archive_table_name]
        new_record = {current_record: form.vars.id}
        for fieldname in archive_table.fields:
            if not fieldname in ['id', current_record]:
                if archive_current and fieldname in form.vars:
                    new_record[fieldname] = form.vars[fieldname]
                elif form.record and fieldname in form.record:
                    new_record[fieldname] = form.record[fieldname]
        if fields:
            new_record.update(fields)
        id = archive_table.insert(**new_record)
        return id

