import os
from web3py import *
from web3py.form import Form
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1

db = DAL('sqlite://test', folder=os.path.join(os.path.dirname(__file__), 'databases'))
db.define_table('thing', 
                Field('name', requires=IS_NOT_EMPTY()),
                Field('quantity','integer', requires=IS_INT_IN_RANGE(0,10)))
session = Session(secret='myscret')

@action('oops')
def oops():
    1/0

# exposed as /examples/form
@action('dbform', method=['GET','POST'])
@action.uses('dbform.html', db, session)
def form_example():
    form = Form(db.thing, csrf_uuid=session.get('uuid'))
    rows = db(db.thing).select()
    return dict(form=form, rows=rows) 

@action('forms', method=['GET','POST'])
@action.uses('forms.html', session, db)
def multiple_form_example():
    uuid = session.get('uuid')
    name = Field('name', requires=IS_NOT_EMPTY())
    forms = [
        Form([Field('name', requires=IS_NOT_EMPTY())],
             csrf_uuid=uuid, form_name='1'),
        Form([Field('name', requires=IS_NOT_EMPTY())],
             csrf_uuid=uuid, form_name='2', keep_values=True),
        Form([Field('name', requires=IS_NOT_EMPTY()),
              Field('age','integer')], 
             csrf_uuid=uuid, form_name='3'),
        Form([Field('name', requires=IS_NOT_EMPTY()),
              Field('insane','boolean')], 
             csrf_uuid=uuid, form_name='4'),
        Form([Field('name', requires=IS_NOT_EMPTY()),
              Field('color',requires=IS_IN_SET(['red','blue','gree']))], 
             csrf_uuid=uuid, form_name='5'),
        Form([Field('name', requires=IS_NOT_EMPTY()),
              Field('favorite_thing', requires=IS_IN_DB(db, 'thing.id', 'thing.name'))], 
             csrf_uuid=uuid, form_name='6')]
    messages = []
    for form in forms:
        if form.accepted:
            messages.append('form %s accepted with: %s ' % (form.form_name, form.vars))
        elif form.errors:
            messages.append('form %s has errors: %s ' % (form.form_name, form.errors))
    return dict(forms=forms, messages=messages)

# exposed as /examples/showme
@action('showme')
@action.uses('generic.html')
def showme():
    return dict(a=H1("I am a title"),
                b=2,
                c=dict(d=3,
                       e=4,
                       x=INPUT(_name="test")))
