from web3py import action, request, run, DAL, Field

db = DAL('sqlite://storage.db')
db.define_table('todo', Field('info'))

@action('/$APP/index', method='GET', view='index.html')
def index():
    return dict()

@action('/$APP/api', method='GET')
def todo():
    return dict(items=db(db.todo).select().as_list())

@action('/$APP/api', method='POST')
def todo():
    return dict(id=db.todo.insert(info=request.json.get('info')))

@action('/$APP/api/<id>', method='DELETE')
def todo(id):    
    db(db.todo.id==id).delete()
    return dict()
