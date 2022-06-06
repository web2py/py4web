"""
This file defines the database models
"""
import datetime

from pydal.validators import *
from pydal.validators import IS_DATETIME, ValidationError

from py4web.utils.populate import populate

from .common import Field, T, auth, db

# simple table example
db.define_table(
    "person",
    Field("name", requires=IS_NOT_IN_DB(db, "person.name"), label=T("name")),
    Field("job", requires=IS_NOT_EMPTY(), label=T("job")),
    format="%(name)s",
)

# simple reference example
db.define_table(
    "superhero",
    Field("name", requires=IS_NOT_IN_DB(db, "superhero.name")),
    Field("real_identity", "reference person"),
    format="%(name)s",
)

db.define_table("superpower", Field("description"), format="%(description)s")

# many to many example
db.define_table(
    "tag",
    Field("superhero", "reference superhero"),
    Field("superpower", "reference superpower"),
    Field("strength", "integer"),
)

if not db(db.person).count():
    db.person.insert(
        name="Clark Kent",
        job="Journalist",
    )
    db.person.insert(name="Peter Park", job="Photographer")
    db.person.insert(name="Bruce Wayne", job="CEO")
    db.superhero.insert(name="Superman", real_identity=1)
    db.superhero.insert(name="Spiderman", real_identity=2)
    db.superhero.insert(name="Batman", real_identity=3)
    db.superpower.insert(description="Flight")
    db.superpower.insert(description="Strength")
    db.superpower.insert(description="Speed")
    db.superpower.insert(description="Durability")
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
    return None if auth.current_user is None else auth.current_user.get("email")


def get_time():
    return datetime.datetime.utcnow()


db.define_table(
    "thing",
    Field("name", required=True),
    Field("color", options=("red", "green", "blue")),
    Field("is_ready", "boolean"),
    Field("time_created", "time"),
    Field("date_created", "date"),
    Field("timetime_created", "datetime"),
)

if db(db.thing).isempty():
    populate(db.thing, 100)

db.commit()
