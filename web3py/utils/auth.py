import hashlib
import uuid
from web3py import redirect, request, URL
from web3py.core import Fixture, Template
from pydal.validators import IS_EMAIL, CRYPT, IS_NOT_EMPTY, IS_NOT_IN_DB

class Auth(Fixture):

    messages = {
        'confirm_email': 'Welcome {first_name}, click {link} to confirm your email',
        'request_password': 'Hello {first_name}, click {link} to change password',
        'unsubscribe': 'By {first_name}, you have been erased from our system'
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

    def send(self, user, subject, body):
        """extend the object and override this function to send messages with
        twilio or onesignal or alternative method other than email"""
        if not self.sender:
            print('Mock send to %s subject "%s" body:\n%s\n' % (
                    user.id, subject, body)) 
            return True
        self.sender.send(to=user.email, subject=subject, body=body)

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
        elif path == 'api/register' and method=='POST':
            data = self.register(**dict(request.json)).as_dict()
            data['status'] = 'success'
            data['redirect'] = URL('auth/login')
        elif path == 'api/login' and method=='POST':
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
            self.request_reset_password(**dict(request.json))
        elif path == 'api/reset_password':
            user = self.session.get('user')
            data = {'status': 'error', 'message': 'action not implemented'}
        elif path == 'api/verify_email':
            data = {'status': 'error', 'message': 'action not implemented'}
        elif path == 'api/change_email':
            user = self.session.get('user')
            data = {'status': 'error', 'message': 'action not implemented'}
        elif path == 'api/change_password':
            user = self.session.get('user')
            data = {'status': 'error', 'message': 'action not implemented'}
        elif path == 'api/edit_profile':
            user = self.session.get('user')
            data = {'status': 'error', 'message': 'action not implemented'}
        else:
            data = {'status': 'error', 'message': 'action not implemented'}
        return data

    def register(self, **fields):
        fields['email'] = fields['email'].lower()
        fields['action_token'] = 'pending-registation:%s' % uuid.uuid4() 
        return self.db.auth_user.validate_and_insert(**fields)

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

    def request_reset_password(self, email):
        user = self.db(self.db.auth_user.email == email.lower()).select().first()
        if user and not user.action_token == 'account-blocked':
            token = str(uuid.uuid4())
            user.update_record(action_token='reset-password-request:'+token)
            return token
        return None

    def verify_account(self, token):
        query = self.db.auth_user.action_token == 'reset-password-request:'+token
        query |= self.db.auth_user.action_token == 'pending-registration:'+token
        n = self.db(query).update(action_token=None)
        return n>0

    def gdpr_unsubscribe(self, user):
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
        body = self.messages['unsubscribe'].format(**user)
        self.send(user=user,
                  subject="GDPR Unsubscribe",
                  body=body)
        
    def is_gdpr_unsubscribed(self, email):
        db = self.db
        token = hashlib.sha1(email.lower()).hexdigest()
        email="%s@example.com" % token
        return db(db.auth_user.email==email).count() > 0
