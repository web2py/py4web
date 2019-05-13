import uuid
from web3py import redirect, request, URL
from web3py.core import Fixture, Template
from pydal.validators import IS_EMAIL, CRYPT, IS_NOT_EMPTY, IS_NOT_IN_DB

class Auth(Fixture):
    
    def __init__(self, db, session, define_tables=True, extra_fields=None):
        self.db = db
        Field = db.Field
        self.session = session
        self.__prerequisites__ = [db, session]
        if define_tables and not 'auth_user' in db.tables:
            ne = IS_NOT_EMPTY()
            db.define_table(
                'auth_user',
                Field('email', requires=(IS_EMAIL(), IS_NOT_IN_DB(db, 'auth_user.email')), unique=True),
                Field('password','password', requires=CRYPT(),readable=False),
                Field('first_name', requires=ne),
                Field('last_name', requires=ne),
                Field('action_token', editable=False, readable=False),
                *(extra_fields or []))

    def get_user(self):
        user = self.session.get('user')
        if not user or not isinstance(user, dict) or not 'id' in user:
            return None
        if len(user) == 1:
            user = db.auth_user(user['id'])
        return user

    def action(self, path):
        method = request.method
        if not path.startswith('api/'):
            return Template('auth.html').transform({'action': path})
        elif path == 'api/register' and method=='POST':
            data = self.register(**request.json).as_dict()
            data['status'] = 'success'
            data['redirect'] = URL('auth/login')
        elif path == 'api/login' and method=='POST':
            user, error = self.login(**request.json)            
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
            self.request_reset_password(**request.json)
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
