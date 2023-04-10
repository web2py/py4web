from .pam import authenticate


class PamPlugin:

    name = "pam"
    label = "Pam"

    def check_credentials(self, username, password):
        return authenticate(username, password)
