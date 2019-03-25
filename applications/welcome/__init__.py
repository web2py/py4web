from web3py import action, request, DAL, Field, Session, Cache

session = Session(secret = 'some secret')
cache = Cache(size=1000)

db = DAL('sqlite://storage.db')
db.define_table('todo', Field('info'))

# example index page using session, template and vue.js
@action('/$app_name/index', view='index.html')
def index(session=session):
    session['counter'] = session.get('counter', 0) + 1
    return dict(session=session)

# example of GET/POST/DELETE RESTful APIs
@action('/$app_name/api')
def todo(db=db):
    return dict(items=db(db.todo).select().as_list())

@action('/$app_name/api', method='POST')
def todo(db=db):
    return dict(id=db.todo.insert(info=request.json.get('info')))

@action('/$app_name/api/<id>', method='DELETE')
def todo(id, db=db, session=session):   
    db(db.todo.id==id).delete()
    return dict()

# example of caching
@action('/$app_name/uuid')
@cache.memoize(expiration=5)
def uuid():
    import uuid
    return str(uuid.uuid4())
