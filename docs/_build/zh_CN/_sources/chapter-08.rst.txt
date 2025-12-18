===========
The RestAPI
===========

Since version 19.5.10 pyDAL includes a restful API [CIT0801]_ called RestAPI. It is
inspired by GraphQL [CIT0802]_ and while it’s not quite the same due to it being less
powerful, it is in the spirit of py4web since it's more practical and easier to use.

Like GraphQL RestAPI allows a client to query for information using the
GET method and allows to specify some details about the format of the
response (which references to follow, and how to denormalize the data).
Unlike GraphQL it allows the server to specify a policy and restrict
which queries are allowed and which ones are not. They can be evaluated
dynamically per request based on the user and the state of the server.

As the name implies RestAPI allows all standard methods: GET, POST, PUT,
and DELETE. Each of them can be enabled or disabled based on the policy,
for individual tables and individual fields.

.. note::

   Specifications might be subject to changes since this is a new feature.

In the examples below we assume a simple app called “superheroes”:

.. code:: python

    # in superheroes/__init__.py
    import os
    from py4web import action, request, Field, DAL
    from pydal.restapi import RestAPI, Policy

    # database definition
    DB_FOLDER = os.path.join(os.path.dirname(__file__), 'databases')
    if not os.path.isdir(DB_FOLDER):
        os.mkdir(DB_FOLDER)
    db = DAL('sqlite://storage.sqlite', folder=DB_FOLDER)
    db.define_table(
        'person',
        Field('name'),
        Field('job'))
    db.define_table(
        'superhero',
        Field('name'),
        Field('real_identity', 'reference person'))
    db.define_table(
        'superpower',
        Field('description'))
    db.define_table(
        'tag',
        Field('superhero', 'reference superhero'),
        Field('superpower', 'reference superpower'),
        Field('strength', 'integer'))

    # add example entries in db
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

    # policy definitions
    policy = Policy()
    policy.set('superhero', 'GET', authorize=True, allowed_patterns=['*'])
    policy.set('*', 'GET', authorize=True, allowed_patterns=['*'])

    # for security reasons we disabled here all methods but GET at the policy level,
    # to enable any of them just set authorize = True
    policy.set('*', 'PUT', authorize=False)
    policy.set('*', 'POST', authorize=False)
    policy.set('*', 'DELETE', authorize=False)

    @action('api/<tablename>/', method = ['GET', 'POST'])
    @action('api/<tablename>/<rec_id>', method = ['GET', 'PUT', 'DELETE'])
    @action.uses(db)
    def api(tablename, rec_id=None):
        return RestAPI(db, policy)(request.method,
                                tablename,
                                rec_id,
                                request.GET,
                                request.POST
                                )

    @action("index")
    def index():
        return "RestAPI example"


RestAPI policies and actions
----------------------------

The policy is per table (or * for all tables) and per method. ``authorize``
can be True (allow), False (deny) or a function with the signature
(method, tablename, record_id, get_vars, post_vars) which returns
True/False. For the GET policy one can specify a list of allowed query
patterns (* for all). A query pattern will be matched against the keys
in the query string.

The above action is exposed as:

::

   /superheroes/api/{tablename}
   /superheroes/api/{tablename}/{rec_id}


The result can be seen directly with a browser, rendered as JSON.
Let's look for example at the ``person`` table:

.. image:: images/restapi.png


The diagram of the superhero's database should help you interpreting the code:


.. image:: images/restapi2.png


.. note::

   Keep in mind that **request.POST** only contains the form data
   that is posted using a **regular HTML-form** or **JavaScript
   FormData** object.

RestAPI GET
-----------

The general query has the form ``{something}.eq=value`` where ``eq=``
stands for “equal”, ``gt=`` stands for “greater than”, etc. The
expression can be prepended by ``not.``.

``{something}`` can be:

- the name of a field in the table being queried as in:

    **All superheroes called “Superman”**

    ::

    /superheroes/api/superhero?name.eq=Superman


