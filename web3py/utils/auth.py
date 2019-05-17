import hashlib
import uuid
from web3py import redirect, request, URL
from web3py.core import Fixture, Template
from pydal.validators import IS_EMAIL, CRYPT, IS_NOT_EMPTY, IS_NOT_IN_DB

class Auth(Fixture):

    messages = {
        'confirm_email': {
            'subject': 'Confirm email',
            'body': 'Welcome {first_name}, click {link} to confirm your email'
            },
        'reset_password': {
            'subject': 'Password reset',
            'body': 'Hello {first_name}, click {link} to change password'
            },
        'unsubscribe': {
            'subject': 'Unsubscribe confirmation',
            'body': 'By {first_name}, you have been erased from our system'
            }
        }
    
    extra_auth_user_fields = []

    def __init__(self, db, session, 
                 define_tables=True, 
                 sender=None,
                 registration_requires_confirmation=True,
                 registration_requires_appoval=False):        
        self.db = db
        self.session = session
        self.sender = sender
        self.registration_requires_confirmation = registration_requires_confirmation
        self.registration_requires_appoval = registration_requires_appoval
        self.__prerequisites__ = [db, session]
        if define_tables:
            self.define_tables()

    def define_tables(self):
        db = self.db
        Field = db.Field
        if not 'auth_user' in db.tables:
            ne = IS_NOT_EMPTY()
            db.define_table(
                'auth_user',
                Field('email', requires=(IS_EMAIL(), IS_NOT_IN_DB(db, 'auth_user.email')), unique=True),
                Field('password','password', requires=CRYPT(), readable=False),
                Field('first_name', requires=ne),
                Field('last_name', requires=ne),
                Field('sso_id', editable=False, readable=False),
                Field('action_token', editable=False, readable=False),
                *self.extra_auth_user_fields)

    def send(self, name, user, **attrs):
        """extend the object and override this function to send messages with
        twilio or onesignal or alternative method other than email"""
        message = self.messages[name]
        d = dict(user)
        d.update(**attrs)
        email = user['email']
        subject = message['subject'].format(**d)
        body = message['body'].format(**d)
        if not self.sender:
            print('Mock send to %s subject "%s" body:\n%s\n' % (email, subject, body))
            return True
        return self.sender.send(email, subject=subject, body=body)

    def get_user(self):
        user = self.session.get('user')
        if not user or not isinstance(user, dict) or not 'id' in user:
            return None
        if len(user) == 1:
            user = self.db.auth_user(user['id'])
        return user

    def action(self, path):
        method = request.method
        if not path.startswith('api/'):
            return Template('auth.html').transform({'action': path})
        if method == 'POST':
            user = self.get_user()
            if not user:
                if path == 'api/register':
                    data = self.register(dict(request.json), send=True).as_dict()
                    data['status'] = 'success'
                    data['redirect'] = URL('auth/login')
                elif path == 'api/login':
                    user, error = self.login(**dict(request.json))
                    if user:
                        self.session['user'] = {'id': user.id}
                        user = {f.name: user[f.name] for f in self.db.auth_user if f.readable}
                        data = {'user': user, 'ststus': 'success', 'redirect': URL('index')}
                    else:
                        data = {'ststus': 'error', 'message': error}               
                elif path == 'api/logout':
                    self.session['user'] = None
                    data = {'status': 'success'}
                elif path == 'request_reset_password':
                    if self.request_reset_password(**dict(request.json)):
                        data = {'status': 'success'}
                    else:
                        data = {'status': 'error', 'message': 'invalid user'}
                elif path == 'api/reset_password':
                    if self.reset_password(request.json().get('token'), request.json().get('new_password')):
                        data = {'status': 'success'}
                    else:
                        data = {'status': 'error', 'message': 'invalid token, request expired'}
                elif path == 'api/verify_email':
                    if self.verify_email(request.json().get('token')):
                        data = {'status': 'success'}
                    else:
                        data = {'status': 'error', 'message': 'invalid token, request expired'}
            else:
                if path == 'api/change_password':
                    if self.change_password(request.json().get('old_password'), 
                                            request.json().get('new_password')):
                        data = {'status': 'success'}
                    else:
                        data = {'status': 'error', 'message': 'invalid password'}
                elif path == 'api/change_email':
                    data = {'status': 'error', 'message': 'action not implemented'}
                elif path == 'api/edit_profile':
                    data = {'status': 'error', 'message': 'action not implemented'}
                else:
                    data = {'status': 'error', 'message': 'action not implemented'}
        return data

    def register(self, fields, send=True):
        fields['email'] = fields['email'].lower()
        token = uuid.uuid4()
        fields['action_token'] = 'pending-registation:%s' % token
        res = self.db.auth_user.validate_and_insert(**fields)        
        if send and res.get('id'):        
            link = self.base_url + 'api/verify_email?token=' + token 
            self.send('verify_email', fields, link=link)

    def login(self, email, password):
        db = self.db
        user = db(db.auth_user.email == email.lower()).select().first()
        if not user: return (None, 'Invalid email')
        if (user.action_token).startswith('pending-registration'):
            return (None, 'Registration is pending')
        if (user.action_token).startswith('account-blocked'):
            return (None, 'Account is blocked')
        if db.auth_user.password.requires(password)[0] == user.password:
            return (user, None)
        return None, 'Invalid password'

    def update(self, **fields):
        email = fields['email'].lower()
        self.db(self.db.auth_user.email == email).update(**fields)

    def request_reset_password(self, email, send=True):
        user = self.db(self.db.auth_user.email == email.lower()).select().first()
        if user and not user.action_token == 'account-blocked':
            token = str(uuid.uuid4())
            user.update_record(action_token='reset-password-request:'+token)
            if send:
                link = self.base_url + 'api/reset_password?token=' + token
                self.send('reset_password', user, link=link)
            return token
        return None

    def query_from_token(self,token):
        query = self.db.auth_user.action_token == 'reset-password-request:' + token
        query |= self.db.auth_user.action_token == 'pending-registration:' + token
        return query

    def verify_email(self, token):
        n = self.db(self.query_from_token(token)).update(action_token=None)
        return n>0

    def reset_password(self, token, new_password):
        user = self.db(self.query_from_token(token)).select().first()
        if user:
            if user.update_record(password=self.db.auth_user.passoword.requires(new_password)[1]):
                return True
        return False

    def change_password(self, old_password, new_password):
        user = self.get_user()
        if user and self.db.auth_user.passoword.requires(old_password)[1] == user.password:
            if user.update_record(password=self.db.auth_user.passoword.requires(new_password)[1]):
                return True
        return False

    def gdpr_unsubscribe(self, user, send=True):
        """GDPR unsubscribe means we delete first_name, last_name,
        replace email with hash of the actual email and notify the user
        Essentially we lose the info about who is who
        Yet we have the ability to verify that a given email has unsubscribed 
        and maybe restore it if it was a mistake.
        Despite unsubscription we retain enought info to be able to comply
        with police audit for illecit activities.
        I am not a lwayer but I believe this to be OK.
        Check with your lwayr before using this feature.
        """
        user = user.as_dict()
        id = user['id']
        token = hashlib.sha1(user['email'].lower()).hexdigest()
        db = self.db
        db(db.auth_user.id==id).update(
            email="%s@example.com" % token,
            password=None,
            first_name='anonymous', 
            last_name='anonymous',
            sso_id=None,
            action_token='gdpr-unsubscribed')
        if send:
            self.send('unsubscribe', user)
        
    def is_gdpr_unsubscribed(self, email):
        db = self.db
        token = hashlib.sha1(email.lower()).hexdigest()
        email="%s@example.com" % token
        return db(db.auth_user.email==email).count() > 0
