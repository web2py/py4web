## What is web3py?

WEB3PY is a web framework for rapid development of efficient database driven web applications. It is an evolution of the popular web2py framework but much faster and slicker. Its internal design has been much simplified compared to web2py.

WEB3PY can be seen as a competitor of other frameworks like Django or Flask, and it can indeed serve the same purpose. Yet WEB3PY aims to provide a larger feature set out of the box and reduce the development time of new apps.

Form an historical prospective our story starts in 2007 when web2py was first relased. web2py was designed to provide an all-inclusive solution for web development: one zip file containing the python interpreter, the framework, a web based IDE, and a collection of battle-tested packages that work well together. In many ways web2py has been immensely successful. Web2py succeeded in providing a low barrier of entry for new developers, a very secure development platform, and remaines backwards compatibile until today.

Web2py always suffered from one problem: its monolitic design. The most experienced Python developers did not understand how to use its components outside of the framework and how to use third party components within the framework. This was for good reason, as we did not care too much about them. We thought of web2py as a perfect tool that did not have to be broken into pieces because that would compromise its security. It turned out that we were wrong, and playing well with others is important. Hence, in the last two years we worked on three fronts:

- we ported web2py to python 3
- we broke web2py into modules that can be used independently
- we reassembled some of those modules into a new more modular framework ... WEB3PY.

WEB3PY is more than a repackaging of those modules. It is a complete redesign. It uses some of the web2py modules, but not all of them. In some cases, it uses other and better modules. Some functionality was removed and some was added. We tried to preserve most of the syntax and features that experienced web2py users loved. Here is a more explicit list:

- WEB3PY, unlike web2py, requires Python 3
- WEB3PY, unlike web2py, can be installed using pip and its dependecies are managed using requirements.txt
- WEB3PY apps are regular python modules. This is very different than web2py. In particular, we ditched the custom importer, and we rely now exclusively on the regular Python import mechanism.
- WEB3PY, like web2py, can serve multiple applications concurrently, as long as the apps are submodules of the apps module.
- WEB3PY, unlike web2py, is based on bottlepy and in particular uses the Bottle request object and the Bottle routing mechanism.
- WEB3PY, unlike web2py, does not create a new enviroment at every request. It introduces the concept of fixtures to explicitly declare which objects need to be re-initialized when a new http request is processed. This makes it much faster.
- WEB3PY, has a new sesson object which, like web2py's, provides strong security and encryption of the session data, but sessions are no longer stored in the file system - which created performance issues. It provides sessions in cookies, in redis, in memcache, or in database. We also limited session data to objects that are json serializable.
- WEB3PY, like web2py, has a built-in ticketing system but, unlike web2py, this system is global and not per app. Tickets are no longer stored in the filesystem with the individual apps. They are stored in a single database.
- WEB3PY, like web2py, is based on pydal but uses some new features of pydal (RESTAPI)
- WEB3PY, like web2py, uses the yatl template language but defaults to square brackets [[...]] delimiters to avoid conflicts with model JS fameworks, such as Vue.js and angular.js. Yatl includes a subset of the web2py helpers.
- WEB2PY, unlike web2py, uses the plularization library for internationalization. In practice, this exposes an object T very similar to web2py's T but it provides better caching and more flexible pluralization capabilities.
- WEB3PY comes with a Dashboard APP that replaces web2py's admin. This is a web IDE for uploading/managing/editings apps.
- WEB3PY's Dashboard includes a web based database interface. This replaces the appadmin functionality of web2py.
- WEB3PY comes with a Form object that is similar to web2py's SQLFORM but it is much simpler and faster. The syntax is the same. This has been provided in order to help users to port existing apps; but WEB3PY encourages using API based forms over postbacks.
- WEB3PY comes with an Auth object that replaces the web2py one. It is more modular and easier to extend. Out of the box, it provides the basic functionaly of register, login, logout, change password, request change password, edit profile as well as integration with PAM, SAML2, LDAP, OAUTH2 (google, facebook, and twitter).
- WEB3PY comes with some utilites like "tags", for instance, which allows adding searchable tags to any database table. It can be used, for example, to tag users with groups and search users by groups and apply permissions based on membership.
- WEB3PY comes with with some custom Vue.js components designed to interact with the PyDAL RESTAPI, and with WEB3PY in general. These APIs are designed to allow the server to set policies about which operations a client is allowed to perform, but give the client flexibility within those constraints. The two main components are mtable (which provides a web based interface to the database similar to web2py's grid) and auth (a customizable interface to the Auth API).

The goal of WEB3PY is and remains the same as web2py's: to make web development easy and accessible, while producing applications that are fast and secure.
