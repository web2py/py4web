import requests
from yatl.helpers import XML

from py4web import Field, action, request
from py4web.utils.form import Form

from .common import session
from .settings import (HCAPTCHA_SECRET_KEY, HCAPTCHA_SITE_KEY,
                       HCAPTCHA_VERIFY_URL)


def hCaptcha(token):

    # Retrieve token from post data with key 'h-captcha-response'.

    # Build payload with secret key and token.
    data = {"secret": HCAPTCHA_SECRET_KEY, "response": token}

    # Make POST request with data payload to hCaptcha API endpoint.
    response = requests.post(url=HCAPTCHA_VERIFY_URL, data=data)

    # Parse JSON from response. Check for success or error codes.
    response_json = response.json()
    success = response_json["success"]

    return success


@action("hcaptcha_form")
@action.uses("examples/hcaptcha_form.html", session)
def hcaptcha_form():

    form = Form(
        [
            Field(
                "dummy_form",
                "string",
            )
        ]
    )

    form.structure.append(
        XML('<div class="h-captcha" data-sitekey="{}"></div>'.format(HCAPTCHA_SITE_KEY))
    )
    if form.accepted:
        r = hCaptcha(request.forms.get("g-recaptcha-response"))
        if r == True:
            # do something with form data
            form.structure.append(
                XML(
                    '<div style="color:green">Captcha was solved succesfully!</font></div>'
                )
            )
        else:
            form.structure.append(
                XML('<div class="py4web-validation-error">invalid captcha</div>')
            )

    return dict(form=form)
