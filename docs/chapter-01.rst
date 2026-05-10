===============
What is py4web?
===============

PY4WEB is a web framework for rapid development of efficient database
driven web applications. It is an evolution of the popular web2py
framework, but much faster and slicker. Its internal design has been much
simplified compared to web2py.

PY4WEB can be seen as a competitor of other frameworks like Django or
Flask, and it can indeed serve the same purpose. Yet PY4WEB aims to
provide a larger feature set out of the box and to reduce the development
time of new apps.

From a historical perspective, our story starts in 2007 when web2py was
first released. web2py was designed to provide an all-inclusive solution
for web development: one zip file containing the Python interpreter, the
framework, a web based IDE, and a collection of battle-tested packages
that work well together. In many ways web2py has been immensely
successful. Web2py succeeded in providing a low barrier of entry for new
developers, a very secure development platform, and remains backwards
compatible until today.

Web2py always suffered from one problem: its monolithic design.
Experienced Python developers found it hard to use web2py's components
outside the framework, or to bring in third-party components. We
originally treated web2py as a self-contained tool that should not be
broken apart, because we believed that splitting it would weaken its
security guarantees. That turned out to be the wrong call: playing well
with others is important. So, starting in 2015, we worked on three
fronts:

-  We ported web2py to Python 3.
-  We broke web2py into modules that can be used independently.
-  We reassembled some of those modules into a new more modular
   framework … PY4WEB.

PY4WEB is more than a repackaging. It is a complete redesign.
It uses some of the web2py modules, but not all of them; in some cases
it switches to other, better modules. Some functionality was removed
and some was added. We tried to preserve most of the syntax and
features that experienced web2py users loved.


Here is a more explicit list (see :ref:`From web2py to py4web` for more
details if you come from web2py):

-  PY4WEB, unlike web2py, requires Python 3.
-  PY4WEB, unlike web2py, can be installed using pip, and its
   dependencies are managed using pyproject.toml
-  PY4WEB apps are regular Python modules. This is very different from
   web2py. In particular, we ditched the custom importer, and we rely
   now exclusively on the regular Python import mechanism.
-  PY4WEB, like web2py, can serve multiple applications concurrently, as
   long as the apps are submodules of the apps module.
-  PY4WEB, unlike web2py, is based on ombott (a reduced and faster
   spin-off of Bottle) and in particular uses a Bottle-compatible
   request object and routing mechanism.

-  PY4WEB, unlike web2py, does not create a new environment at every
   request. It introduces the concept of *fixtures* to explicitly
   declare which objects need to be (re)initialized when a new HTTP
   request arrives, or cleaned up when the request finishes. This makes
   it much faster than web2py.
-  PY4WEB has a new session object which, like web2py’s, provides strong
   security and encryption of the session data, but sessions are no
   longer stored in the file system — which created performance issues.
   It provides sessions in cookies, redis, memcache, or optionally
   in a database. We also limited session data to objects that are JSON
   serializable.
-  PY4WEB, like web2py, has a built-in ticketing system but, unlike
   web2py, this system is global and not per app. Tickets are no longer
   stored in the filesystem with the individual apps. They are stored in
   a single database.
-  PY4WEB, like web2py, is based on pydal but leverages some new features of
   pydal (RESTAPI).
-  PY4WEB, like web2py, uses the YATL template language but defaults
   to square-bracket delimiters (``[[ ... ]]``) to avoid conflicts with
   modern JS frameworks such as Vue.js and Angular. YATL includes a
   subset of the web2py helpers.
-  PY4WEB, unlike web2py, uses the pluralization library for
   internationalization. In practice, this exposes an object T very
   similar to web2py’s T but it provides better caching and more
   flexible pluralization capabilities.
-  PY4WEB comes with a Dashboard APP that replaces web2py’s admin. This
   is a web IDE for uploading/managing/editing apps.
-  PY4WEB’s Dashboard includes a web based database interface. This
   replaces the appadmin functionality of web2py.
-  PY4WEB comes with Form and Grid objects that are 
   similar to web2py’s SQLFORM and SQLFORM.grid.
-  PY4WEB comes with an Auth object that replaces the web2py one. It is
   more modular and easier to extend. Out of the box, it provides the
   basic functionality of register, login, logout, change password,
   request change password, edit profile as well as integration with
   PAM, SAML2, LDAP, OAUTH2 (google, facebook, and twitter).
-  PY4WEB leverages PyDAL's new tags functionality
   to tag users with groups, search users by groups, and
   apply permissions based on membership.
-  PY4WEB comes with some custom Vue.js components designed to
   interact with the PyDAL RESTAPI, and with PY4WEB in general. These
   APIs are designed to allow the server to set policies about which
   operations a client is allowed to perform, but give the client
   flexibility within those constraints. The two main components are
   mtable (which provides a web based interface to the database similar
   to web2py’s grid) and auth (a customizable interface to the Auth
   API).

The goal of PY4WEB is and remains the same as web2py’s: to make web
development easy and accessible, while producing applications that are
fast and secure.



Acknowledgments
---------------

Many thanks to everyone who has contributed to the project, and especially:


..
  Comment: the list in CONTRIBUTORS.rst has been moved to the end of the README.rst file

.. include:: ../README.rst
  :start-after: inclusion-marker-do-not-remove

Special thanks to Sam de Alfaro, who designed the official logo of py4web. We friendly call the logo "Axel the axolotl": it magically represents the sense of kindness and inclusion. We believe it's the cornerstone of our growing community.

.. image:: images/logo.png
