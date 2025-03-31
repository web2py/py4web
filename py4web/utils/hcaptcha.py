import requests
from yatl.helpers import XML

from py4web.core import Field, Fixture, request


class hcaptcha_fixture(Fixture):
    def __init__(self, site_key, secret_key):
        self.site_key = site_key
        self.secret_key = secret_key

        Fixture.__init__(self)

    def on_request(self, context):
        value = request.POST.get("h-captcha-response")
        if value:
            request.POST["h_captcha_response"] = value
            del request.POST["h-captcha-response"]

    def on_success(self, context):
        if context:
            hcaptcha_script = "".join(
                map(
                    lambda line: line.strip(),
                    """<script>
                    
            hcaptcha_div = document.createElement('div');
            input = document.getElementById("no_table_h_captcha_response");
            let label = document.querySelector('label[for="no_table_h_captcha_response"]');
            label.hidden = true;
          
            input.hidden = true;
            hcaptcha_div.setAttribute("data-sitekey", "%s");
            hcaptcha_div.classList.add("h-captcha");
            var form =  document.querySelector("form");
            form.appendChild(hcaptcha_div);
            var button = form.querySelector("input[type=submit]");
             if (window.location.href.endsWith('/auth/register')) {
                form.insertBefore(hcaptcha_div, form.childNodes[5]);
                }
              else if (window.location.href.endsWith('/auth/request_reset_password')) {
                form.insertBefore(hcaptcha_div, form.childNodes[2]);
                }
              else {
                form.insertBefore(hcaptcha_div, form.childNodes[4]);
              }
            window.hcaptcha_submit = function(token){ form.submit(); };
            </script>
            <script src="https://js.hcaptcha.com/1/api.js" async defer></script>
            """.split("\n"),
                )
            )

            if context["output"] is None:
                context["output"] = {}
            context["output"]["hcaptcha"] = XML(hcaptcha_script % self.site_key)


class Hcaptcha:
    def __init__(self, site_key, secret_key):
        self.site_key = site_key
        self.secret_key = secret_key

    @property
    def fixture(self):
        return hcaptcha_fixture(self.site_key, self.secret_key)

    @property
    def field(self):
        return Field("h_captcha_response", "hidden", requires=self.validator)

    def validator(self, value, _):
        print(value)
        print(self.secret_key)
        # Build payload with secret key and token.
        data = {"secret": self.secret_key, "response": value}

        # Make POST request with data payload to hCaptcha API endpoint.
        res = requests.post(url="https://hcaptcha.com/siteverify", data=data)
        print(res.text)
        try:
            if res.json()["success"]:
                return (True, None)
            return (False, "Invalid Hcaptcha value")
        except Exception as exc:
            print(exc)
            return (False, str(exc))
