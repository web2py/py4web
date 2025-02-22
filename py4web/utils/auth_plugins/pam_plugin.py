from .pam import authenticate


class PamPlugin:
    name = "pam"
    label = "Pam"

    def is_auth_compatible(self, auth):
        if not auth.use_username:
            return False, "requires auth.use_username = True"
        return True, ""

    def check_credentials(self, username, password):
        return authenticate(username, password)
