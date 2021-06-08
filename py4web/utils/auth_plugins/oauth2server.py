import uuid
import hashlib
import jwt

from py4web.core import request, abort, DAL, Field


class OAuthServer(object):

    algorithms = ["HS256", "RS256"]

    def __init__(self, auth, secret):
        self.secret = secret
        self.auth = auth
        self.define_tables()

    def define_tables(self):
        db = self.auth.db
        db.define_table(
            "oauth2",
            Field("registrant_id", "reference auth_user"),
            Field("client_secret"),
        )
        db.commit()

    def register_new_client(self, registrant_id):
        client_secret = str(uuid.uuid4())
        self.auth.db.oauth2.insert(
            registrant_id=registrant_id, client_secret=client_secret
        )

    def handle_request(self, auth, path, get_vars, post_vars):
        if path == "login":
            # WIP
            client_id = request.get("client_id")
            info = {}  # retrieve the user info upon login
            code = jwt.encode(info, self.secret + client_id, algorithm="HS256")
        elif path == "callback":
            db = self.auth.db
            code = (get_vars.get("code"),)
            client_id = (get_vars.get("client_id"),)
            client_secret = (get_vars.get("client_secret"),)
            redirect_uri = (get_vars.get("callback_url"),)
            grant_type = get_vars.get("grant_type")
            if (
                not grant_type == "authorization_code"
                or not hashlib.sha1(client_secret).hexdigest() == client_id
                or not db(db.oauth2.client_secret == client_secret).count()
            ):
                abort(404)
            info = jwt.decode(code, self.secret + client_id, algorithms=["HS256"])
            access_token = jwt.encode(info, self.secret, algorithm="HS256")
            return dict(access_token=access_token)
        elif path == "profile":
            access_token = request.environ.get("HTTP_AUTHORIZATION", "")[7:]
            info = jwt.decode(access_token, self.secret, algorithms=self.algorithms)
            return info
        else:
            abort(404)
