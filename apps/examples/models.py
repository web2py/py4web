import os
from py4web import DAL, Field
from pydal.validators import IS_NOT_EMPTY, IS_NOT_IN_DB
# define database and tables
db = DAL('sqlite://storage.db', folder=os.path.join(os.path.dirname(__file__), 'databases'))

# simple table example
db.define_table(
    'person',
    Field('name', requires=IS_NOT_IN_DB(db, 'person.name')),
    Field('job', requires=IS_NOT_EMPTY()))

# simple reference example
db.define_table(
    'superhero',
    Field('name'),
    Field('real_identity', 'reference person'))

db.define_table(
    'superpower',
    Field('description'))

# many to many example
db.define_table(
    'tag',
    Field('superhero', 'reference superhero'),
    Field('superpower', 'reference superpower'),
    Field('strength', 'integer'))

if not db(db.person).count():
    db.person.insert(name='Clark Kent', job='Journalist')
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
    db.commit()
