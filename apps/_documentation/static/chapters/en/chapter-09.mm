## Pluralize

Pluralize is a Python library for Internationalization (i18n) and Pluralization (p10n).

The library assumes a folder (for exaple "translations") that contains files like:

``
it.json
it-IT.json
fr.json
fr-FR.json
(etc)
``

Each file has the following structure, for example for Italian (it.json):

``
{"dog": {"0": "no cane", "1": "un cane", "2": "{n} cani", "10": "tantissimi cani"}}
``

The top level keys are the expressions to be translated and the associated value/dictionary maps a number to a translation.
Different translations correspond to different plural forms of the expression,

Here is another example for the word "bed" in Czech

``
{"bed": {"0": "no postel", "1": "postel", "2": "postele", "5": "postelí"}}
``

To translate and pluralize a string "dog" one simply warps the string in the T operator as follows:

``
>>> from pluralize import Translator
>>> T = Translator('translations')
>>> dog = T("dog")
>>> print(dog)
dog
>>> T.select('it')
>>> print(dog)
un cane
>>> print(dog.format(n=0))
no cane
>>> print(dog.format(n=1))
un cane
>>> print(dog.format(n=5))
5 cani
>>> print(dog.format(n=20))
tantissimi cani
``

The string can contain multiple placeholders but the {n} placeholder is special because
the variable called "n" is used to determine the pluralization by best match (max dict key <= n).

T(...) objects can be added together with each other and with string, like regular strings.

T.select(s) can parse a string s following the HTTP accept language format.

### Update the translation files

Find all strings wrapped in T(...) in .py, .html, and .js files:
``
matches = T.find_matches('path/to/app/folder')
``

Add newly discovered entries in all supported languages
``
T.update_languages(matches)
``

Add a new supported language (for example german, "de")

``
T.languages['de'] = {}
``

Make sure all languages contain the same origin expressions
``
known_expressions = set()
for language in T.languages.values():
    for expression in language:
        known_expressions.add(expression)
T.update_languages(known_expressions))
``

Finally save the changes:

``
T.save('translations')
``
