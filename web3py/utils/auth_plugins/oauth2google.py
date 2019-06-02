from . import OAuth2

class OAuth2Google(OAuth2):
    name = 'oauth2google'
    login_button_content = 'Login with Google'
    login_button_class = 'google-login-button'
    login_url = 'https://accounts.google.com/o/oauth2/v2/auth'
    token_url = 'https://www.googleapis.com/oauth2/v4/token'
    userinfo_url = 'https://www.googleapis.com/plus/v1/people/me'
    #userinfo_url = 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json'
    revoke_url = 'https://accounts.google.com/o/oauth2/revoke'
    default_scope='email' #https://www.googleapis.com/auth/plus.me'
    maps = {
        'email': 'emails.0.value',
        'id': 'id',
        'first_name': 'name.givenName',
        'last_name': 'name.familyName'
        }

