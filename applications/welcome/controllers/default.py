def index():
    return dict()

def simple():
    return 'hello world'

def vars():
    return 'request.vars='+str(request.vars)

def template():
    return dict(a=1, b=2)

def make_thing():
    from gluon.dal import DAL
    from gluon.form import Form
    db = DAL('sqlite://storage.db')
    db.define_table('thing',Field('name'))
    form = Form(db.thing, csrf=False)
    return dict(form=form)

