from yatl.helpers import XML

from py4web import Field, action
from py4web.utils.form import Form

from ..common import session
from ..settings import HCAPTCHA_SITE_KEY, SESSION_SECRET_KEY


@action("hcaptcha_form")
@action.uses("hcaptcha_form.html", session)
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
