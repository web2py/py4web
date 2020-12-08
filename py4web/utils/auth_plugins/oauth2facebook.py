from . import OAuth2


class OAuth2Facebook(OAuth2):
    name = "oauth2facebook"
    label = "Facebook"

    login_url = "https://www.facebook.com/v3.3/dialog/oauth"
    token_url = "https://graph.facebook.com/v3.3/oauth/access_token"
    userinfo_url = "https://graph.facebook.com/me?fields=id,email,first_name,last_name"
    revoke_url = "https://accounts.google.com/me/permissions"
    default_scope = None
    maps = {
        "email": "email",
        "sso_id": "id",
        "first_name": "first_name",
        "last_name": "last_name",
    }

    def revoke(self, token):
        requests.delete(self.revoke_url, headers={"Authorization": token})
