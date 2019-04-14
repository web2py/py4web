from web3py import *
from web3py.form import Form
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE
from yatl.helpers import INPUT, H1

db = DAL('sqlite://test')
db.define_table('thing', 
                Field('name', requires=IS_NOT_EMPTY()),
                Field('nummber','integer', requires=IS_INT_IN_RANGE(0,10)))
session = Session(secret='myscret')

@action('/oops')
def oops():
    1/0

# exposed as /examples/form
@action('form', method=['GET','POST'])
@action.uses('form.html', db, session)
def form_example():
    form = Form(db.thing, csrf_uuid=session.get('uuid'))
    rows = db(db.thing).select()
    return dict(form=form, rows=rows) 

# exposed as /examples/showme
@action('showme')
@action.uses('generic.html')
def showme():
    return dict(a=H1("I am a title"),
                b=2,
                c=dict(d=3,
                       e=4,
                       x=INPUT(_name="test")))