- the name of a field of a table referred by the table being queried as in:

    **All superheroes with real identity “Clark Kent”**

    ::

    /superheroes/api/superhero?real_identity.name.eq=Clark Kent

- the name of a field of a table that refers to the table being queried as in:

    **All superheroes with any tag superpower with strength > 90**

    ::

    /superheroes/api/superhero?superhero.tag.strength.gt=90

    (here ``tag`` is the name of the link table, the preceding ``superhero`` is
    the name of the field that refers to the selected table and ``strength``
    is the name of the field used to filter)

- a field of the table referenced by a many-to-many linked table as in:

    **All superheroes with the flight power**

    ::

    /superheroes/api/superhero?superhero.tag.superpower.description.eq=Flight


.. hint::
    The key to understand the syntax above is to read it as:

    << select records of table **superhero** referred by field **superhero**
    of table **tag**, when the **superpower** field of said table points
    to a record with **description** equal to “Flight” >>


The query allows additional modifiers for example:

::

   @offset=10
   @limit=10
   @order=name
   @model=true
   @lookup=real_identity

The first 3 are obvious. ``@model`` returns a JSON description of database
model. ``@lookup`` denormalizes the linked field.


RestAPI practical examples
--------------------------

Here are some practical examples:

URL:

::

   /superheroes/api/superhero

OUTPUT:

.. code:: json

   {
       "count": 3,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 1,
               "name": "Superman",
               "id": 1
           },
           {
               "real_identity": 2,
               "name": "Spiderman",
               "id": 2
           },
           {
               "real_identity": 3,
               "name": "Batman",
               "id": 3
           }
       ],
       "timestamp": "2019-05-19T05:38:00.132635",
       "api_version": "0.1"
   }

URL:

::

   /superheroes/api/superhero?@model=true

OUTPUT:

.. code:: json

   {
       "count": 3,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 1,
               "name": "Superman",
               "id": 1
           },
           {
               "real_identity": 2,
               "name": "Spiderman",
               "id": 2
           },
           {
               "real_identity": 3,
               "name": "Batman",
               "id": 3
           }
       ],
       "timestamp": "2021-01-04T07:03:38.466030",
       "model": [
           {
               "regex": "[1-9]\\d*",
               "name": "id",
               "default": null,
               "required": false,
               "label": "Id",
               "post_writable": true,
               "referenced_by": [
                   "tag.superhero"
               ],
               "unique": false,
               "type": "id",
               "options": null,
               "put_writable": true
           },
           {
               "regex": null,
               "name": "name",
               "default": null,
               "required": false,
               "label": "Name",
               "post_writable": true,
               "unique": false,
               "type": "string",
               "options": null,
               "put_writable": true
           },
           {
               "regex": null,
               "name": "real_identity",
               "default": null,
               "required": false,
               "label": "Real Identity",
               "post_writable": true,
               "references": "person",
               "unique": false,
               "type": "reference",
               "options": null,
               "put_writable": true
           }
       ],
       "api_version": "0.1"
   }

URL:

::

   /superheroes/api/superhero?@lookup=real_identity

OUTPUT:

.. code:: json

   {
       "count": 3,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": {
                   "name": "Clark Kent",
                   "job": "Journalist",
                   "id": 1
               },
               "name": "Superman",
               "id": 1
           },
           {
               "real_identity": {
                   "name": "Peter Park",
                   "job": "Photographer",
                   "id": 2
               },
               "name": "Spiderman",
               "id": 2
           },
           {
               "real_identity": {
                   "name": "Bruce Wayne",
                   "job": "CEO",
                   "id": 3
               },
               "name": "Batman",
               "id": 3
           }
       ],
       "timestamp": "2019-05-19T05:38:00.178974",
       "api_version": "0.1"
   }

URL:

::

   /superheroes/api/superhero?@lookup=identity:real_identity

(denormalize the real_identity and rename it identity)

OUTPUT:

