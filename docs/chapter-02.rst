=========================
Help, resources and hints
=========================

We've done our best to make PY4WEB simple and clean. Even so, modern
web programming is a broad topic: a single feature can pull you across
Python, HTML, JavaScript, CSS, and the database, sometimes within the
same screen. Don't be intimidated — this manual walks you through it
step by step, and the rest of this chapter points to other valuable
resources that complement it.


Resources
=========

This manual
-----------

This manual is the Reference Manual for py4web. It's available online at https://py4web.com/_documentation/static/index.html, where you'll also find the 
PDF and EBOOK version, in multiple languages. It is written in RestructuredText and generated using Sphinx.


The Google group
----------------

There is a dedicated mailing list hosted on Google Groups, see https://groups.google.com/g/py4web. This is the main source of discussions for developers
and simple users. For any problem you should face, this is the right place to search for a hint or a solution.


The Discord server
-------------------

For quick questions and chats you can also use the free `Discord server dedicated to py4web <https://discord.gg/xCzQ9KTk3W>`__. You could usually find
many py4web developers hanging out in the channel. 


Tutorials and video
-------------------

There are many tutorials and videos available. Here are some of them:

- the `Learn Py4Web site <https://learn-py4web.github.io>`__ by Luca de Alfaro (with lots of excellent training videos)
- the free video `course 2020 by Luca de Alfaro <https://sites.google.com/a/ucsc.edu/luca/classes/cmps-183-hypermedia-and-the-web/cse-183-spring-2020>`__
  at UC Santa Cruz
- the `py4web blog app <https://github.com/agavgavi/py4web-blog-app.git>`__ by Andrew Gavgavian,  which uses py4web to replicate the famous Corey
  Schafer's tutorial series on creating a blog app in Django
- the `South Breeze Enterprises demo app <https://github.com/jpsteil/southbreeze>`__ by `Jim Steil <https://github.com/jpsteil>`__.  It is built around
  the structure of the Microsoft Northwind database,
  but converted to SQLite. You can view the final result online `here <https://southbreeze.pythonbench.com>`__
- the `py4web blog in spanish <https://py4web-tutoriales.blogspot.com>`__ by Alan Etkin, which covers the basics to start with the framework plus examples. It is intended as a resource for students and aims to provide a full web development course

The sources on GitHub
---------------------

Last but not least, py4web is Open Source, with a BSD v3 license, hosted on GitHub at https://github.com/web2py/py4web. This means that you can read,
study and experiment with all of its internal details by yourself.


Hints and tips
==============

This paragraph is dedicated to preliminary hints, suggestions and tips that could be helpful to know before starting to learn py4web.


Prerequisites
-------------

To follow this manual you need at least a basic Python knowledge.
There are many books, courses and tutorials freely available on the
web — pick what works for you. One Python feature you should be
comfortable with before going further is **decorators**: py4web uses
them everywhere to attach behavior (routes, fixtures, authentication)
to ordinary Python functions. If ``@something`` syntax is still
mysterious, take a moment to read the
`Python decorators tutorial <https://docs.python.org/3/glossary.html#term-decorator>`__
before continuing.

A modern Python workspace
-------------------------

In the following chapters you'll start writing code on your own
machine. A few small investments now will pay off many times over:

- **Use an IDE.** Even for simple examples, an Integrated Development
  Environment gives you syntax checking, linting and a visual
  debugger. The two free, multi-platform options most py4web
  developers use are Microsoft
  `Visual Studio Code <https://code.visualstudio.com/>`__ (VS Code)
  and JetBrains `PyCharm <https://www.jetbrains.com/pycharm/>`__.
- **Use a virtual environment** (a *virtualenv*; see
  `the official tutorial <https://docs.python.org/3/tutorial/venv.html>`__
  for an introduction). It keeps the libraries used by your project
  isolated from the rest of your system, so installing or upgrading
  one project never breaks another.
- **Use git** to track every change you make and back the history up
  to a hosting service (GitHub, GitLab or Bitbucket). At some point
  you *will* break something — git is how you go back.


Debugging py4web with VS Code
-----------------------------

It's quite simple to run and debug py4web within VS Code.

If you have **installed py4web from source**, you just need to open the main py4web folder (not the apps folder!) with VS Code and add:

::

  "args": ["run", "apps"],
  "program": "your_full_path_to_py4web.py",

to the vscode ``launch.json`` configuration file. Note that if you're using Windows the "your_full_path_to_py4web.py" parameter must be written using
forward slash only, like
"C:/Users/your_name/py4web/py4web.py".

If you have instead **installed py4web from pip,** you need to set the launch.json file to run py4web as a module

::

  {
    "name": "py4web apps",
    "type": "debugpy",
    "request": "launch",
    "module": "py4web",
    "args": ["run", "apps", "-D", "--watch", "lazy"]
  }

Adjust the `args` to match your apps folder. For example, replace `apps` with `.` if you opened the apps folder itself in VS Code.

.. tip::

   In both cases, if you get gevent errors, also add ``"gevent": true`` to the ``launch.json`` configuration file.


Debugging py4web with PyCharm
-----------------------------

In PyCharm, if you get gevent errors, enable Settings → Build, Execution, Deployment → Python Debugger → Gevent compatible.


How to contribute
=================

We need help from everyone: support our efforts! You can just participate in the Google group trying to answer others' questions, submit bugs or
create pull requests on the GitHub repository.

If you wish to correct and expand this manual, or even translate it
into a new language, you can read all the information you need on the
`specific README <https://github.com/web2py/py4web/blob/master/docs/README.md>`__
on GitHub.

It's really simple: edit the ``.rst`` files in the ``docs/`` folder
and open a pull request against
https://github.com/web2py/py4web — you can do it from your browser.
Once the PR is accepted, your changes are merged to ``master`` and
appear in the web, PDF and EPUB outputs the next time the docs are
rebuilt.

