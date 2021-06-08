from . import OAuth2


class OAuth2Google(OAuth2):
    name = "oauth2google"
    label = "Google"

    login_url = "https://accounts.google.com/o/oauth2/v2/auth"
    token_url = "https://oauth2.googleapis.com/token"
    userinfo_url = "https://www.googleapis.com/oauth2/v3/userinfo"
    revoke_url = "https://accounts.google.com/o/oauth2/revoke"
    default_scope = "email profile"
    maps = {
        "email": "email",
        "sso_id": "sub",
        "first_name": "given_name",
        "last_name": "family_name",
    }
