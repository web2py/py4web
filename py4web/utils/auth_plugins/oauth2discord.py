from . import OAuth2


class OAuth2Discord(OAuth2):
    """
    This plugin is designed to allow usage of Discord as an OAuth2 provider.

    Example usage to register plugin:

    auth.register_plugin(
        OAuth2Discord(
            client_id=<DISCORD_CLIENT_ID>,
            client_secret=<DISCORD_CLIENT_SECRET>,
            callback_url="auth/plugin/oauth2discord/callback",
        )
    )

    To obtain a Discord client ID and secret, create an application at https://discord.com/developers/applications.
    You will also have to register your OAuth2 redirect URI in your created application:
    http(s)://<your host>/<your app name>/auth/plugin/oauth2discord/callback

    Note that as Discord users have no concept of first/last name, the user in the auth table will contain the
    Discord username as the first name and discriminator as the last name.
    """

    name = "oauth2discord"
    label = "Discord"

    login_url = "https://discord.com/api/oauth2/authorize"
    token_url = "https://discord.com/api/oauth2/token"
    userinfo_url = "https://discord.com/api/v8/users/@me"
    revoke_url = "https://discord.com/api/oauth2/token/revoke"
    default_scope = "identify email"
    maps = {
        "email": "email",
        "sso_id": "id",
        "first_name": "username",
        "last_name": "discriminator",
        "username": "full_username",
    }

    def callback(self, query):
        # since Discord returns username and discriminator separately, we extend the auth plugin's callback
        # function to merge them into a single field, so it can be mapped into username correctly later
        data = super().callback(query)
        data["full_username"] = f"{data['username']}#{data['discriminator']}"
        return data
