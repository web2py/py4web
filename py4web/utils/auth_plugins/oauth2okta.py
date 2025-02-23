from . import OAuth2


class OAuth2Okta(OAuth2):
    name = "oauth2okta"
    label = "Okta"

    login_url = "https://XXX.okta.com/oauth2/default/v1/authorize"
    token_url = "https://XXX.okta.com/oauth2/default/v1/token"
    userinfo_url = "https://XXX.okta.com/oauth2/default/v1/revoke"
    revoke_url = "https://XXX.okta.com/oauth2/default/v1/userinfo"
    default_scope = "openid profile"
    maps = {
        "username": "sub",
        "email": "sub",
        "sso_id": "sub",
    }

    def is_auth_compatible(self, auth):
        if not auth.use_username:
            return False, "requires auth.use_username = True"
        return super().is_auth_compatible(auth)
