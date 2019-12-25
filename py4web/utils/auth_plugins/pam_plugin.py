from .pam import authenticate


class PamPlugin:

    name = "pam"

    def check_credentials(self, username, password):
        return authenticate(username, password)
