import os
from py4web import *
from py4web.utils.form import Form, FormStyleBulma
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1

if not os.path.exists(os.path.join(os.path.dirname(__file__), 'databases')):
    try:
        os.makedirs(os.path.join(os.path.dirname(__file__), 'databases'))
    except FileExistsError:
        pass

db = DAL('sqlite://test', folder=os.path.join(os.path.dirname(__file__), 'databases'))
db.define_table('thing', 
                Field('name', requires=IS_NOT_EMPTY()),
                Field('size','integer', requires=IS_INT_IN_RANGE(0,10)),
                format='%(name)s')
db.define_table(
    'order',
    Field('code', requires=IS_NOT_EMPTY()),
    Field('thing', 'reference thing'))

if db(db.thing).count() == 0:
    db.thing.insert(name='pants', size=1)
    db.thing.insert(name='shirt', size=1)
    db.order.insert(code='123', thing=1)

db.commit()
session = Session(secret='myscret')

@action('do/nothing')
def do_nothing():
    return 'ok'

@action('oops')
def oops():
    1/0

# exposed as /examples/dbform
@action('dbform_thing/<id>', method=['GET','POST'])
@action.uses('dbform.html', db, session)
def form_example(id):
    form = Form(db.thing, id)
    rows = db(db.thing).select()
    return dict(form=form, rows=rows) 

# exposed as /examples/dbform2                                                                             
@action('dbform_order/<id>', method=['GET','POST'])
@action.uses('dbform.html', db, session)
def form_example2(id):
    form = Form(db.order, id)
    rows = db(db.order).select()
    return dict(form=form, rows=rows)

@action('forms', method=['GET','POST'])
@action.uses('forms.html', session, db)
def multiple_form_example():
    name = Field('name', requires=IS_NOT_EMPTY())
    forms = [
        Form([Field('name', requires=IS_NOT_EMPTY())],
             form_name='1', formstyle=FormStyleBulma),
        Form([Field('name', requires=IS_NOT_EMPTY())],
             form_name='2', keep_values=True, formstyle=FormStyleBulma),
        Form([Field('name', requires=IS_NOT_EMPTY()),
              Field('age','integer')], 
             form_name='3', formstyle=FormStyleBulma),
        Form([Field('name', requires=IS_NOT_EMPTY()),
              Field('insane','boolean')], 
             form_name='4', formstyle=FormStyleBulma),
        Form([Field('name', requires=IS_NOT_EMPTY()),
              Field('color',requires=IS_IN_SET(['red','blue','gree']))], 
             form_name='5', formstyle=FormStyleBulma),
        Form([Field('name', requires=IS_NOT_EMPTY()),
              Field('favorite_thing', requires=IS_IN_DB(db, 'thing.id', 'thing.name'))], 
             form_name='6', formstyle=FormStyleBulma)]
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
