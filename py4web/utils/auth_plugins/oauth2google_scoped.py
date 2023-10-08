# This is a version of google login that also enables the use of other
# authenticatio scopes (e.g., Google Drive, etc).  The credentials for the
# scopes are stored, so that the application can access them and use to
# operate on the scopes (e.g., create files on Google Drive on behalf of
# the user).
# See https://developers.google.com/identity/protocols/oauth2/web-server#python

import calendar
import json
import time
import uuid

import google_auth_oauthlib.flow
import google.oauth2.credentials
from googleapiclient.discovery import build

from py4web import request, redirect, URL, HTTP
from pydal import Field

class OAuth2GoogleScoped(object):
    """Class that enables google login via oauth2 with additional scopes.
    The authorization info is saved so the scopes can be used later on."""

    # These values are used for the plugin registration.
    name = "oauth2googlescoped"
    label = "Google Scoped"
    callback_url = "auth/plugin/oauth2googlescoped/callback"

    def __init__(self, secrets_file=None, scopes=None, db=None,
                 define_tables=True, delete_credentials_on_logout=True):
        """
        Creates an authorization object for Google with Oauth2 and paramters.

        There are some differences between this plugin and other Oauth2 plugins:
        - The plugin uses the database, and creates an auth_credentials table to
          store the credentials for the scopes requested.
        - The plugin relies on some google libraries (see on top), so these
          need to be installed.
        - The plugin takes in input a .json credentials file that can be
          downloaded from Google Cloud when creating the OAuth2 credentials.
        Args:
            secrets_file: file with secrets for Oauth2.
            scopes: scopes desired.
                See https://developers.google.com/drive/api/guides/api-specific-auth
                and https://developers.google.com/identity/protocols/oauth2/scopes
            db: Database handle.
            define_tables: Define the tables for storing credentials?
            delete_credentials_on_logout: if True, the credentials are cleared
                when the user logs out.  If False, the app keeps a copy of the
                credentials, so it can do work on behalf of the user using
                those credentials after logout.  This can obviously
                generate security concerns.
        """

        # Local secrets to be able to access.
        assert secrets_file is not None, "Missing secrets file"
        self._secrets_file = secrets_file
        # Scopes for which we ask authorization
        scopes = scopes or []
        self._scopes = ["openid",
                       "https://www.googleapis.com/auth/userinfo.email",
                       "https://www.googleapis.com/auth/userinfo.profile"] + scopes
        self._db = db
        if db and define_tables:
            self._define_tables()
            self._delete_credentials_on_logout = delete_credentials_on_logout


    def _define_tables(self):
        self._db.define_table('auth_credentials', [
            Field('email'),
            Field('name'), # First and last names, all together.
            Field('profile_pic'), # URL of profile pic.
            Field('credentials', 'text') # Credentials for access, stored in Json for generality.
        ])


    def handle_request(self, auth, path, get_vars, post_vars):
        """Handles the login request or the callback."""
        if path == "login":
            auth.session["_next"] = request.query.get("next") or URL("index")
            redirect(self._get_login_url(auth))
        elif path == "callback":
            self._handle_callback(auth, get_vars)
        elif path == "logout":
            # Deletes the credentials, and clears the session.
            if self._delete_credentials_on_logout:
                email = auth.current_user.get('email') if auth.current_user else None
                if email is not None:
                    self._db(self._db.auth_credentials.email == email).delete()
                    self._db.commit()
            auth.session.clear()
            next = request.query.get("next") or URL("index")
            redirect(next)
        else:
            raise HTTP(404)


    def _get_login_url(self, auth, state=None):
        # Creates a flow.
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            self._secrets_file, scopes=self._scopes)
        # Sets its callback URL.  This is the local URL that will be called
        # once the user gives permission.
        """Returns the URL to which the user is directed."""
        flow.redirect_uri = URL(self.callback_url, scheme=True)
        authorization_url, state = flow.authorization_url(
            # Enable offline access so that you can refresh an access token without
            # re-prompting the user for permission. Recommended for web server apps.
            access_type='offline',
            # Enable incremental authorization. Recommended as a best practice.
            include_granted_scopes='true')
        auth.session["oauth2googlescoped:state"] = state
        return authorization_url

    def _handle_callback(self, auth, get_vars):
        # Builds a flow again, this time with the state in it.
        state = auth.session["oauth2googlescoped:state"]
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            self._secrets_file, scopes=self._scopes, state=state)
        flow.redirect_uri = URL(self.callback_url, scheme=True)
        # Use the authorization server's response to fetch the OAuth 2.0 tokens.
        if state and get_vars.get('state', None) != state:
            raise HTTP(401, "Invalid state")
        error = get_vars.get("error")
        if error:
            if isinstance(error, str):
                code, msg = 401, error
            else:
                code = error.get("code", 401)
                msg = error.get("message", "Unknown error")
            raise HTTP(code, msg)
        if not 'code' in get_vars:
            raise HTTP(401, "Missing code parameter in response.")
        code = get_vars.get('code')
        flow.fetch_token(code=code)
        # We got the credentials!
        credentials = flow.credentials
        # Now we must use the credentials to check the user identity.
        # see https://github.com/googleapis/google-api-python-client/pull/1088/files
        # and https://github.com/googleapis/google-api-python-client/issues/1071
        # and ??
        user_info_service = build('oauth2', 'v2', credentials=credentials)
        user_info = user_info_service.userinfo().get().execute()
        email = user_info.get("email")
        if email is None:
            raise HTTP(401, "Missing email")
        # Finally, we store the credentials, so we can re-use them in order
        # to use the scopes we requested.
        if self._db:
            credentials_json=json.dumps(self.credentials_to_dict(credentials))
            self._db.auth_credentials.update_or_insert(
                self._db.auth_credentials.email == email,
                email=email,
                name=user_info.get("name"),
                credentials=credentials_json,
                profile_pic=user_info.get("picture"),
            )
            self._db.commit()
        # Logs in the user.
        if auth.db:
            user = {
                "email": user_info.get("email"),
                "first_name": user_info.get("given_name"),
                "last_name": user_info.get("family_name"),
            }
            data = auth.get_or_register_user(user)
            user["id"] = data.get("id")
        else:
            # WIP Allow login without DB
            user = dict(user_info)
            if not "id" in user:
                user["id"] = user.get("username") or user.get("email")
        # Stores the user in the session.  We do it here, so we store
        # the complete details, and not just the user_id.
        auth.session["user"] = user
        auth.session["recent_activity"] = calendar.timegm(time.gmtime())
        auth.session["uuid"] = str(uuid.uuid1())
        # Finally, redirects to next.
        if "_next" in auth.session:
            next = auth.session.get("_next")
            del auth.session["_next"]
        else:
            next = URL("index")
        redirect(next)


    @staticmethod
    def credentials_to_dict(credentials):
        return {'token': credentials.token,
                'refresh_token': credentials.refresh_token,
                'token_uri': credentials.token_uri,
                'client_id': credentials.client_id,
                'client_secret': credentials.client_secret,
                'scopes': credentials._scopes}

    @staticmethod
    def credentials_from_dict(credentials_dict):
        return google.oauth2.credentials.Credentials(**credentials_dict)
