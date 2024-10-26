import requests
from yatl.helpers import XML

from py4web.core import Field, Fixture, request


class recaptcha_fixture(Fixture):
    def __init__(self, api_key):
        self.api_key = api_key
        Fixture.__init__(self)

    def on_request(self, context):
        value = request.POST.get("g-recaptcha-response")
        if value:
            request.POST["g_recaptcha_response"] = value
            del request.POST["g-recaptcha-response"]

    def on_success(self, context):
        if context:
            script = "".join(
                map(
                    lambda line: line.strip(),
                    """<script>
            var field = document.querySelector("input[name=g_recaptcha_response]");
            if(field) {
              field.hidden = true;
              field.setAttribute("type", "hidden");           
              var form =  document.querySelector(".auth-container form");
              var button = form.querySelector("input[type=submit]");
              window.recaptcha_submit = function(token){ form.submit(); };
              button.classList.add("g-recaptcha");
              button.setAttribute("data-action", "submit");
              button.setAttribute("data-callback", "recaptcha_submit");
              button.setAttribute("data-sitekey", "%s");
            }
            </script>
            <script src="https://www.google.com/recaptcha/api.js"></script>
            """.split(
                        "\n"
                    ),
                )
            )
            if context["output"] is None:
                context["output"] = {}
            context["output"]["recaptcha"] = XML(script % self.api_key)


class ReCaptcha:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    @property
    def fixture(self):
        return recaptcha_fixture(self.api_key)

    @property
    def field(self):
        return Field("g_recaptcha_response", "hidden", requires=self.validator)

    def validator(self, value, _):
        data = {"secret": self.api_secret, "response": value}
        res = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", data=data
        )
        try:
            if res.json()["success"]:
                return (True, None)
            return (False, "Invalid ReCaptcha response")
        except Exception as exc:
            return (False, str(exc))
