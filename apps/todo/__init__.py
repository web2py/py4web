import os
from py4web import action, request, DAL, Field, Session, Cache, user_in

# define session and cache objects
session = Session(secret="some secret")
cache = Cache(size=1000)

# define database and tables
db = DAL(
    "sqlite://storage.db", folder=os.path.join(os.path.dirname(__file__), "databases")
)
db.define_table("todo", Field("info"))
db.commit()

# example index page using session, template and vue.js
@action("index")  # the function below is exposed as a GET action
@action.uses("index.html")  # we use the template index.html to render it
@action.uses(session)  # action needs a session object (read/write cookies)
def index():
    session["counter"] = session.get("counter", 0) + 1
    session["user"] = {"id": 1}  # store a user in session
    return dict(session=session)


# example of GET/POST/DELETE RESTful APIs


@action("api")  # a GET API function
@action.uses(session)  # we load the session
@action.requires(user_in(session))  # then check we have a valid user in session
@action.uses(db)  # all before starting a db connection
def todo():
    return dict(items=db(db.todo).select(orderby=~db.todo.id).as_list())


@action("api", method="POST")
@action.uses(session)
@action.requires(user_in(session))
@action.uses(db)
def todo():
    return dict(id=db.todo.insert(info=request.json.get("info")))


@action("api/<id:int>", method="DELETE")
@action.uses(session)
@action.requires(user_in(session))
@action.uses(db)
def todo(id):
    db(db.todo.id == id).delete()
    return dict()


# example of caching
@action("uuid")
@cache.memoize(expiration=5)  # here we cache the result for 5 seconds
def uuid():
    import uuid

    return str(uuid.uuid4())