.. code:: json

   {
       "count": 3,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 1,
               "name": "Superman",
               "id": 1,
               "identity": {
                   "name": "Clark Kent",
                   "job": "Journalist",
                   "id": 1
               }
           },
           {
               "real_identity": 2,
               "name": "Spiderman",
               "id": 2,
               "identity": {
                   "name": "Peter Park",
                   "job": "Photographer",
                   "id": 2
               }
           },
           {
               "real_identity": 3,
               "name": "Batman",
               "id": 3,
               "identity": {
                   "name": "Bruce Wayne",
                   "job": "CEO",
                   "id": 3
               }
           }
       ],
       "timestamp": "2019-05-19T05:38:00.123218",
       "api_version": "0.1"
   }

URL:

::

   /superheroes/api/superhero?@lookup=identity!:real_identity[name,job]

(denormalize the real_identity [but only fields name and job], collapse
the with the identity prefix)

OUTPUT:

.. code:: json

   {
       "count": 3,
       "status": "success",
       "code": 200,
       "items": [
           {
               "name": "Superman",
               "identity.job": "Journalist",
               "identity.name": "Clark Kent",
               "id": 1
           },
           {
               "name": "Spiderman",
               "identity.job": "Photographer",
               "identity.name": "Peter Park",
               "id": 2
           },
           {
               "name": "Batman",
               "identity.job": "CEO",
               "identity.name": "Bruce Wayne",
               "id": 3
           }
       ],
       "timestamp": "2021-01-04T07:03:38.559918",
       "api_version": "0.1"
   }

URL:

::

   /superheroes/api/superhero?@lookup=superhero.tag

OUTPUT:

.. code:: json

   {
       "count": 3,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 1,
               "name": "Superman",
               "superhero.tag": [
                   {
                       "strength": 100,
                       "superhero": 1,
                       "id": 1,
                       "superpower": 1
                   },
                   {
                       "strength": 100,
                       "superhero": 1,
                       "id": 2,
                       "superpower": 2
                   },
                   {
                       "strength": 100,
                       "superhero": 1,
                       "id": 3,
                       "superpower": 3
                   },
                   {
                       "strength": 100,
                       "superhero": 1,
                       "id": 4,
                       "superpower": 4
                   }
               ],
               "id": 1
           },
           {
               "real_identity": 2,
               "name": "Spiderman",
               "superhero.tag": [
                   {
                       "strength": 50,
                       "superhero": 2,
                       "id": 5,
                       "superpower": 2
                   },
                   {
                       "strength": 75,
                       "superhero": 2,
                       "id": 6,
                       "superpower": 3
                   },
                   {
                       "strength": 10,
                       "superhero": 2,
                       "id": 7,
                       "superpower": 4
                   }
               ],
               "id": 2
           },
           {
               "real_identity": 3,
               "name": "Batman",
               "superhero.tag": [
                   {
                       "strength": 80,
                       "superhero": 3,
                       "id": 8,
                       "superpower": 2
                   },
                   {
                       "strength": 20,
                       "superhero": 3,
                       "id": 9,
                       "superpower": 3
                   },
                   {
                       "strength": 70,
                       "superhero": 3,
                       "id": 10,
                       "superpower": 4
                   }
               ],
               "id": 3
           }
       ],
       "timestamp": "2019-05-19T05:38:00.201988",
       "api_version": "0.1"
   }

URL:

::

   /superheroes/api/superhero?@lookup=superhero.tag.superpower

OUTPUT:

