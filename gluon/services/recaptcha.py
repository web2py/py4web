 gluon.tag import TAGGER

class Recaptcha(TAGGER):
    """
    Experimental:
    Creates a DIV holding the newer Recaptcha from Google (v2)

    Args:
        request : the request. If not passed, uses current request
        public_key : the public key Google gave you
        private_key : the private key Google gave you
        error_message : the error message to show if verification fails
        label : the label to use
        options (dict) : takes these parameters

            - hl
            - theme
            - type
            - tabindex
            - callback
            - expired-callback

            see https://developers.google.com/recaptcha/docs/display for docs about those

        comment : the comment

    Examples:
        Use as::

            form = FORM(Recaptcha(public_key='...',private_key='...'))

        or::

            form = SQLFORM(...)
            form.append(Recaptcha(public_key='...',private_key='...'))

        to protect the login page instead, use::

            from gluon.services.recaptcha import Recaptcha
            auth.settings.captcha = Recaptcha(public_key='...',private_key='...')

    """

    API_URI = 'https://www.google.com/recaptcha/api.js'
    VERIFY_SERVER = 'https://www.google.com/recaptcha/api/siteverify'

    def __init__(self,
                 public_key='',
                 private_key='',
                 error_message='invalid',
                 label='Verify:',
                 options=None,
                 comment='',
                 ):
        request = current.request
        self.request_vars = request and request.vars or current.request.vars
        self.remote_addr = request.env.remote_addr
        self.public_key = public_key
        self.private_key = private_key
        self.errors = Storage()
        self.error_message = error_message
        self.components = []
        self.attributes = {}
        self.label = label
        self.options = options or {}
        self.comment = comment

    def _validate(self):
        recaptcha_response_field = self.request_vars.pop('g-recaptcha-response', None)
        remoteip = self.remote_addr
        if not recaptcha_response_field:
            self.errors['captcha'] = self.error_message
            return False
        params = urllib.urlencode({
            'secret': self.private_key,
            'remoteip': remoteip,
            'response': recaptcha_response_field,
        })
        request = urllib2.Request(
            url=self.VERIFY_SERVER,
            data=params,
            headers={'Content-type': 'application/x-www-form-urlencoded',
                     'User-agent': 'reCAPTCHA Python'})
        httpresp = urllib2.urlopen(request)
        content = httpresp.read()
        httpresp.close()
        try:
            response_dict = json_parser.loads(content)
        except:
            self.errors['captcha'] = self.error_message
            return False
        if response_dict.get('success', False):
            self.request_vars.captcha = ''
            return True
        else:
            self.errors['captcha'] = self.error_message
            return False

    def xml(self):
        api_uri = self.API_URI
        hl = self.options.pop('hl', None)
        if hl:
            api_uri = self.API_URI + '?hl=%s' % hl
        public_key = self.public_key
        self.options['sitekey'] = public_key
        captcha = DIV(
            SCRIPT(_src=api_uri, _async='', _defer=''),
            DIV(_class="g-recaptcha", data=self.options),
            TAG.noscript(XML("""
<div style="width: 302px; height: 352px;">
<div style="width: 302px; height: 352px; position: relative;">
  <div style="width: 302px; height: 352px; position: absolute;">
    <iframe src="https://www.google.com/recaptcha/api/fallback?k=%(public_key)s"
            frameborder="0" scrolling="no"
            style="width: 302px; height:352px; border-style: none;">
    </iframe>
  </div>
  <div style="width: 250px; height: 80px; position: absolute; border-style: none;
              bottom: 21px; left: 25px; margin: 0px; padding: 0px; right: 25px;">
    <textarea id="g-recaptcha-response" name="g-recaptcha-response"
              class="g-recaptcha-response"
              style="width: 250px; height: 80px; border: 1px solid #c1c1c1;
                     margin: 0px; padding: 0px; resize: none;" value="">
    </textarea>
  </div>
</div>
</div>""" % dict(public_key=public_key))
            )
        )
        if not self.errors.captcha:
            return XML(captcha).xml()
        else:
            captcha.append(DIV(self.errors['captcha'], _class='error'))
            return XML(captcha).xml()

