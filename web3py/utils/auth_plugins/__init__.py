import urllib
import requests
from web3py.core import URL

class SSO(object):

    name = 'undefined'
    login_button_content = ''
    login_button_class = ''

    def __init__(self, **parameters):
        self.parameters = parameters

    def get_login_url(self):
        pass

    def calback(self, query, session=None):
        pass

    @staticmethod
    def _build_url(base, data):
        return base + '?' + '&'.join('%s=%s' % (k, urllib.parse.quote(v)) for k,v in data.items())

class OAuth2(SSO):
    name = 'undefined'
    login_button_content = ''
    login_button_class = ''
    login_url = ''
    token_url = ''
    userinfo_url = ''
    default_scope = ''

    def __init__(self, client_id, client_secret, callback_url, scope=None):
        SSO.__init__(self)
        self.parameters = dict(client_id=client_id,
                               client_secret=client_secret,
                               callback_url=callback_url,
                               scope=scope or self.default_scope)
        
    def get_login_url(self, state=None):
        data = dict(access_type='offline',
                    redirect_uri=URL(self.parameters.get('callback_url'), scheme=True),
                    response_type='code',
                    client_id=self.parameters.get('client_id'))
        scope=self.parameters.get('scope')
        if scope:
            data['scope'] = scope
            data['include_granted_scopes'] = 'true'
        if state:
            data['state'] = state
        return self._build_url(self.login_url, data)

    def callback(self, query):
        code = query.get('code')
        if not code:
            return False
        data = dict(code=code,
                    client_id=self.parameters.get('client_id'),
                    client_secret=self.parameters.get('client_secret'),
                    redirect_uri=URL(self.parameters.get('callback_url'), scheme=True),
                    grant_type='authorization_code')
        res = requests.post(self.token_url, data=data)
        token = res.json().get('access_token')
        headers = {'Authorization': 'Bearer %s' % token}
        res = requests.get(self.userinfo_url, headers=headers)
        data = res.json()
        return data

    def revoke(self, token):
        requests.post(self.revoke_url, data=dict(token=token))