.. code:: json

   {
       "count": 3,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 1,
               "name": "Superman",
               "superhero.tag.superpower": [
                   {
                       "strength": 100,
                       "superhero": 1,
                       "id": 1,
                       "superpower": {
                           "id": 1,
                           "description": "Flight"
                       }
                   },
                   {
                       "strength": 100,
                       "superhero": 1,
                       "id": 2,
                       "superpower": {
                           "id": 2,
                           "description": "Strength"
                       }
                   },
                   {
                       "strength": 100,
                       "superhero": 1,
                       "id": 3,
                       "superpower": {
                           "id": 3,
                           "description": "Speed"
                       }
                   },
                   {
                       "strength": 100,
                       "superhero": 1,
                       "id": 4,
                       "superpower": {
                           "id": 4,
                           "description": "Durability"
                       }
                   }
               ],
               "id": 1
           },
           {
               "real_identity": 2,
               "name": "Spiderman",
               "superhero.tag.superpower": [
                   {
                       "strength": 50,
                       "superhero": 2,
                       "id": 5,
                       "superpower": {
                           "id": 2,
                           "description": "Strength"
                       }
                   },
                   {
                       "strength": 75,
                       "superhero": 2,
                       "id": 6,
                       "superpower": {
                           "id": 3,
                           "description": "Speed"
                       }
                   },
                   {
                       "strength": 10,
                       "superhero": 2,
                       "id": 7,
                       "superpower": {
                           "id": 4,
                           "description": "Durability"
                       }
                   }
               ],
               "id": 2
           },
           {
               "real_identity": 3,
               "name": "Batman",
               "superhero.tag.superpower": [
                   {
                       "strength": 80,
                       "superhero": 3,
                       "id": 8,
                       "superpower": {
                           "id": 2,
                           "description": "Strength"
                       }
                   },
                   {
                       "strength": 20,
                       "superhero": 3,
                       "id": 9,
                       "superpower": {
                           "id": 3,
                           "description": "Speed"
                       }
                   },
                   {
                       "strength": 70,
                       "superhero": 3,
                       "id": 10,
                       "superpower": {
                           "id": 4,
                           "description": "Durability"
                       }
                   }
               ],
               "id": 3
           }
       ],
       "timestamp": "2019-05-19T05:38:00.322494",
       "api_version": "0.1"
   }

URL (it's a single line, split for readability):

::

   /superheroes/api/superhero?
   @lookup=powers:superhero.tag[strength].superpower[description]

OUTPUT:

.. code:: json

   {
       "count": 3,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 1,
               "name": "Superman",
               "powers": [
                   {
                       "strength": 100,
                       "superpower": {
                           "description": "Flight"
                       }
                   },
                   {
                       "strength": 100,
                       "superpower": {
                           "description": "Strength"
                       }
                   },
                   {
                       "strength": 100,
                       "superpower": {
                           "description": "Speed"
                       }
                   },
                   {
                       "strength": 100,
                       "superpower": {
                           "description": "Durability"
                       }
                   }
               ],
               "id": 1
           },
           {
               "real_identity": 2,
               "name": "Spiderman",
               "powers": [
                   {
                       "strength": 50,
                       "superpower": {
                           "description": "Strength"
                       }
                   },
                   {
                       "strength": 75,
                       "superpower": {
                           "description": "Speed"
                       }
                   },
                   {
                       "strength": 10,
                       "superpower": {
                           "description": "Durability"
                       }
                   }
               ],
               "id": 2
           },
           {
               "real_identity": 3,
               "name": "Batman",
               "powers": [
                   {
                       "strength": 80,
                       "superpower": {
                           "description": "Strength"
                       }
                   },
                   {
                       "strength": 20,
                       "superpower": {
                           "description": "Speed"
                       }
                   },
                   {
                       "strength": 70,
                       "superpower": {
                           "description": "Durability"
                       }
                   }
               ],
               "id": 3
           }
       ],
       "timestamp": "2019-05-19T05:38:00.309903",
       "api_version": "0.1"
   }

URL (it's a single line, split for readability):

::

   /superheroes/api/superhero?
   @lookup=powers!:superhero.tag[strength].superpower[description]

OUTPUT:

.. code:: json

   {
       "count": 3,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 1,
               "name": "Superman",
               "powers": [
                   {
                       "strength": 100,
                       "description": "Flight"
                   },
                   {
                       "strength": 100,
                       "description": "Strength"
                   },
                   {
                       "strength": 100,
                       "description": "Speed"
                   },
                   {
                       "strength": 100,
                       "description": "Durability"
                   }
               ],
               "id": 1
           },
           {
               "real_identity": 2,
               "name": "Spiderman",
               "powers": [
                   {
                       "strength": 50,
                       "description": "Strength"
                   },
                   {
                       "strength": 75,
                       "description": "Speed"
                   },
                   {
                       "strength": 10,
                       "description": "Durability"
                   }
               ],
               "id": 2
           },
           {
               "real_identity": 3,
               "name": "Batman",
               "powers": [
                   {
                       "strength": 80,
                       "description": "Strength"
                   },
                   {
                       "strength": 20,
                       "description": "Speed"
                   },
                   {
                       "strength": 70,
                       "description": "Durability"
                   }
               ],
               "id": 3
           }
       ],
       "timestamp": "2019-05-19T05:38:00.355181",
       "api_version": "0.1"
   }

