import requests
from yatl.helpers import XML

from py4web.core import Field, Fixture, request


class recaptcha_fixture(Fixture):
    def __init__(self, api_key, version):
        self.api_key = api_key
        self.version = version
        Fixture.__init__(self)

    def on_request(self, context):
        value = request.POST.get("g-recaptcha-response")
        if value:
            request.POST["g_recaptcha_response"] = value
            del request.POST["g-recaptcha-response"]

    def on_success(self, context):
        if context:
            script_v2 = "".join(
                map(
                    lambda line: line.strip(),
                    """<script>
            var field = document.querySelector("input[name=g_recaptcha_response]");
            var div_recaptcha = document.createElement("div");
            div_recaptcha.classList.add("g-recaptcha");
            div_recaptcha.setAttribute("id","g-recaptcha-div");
            div_recaptcha.setAttribute("data-sitekey","%s" );
            let current_url = window.location.href;
            
            if(field) {
              field.hidden = true;
              field.setAttribute("type", "hidden");
              let label = document.querySelector('label[for="no_table_g_recaptcha_response"]');
              label.hidden = true;
              var form =  document.querySelector("form");
              var button = form.querySelector("input[type=submit]");
              
              if (window.location.href.endsWith('/auth/register')) {
                form.insertBefore(div_recaptcha, form.childNodes[5]);
                }
              else if (window.location.href.endsWith('/auth/request_reset_password')) {
                form.insertBefore(div_recaptcha, form.childNodes[2]);
                }
              else {
                form.insertBefore(div_recaptcha, form.childNodes[4]);
              }
              
              window.recaptcha_submit = function(token){ form.submit(); };
           
            }
            </script>
            <script src="https://www.google.com/recaptcha/api.js" async defer></script>
            """.split("\n"),
                )
            )
            script_v3 = "".join(
                map(
                    lambda line: line.strip(),
                    """<script>
            var field = document.querySelector("input[name=g_recaptcha_response]");
            
            if(field) {
              field.hidden = true;
              field.setAttribute("type", "hidden");
              let label = document.querySelector('label[for="no_table_g_recaptcha_response"]');
              label.hidden = true;
              var form =  document.querySelector("form");
              var button = form.querySelector("input[type=submit]");
              window.recaptcha_submit = function(token){ form.submit(); };

              button.classList.add("g-recaptcha");
              button.setAttribute("data-action", "submit");
              button.setAttribute("data-callback", "recaptcha_submit");
              button.setAttribute("data-sitekey", "%s");
            
           
            }
            </script>
            <script src="https://www.google.com/recaptcha/api.js" async defer></script>
            """.split("\n"),
                )
            )
            if context["output"] is None:
                context["output"] = {}
            if self.version == "v2":
                context["output"]["recaptcha"] = XML(script_v2 % self.api_key)
            else:
                context["output"]["recaptcha"] = XML(script_v3 % self.api_key)


class ReCaptcha:
    def __init__(self, api_key, api_secret, version):
        self.api_key = api_key
        self.api_secret = api_secret
        self.version = version

    @property
    def fixture(self):
        return recaptcha_fixture(self.api_key, self.version)

    @property
    def field(self):
        return Field("g_recaptcha_response", "hidden", requires=self.validator)

    def validator(self, value, _):
        data = {"secret": self.api_secret, "response": value}
        res = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", data=data
        )
        try:
            if res.json()["success"] == True:
                return (True, None)

            return (False, "Please verify that you are not a robot")
        except Exception as exc:
            return (False, str(exc))
