"""
This file defines the database models
"""
import datetime

from pydal.validators import *
from pydal.validators import IS_DATETIME, ValidationError

from .common import Field, T, auth, db


class IS_ISO_DATETIME(IS_DATETIME):
    def validate(self, value, record_id=None):
        if isinstance(value, datetime.datetime):
            return value
        try:
            if value[-1:] == "Z":
                value = value[:-1]
            value = datetime.datetime.fromisoformat(value)
            return value.replace(tzinfo=datetime.timezone.utc)
        except:
            raise ValidationError("Wrong date format")

    def formatter(self, value):
        print("Asked to format:", value)
        if value is None or value == "":
            return None
        return value.isoformat()


def get_utc_time():
    return datetime.datetime.utcnow().isoformat()


db.define_table(
    "vue_form_table",
    Field("first_name", default="Jane"),
    Field("last_name", default="Smith"),
    Field("read", "boolean", default=True),
    Field(
        "animal",
        requires=IS_IN_SET(["cat", "dog", "bird"]),
        default="dog",
    ),
    Field("arrival_time", "datetime", default=get_utc_time, requires=IS_ISO_DATETIME()),
    Field("date_of_birth", "date"),
    Field("narrative", "text"),
)
db.vue_form_table.id.readable = db.vue_form_table.id.writable = False

db.commit()
