# from https://requests-oauthlib.readthedocs.io/en/latest/examples/github.html


from . import OAuth2


class OAuth2Github(OAuth2):
    name = "oauth2github"
    label = "Github"

    login_url = "https://github.com/login/oauth/authorize"
    token_url = "https://github.com/login/oauth/access_token"
    userinfo_url = "https://api.github.com/user"
    default_scope = None
    maps = {
        "username": "login",
        "email": "email",
        "sso_id": "url",
    }
