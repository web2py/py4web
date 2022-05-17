"""
This file defines the database models
"""
import datetime

from .common import db, Field, T, auth
from pydal.validators import *
from py4web.utils.populate import populate

# simple table example
db.define_table(
    'person',
    Field('name', requires=IS_NOT_IN_DB(db, 'person.name'), label=T('name')),
    Field('job', requires=IS_NOT_EMPTY(), label=T('job')),
    format='%(name)s',
)

# simple reference example
db.define_table(
    'superhero',
    Field('name', requires=IS_NOT_IN_DB(db, 'superhero.name')),
    Field('real_identity', 'reference person'),
    format='%(name)s',
)

db.define_table('superpower', Field('description'), format='%(description)s')

# many to many example
db.define_table(
    'tag',
    Field('superhero', 'reference superhero'),
    Field('superpower', 'reference superpower'),
    Field('strength', 'integer'),
)

if not db(db.person).count():
    db.person.insert(
        name='Clark Kent', job='Journalist',
    )
    db.person.insert(name='Peter Park', job='Photographer')
    db.person.insert(name='Bruce Wayne', job='CEO')
    db.superhero.insert(name='Superman', real_identity=1)
    db.superhero.insert(name='Spiderman', real_identity=2)
    db.superhero.insert(name='Batman', real_identity=3)
    db.superpower.insert(description='Flight')
    db.superpower.insert(description='Strength')
    db.superpower.insert(description='Speed')
    db.superpower.insert(description='Durability')
    db.tag.insert(superhero=1, superpower=1, strength=100)
    db.tag.insert(superhero=1, superpower=2, strength=100)
    db.tag.insert(superhero=1, superpower=3, strength=100)
    db.tag.insert(superhero=1, superpower=4, strength=100)
    db.tag.insert(superhero=2, superpower=2, strength=50)
    db.tag.insert(superhero=2, superpower=3, strength=75)
    db.tag.insert(superhero=2, superpower=4, strength=10)
    db.tag.insert(superhero=3, superpower=2, strength=80)
    db.tag.insert(superhero=3, superpower=3, strength=20)
    db.tag.insert(superhero=3, superpower=4, strength=70)

# Used for examples of forms.
def get_user_email():
    return None if auth.current_user is None else auth.current_user.get('email')


def get_time():
    return datetime.datetime.utcnow()


db.define_table(
    'product',
    Field('product_name'),
    Field('product_quantity', 'integer', requires=IS_INT_IN_RANGE(0, None), default=0),
    Field('product_cost', 'float', requires=IS_FLOAT_IN_RANGE(0, None), default=0.0),
    Field('mail_order', 'boolean'),
    Field('created_by', default=get_user_email),
    Field('creation_date', 'datetime', default=get_time),
)

# We do not want these fields to appear in forms by default.
db.product.id.readable = False
db.product.created_by.readable = False
db.product.creation_date.readable = False

db.define_table(
    'thing',
    Field('name', required=True),
    Field('color', options=('red', 'green', 'blue')),
    Field('is_ready', 'boolean'),
    Field('time_created', 'time'),
    Field('date_created', 'date'),
    Field('timetime_created', 'datetime'))

if db(db.thing).isempty():
    populate(db.thing, 100)

db.define_table(
    'vue_form_table',
    Field("first_name", default="Jane"),
    Field("last_name", default="Smith", writable=False),
    Field("read", "boolean", default=True),
    Field(
        "animal",
        requires=IS_IN_SET(["cat", "dog", "bird"]),
        default="dog",
        writable=False,
    ),
    Field(
        "choice",
        requires=IS_IN_SET({"c": "cat", "d": "dog", "b": "bird"}),
        default="d",
    ),
    Field("arrival_time", "datetime", default=get_time),
    Field("date_of_birth", "date"),
    Field("narrative", "text"),
)


db.commit()
