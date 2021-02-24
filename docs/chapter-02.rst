=========================
Help, resources and hints
=========================

We've made our best to make PY4WEB simple and clean. But you know, modern web programming is a daunting task. It requires an open mind, able to
jump frequently (without being lost!) from python to HTML to javascript to css and even database management. 
But don't be scared, in this manual we'll assist you side by side in this journey. And there are many other valuable resources that we're going to show you.


Resources
=========

This manual
-----------

This manual is the Reference Manual for py4web. It's available online at https://py4web.com/_documentation/static/index.html, where you'll also find the PDF
and EBOOK version, in multiple languages. 
It was originally written with the MarkMin format (similar to MarkDown) and displayed in HTML with a custom py4web application. In 2020 we decided to
convert its sources to the RST format which is better suited for technical documentation. Using Sphinx and the ReadTheDocs style we are now able to achieve
high quality outputs.


The Google group
----------------

There is a dedicated mailing list hosted on Google Groups, see https://groups.google.com/g/py4web. This is the main source of discussions for developers and
simple users. For any problem you should face, this is the right place to search for a hint or a solution.

The chat on IRC
---------------

We also use to chat sometime on IRC (Internet Relay Chat, which is an old-style text only chat). You can freely join us at https://webchat.freenode.net/#py4web.
From time to time we also use it to host a scheduled public chat, where you can write and read live questions to developers.
Transcripts of them are then available on the mailing list.


Tutorials and video
-------------------

There are many tutorials and videos if you like them. Generally, you can search for them on `YouTube <https://www.youtube.com/results?search_query=py4web>`__.

Here are some of them:

- the free video `course by Luca de Alfaro <https://sites.google.com/a/ucsc.edu/luca/classes/cmps-183-hypermedia-and-the-web/cse-183-spring-2020>`__ at UC Santa Cruz. 
- the `py4web blog app <https://github.com/agavgavi/py4web-blog-app.git>`__ by Andrew Gavgavian,  which uses py4web to replicate the famous Corey Schafer's tutorial series on creating a blog app in Django


The sources on GitHub
---------------------

Last but not least, py4web is Open Source, with a BSD v3 licence, hosted on GitHub at https://github.com/web2py/py4web. This means that you can read, study and experiment
with all of its internal details by yourself.


Hints and tips
==============

This paragraph is dedicated to preliminary hints, suggestions and tips that could be helpful to know before starting to learn py4web.


Prerequisites
-------------

In order to understand py4web you need at least a basic python knowledge. There are many books, courses and tutorials available on the web - choose what's best for you.
The python's decorators, in particular, are a milestone of any python web framework and you have to fully understand it.

A modern python workplace
-------------------------

In the following chapters you will start coding on your computer. We suggest you to setup a modern python workplace if you plan to do it efficiently and safely.
Even for running simple examples and experimenting a little, we strongly suggest to use an **Integrated Development Environment** (IDE). This will make your programming experience much better, allowing syntax checking, linting and visual debugging.
Nowadays there are two free and multiplatform main choices: Microsoft Visual Studio Code aka `VScode <https://code.visualstudio.com/>`__ and
JetBrains `PyCharm <https://www.jetbrains.com/pycharm/>`__.

When you'll start to deal with more complex programs and need reliability,
we also suggest to:

- use virtual environments (also called **virtualenv**, see
  `here <https://docs.python.org/3.7/tutorial/venv.html>`__ for an
  introduction). In a complex workplace this will avoid to be messed up
  with other python programs and modules
- use a Concurrent Versions System (**CVS**). Keeping track of your
  program's changes is highly valuable - along with backups it will save
  your computing life! Git and GitHub are the current standards.


Debugging py4web with VScode
----------------------------

In order to run py4web.py directly, you need to add ``"args": ["run", "apps"]`` to the vscode launch.json configuration file.
In addition, if you should get gevent errors you have to add ``"gevent": true`` on the same configuration file.

Debugging py4web with PyCharm
-----------------------------

In PyCharm, if you should get gevent errors you need to enable Settings | Build, Execution, Deployment | Python Debugger | Gevent compatible.


How to contribute
=================

We need help from everyone: support our efforts! You can just partecipate in the Google group trying to answer other's questions, submit bugs using or create pull requests on the GitHub
repository.

If you wish to correct and expand this manual, or even translate it in a new foreign language, you can read all the needed information directly on the
`specific README <https://github.com/web2py/py4web/blob/master/docs/README.md>`__ on GitHub.

It's really simple! Just change the .RST files in the /doc folder and create a Push Request on
the GitHub repository at https://github.com/web2py/py4web - you can even do it within your browser.
Once the PR is accepted, your changes will be written on the master branch, and will be reflected on the web pages / pdf / epub at
the next output generation on the branch. 