URL (it's a single line, split for readability):

::

   /superheroes/api/superhero?
   @lookup=powers!:superhero.tag[strength].superpower[description],
   identity!:real_identity[name]

OUTPUT:

.. code:: json

   {
       "count": 3,
       "status": "success",
       "code": 200,
       "items": [
           {
               "name": "Superman",
               "identity.name": "Clark Kent",
               "powers": [
                   {
                       "strength": 100,
                       "description": "Flight"
                   },
                   {
                       "strength": 100,
                       "description": "Strength"
                   },
                   {
                       "strength": 100,
                       "description": "Speed"
                   },
                   {
                       "strength": 100,
                       "description": "Durability"
                   }
               ],
               "id": 1
           },
           {
               "name": "Spiderman",
               "identity.name": "Peter Park",
               "powers": [
                   {
                       "strength": 50,
                       "description": "Strength"
                   },
                   {
                       "strength": 75,
                       "description": "Speed"
                   },
                   {
                       "strength": 10,
                       "description": "Durability"
                   }
               ],
               "id": 2
           },
           {
               "name": "Batman",
               "identity.name": "Bruce Wayne",
               "powers": [
                   {
                       "strength": 80,
                       "description": "Strength"
                   },
                   {
                       "strength": 20,
                       "description": "Speed"
                   },
                   {
                       "strength": 70,
                       "description": "Durability"
                   }
               ],
               "id": 3
           }
       ],
       "timestamp": "2021-01-04T07:31:34.974953",
       "api_version": "0.1"
   }

URL:

::

   /superheroes/api/superhero?name.eq=Superman

OUTPUT:

.. code:: json

   {
       "count": 1,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 1,
               "name": "Superman",
               "id": 1
           }
       ],
       "timestamp": "2019-05-19T05:38:00.405515",
       "api_version": "0.1"
   }

URL:

::

   /superheroes/api/superhero?real_identity.name.eq=Clark Kent

OUTPUT:

.. code:: json

   {
       "count": 1,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 1,
               "name": "Superman",
               "id": 1
           }
       ],
       "timestamp": "2019-05-19T05:38:00.366288",
       "api_version": "0.1"
   }

URL:

::

   /superheroes/api/superhero?not.real_identity.name.eq=Clark Kent

OUTPUT:

.. code:: json

   {
       "count": 2,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 2,
               "name": "Spiderman",
               "id": 2
           },
           {
               "real_identity": 3,
               "name": "Batman",
               "id": 3
           }
       ],
       "timestamp": "2019-05-19T05:38:00.451907",
       "api_version": "0.1"
   }

URL:

::

   /superheroes/api/superhero?superhero.tag.superpower.description=Flight

OUTPUT:

.. code:: json

   {
       "count": 1,
       "status": "success",
       "code": 200,
       "items": [
           {
               "real_identity": 1,
               "name": "Superman",
               "id": 1
           }
       ],
       "timestamp": "2019-05-19T05:38:00.453020",
       "api_version": "0.1"
   }


The RestAPI response
--------------------

All RestAPI response have the fields:

:api_version: RestAPI version.
:timestamp: Datetime in ISO 8601 format.
:status: RestAPI status (i.e. "success" or "error").
:code: HTTP status.

Other optional fields are:

:count: Total matching (not total returned), for GET.
:items: In response to a GET.
:errors: Usually a validation error.
:models: Usually if status != "success".
:message: For error details.


.. [CIT0801] https://en.wikipedia.org/wiki/Representational_state_transfer
.. [CIT0802] https://graphql.org/
