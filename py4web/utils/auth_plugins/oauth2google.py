from . import OAuth2


class OAuth2Google(OAuth2):
    name = "oauth2google"
    login_url = "https://accounts.google.com/o/oauth2/v2/auth"
    token_url = "https://www.googleapis.com/oauth2/v4/token"
    userinfo_url = "https://www.googleapis.com/plus/v1/people/me"
    revoke_url = "https://accounts.google.com/o/oauth2/revoke"
    default_scope = "email"
    maps = {
        "email": "emails.0.value",
        "sso_id": "id",
        "first_name": "name.givenName",
        "last_name": "name.familyName",
    }
