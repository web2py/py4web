import json
import uuid

from py4web.core import Fixture, action, request, response

from .models import Field, db

# for demo purposes we create a table of tokens
# in practice you want to link them to users
db.define_table("user_token", Field("token"), Field("user_id", db.auth_user))

# we also create a storage where to put raw data
# in practice you want to use something more structured
db.define_table("dummy", Field("token"), Field("name"), Field("raw", "json"))


# let's create a fixture to check auth token exists
def get_token():
    return request.headers.get("Authentication")


class AuthTokenVerify(Fixture):
    def on_request(self, context):
        # response.headers = "Content-Type: application/json"
        token = get_token()
        if not db(db.user_token.token == token).count():
            raise HTTP(401)


auth_token_verify = AuthTokenVerify()

# put the id into the raw dict
def to_dict(item):
    if not item or not item.raw:
        return {}
    raw = dict(item.raw)
    raw["id"] = item.id
    return raw


# return records filetered by name and token
def my_stuff(name):
    return db(db.dummy.token == get_token())(db.dummy.name == name)


# select all records
@action("rest/<name>", method="GET")
@action.uses(db, auth_token_verify)
def rest(name):
    items = [to_dict(item) for item in my_stuff(name).select(cacheable=True)]
    print(items)
    return {"items": items}


# select one record
@action("rest/<name>/<id:int>", method="GET")
@action.uses(db, auth_token_verify)
def rest(name, id):
    token = request.headers.get("Authentication")
    item = my_stuff(name)(db.dummy.id == id).select(cacheable=True).first()
    return to_dict(item)


# create a record
@action("rest/<name>", method="POST")
@action.uses(db, auth_token_verify)
def rest(name):
    token = request.headers.get("Authentication")
    id = db.dummy.insert(token=get_token(), name=name, raw=request.json)
    return {"id": id}


# update a record
@action("rest/<name>/<id:int>", method="PUT")
@action.uses(db, auth_token_verify)
def rest(name, id):
    item = my_stuff(name)(db.dummy.id == id).select(cacheable=True).first()
    if item:
        raw = item.raw
        raw.update(**request.json)
        my_stuff(name)(db.dummy.id == id).update(raw=raw)
    return to_dict(item)


# delete a record
@action("rest/<name>/<id:int>", method="DELETE")
@action.uses(db, auth_token_verify)
def rest(name, id):
    my_stuff(name)(db.dummy.id == id).delete()
    return {}


@action("rest")
@action.uses("examples/rest_info.html", db)
def rest():
    new_token = str(uuid.uuid4())
    id = db.user_token.insert(token=new_token)
    # expire old user tokens
    db(db.user_token.id < max(1, id - 1000)).delete()
    return dict(token=new_token)
