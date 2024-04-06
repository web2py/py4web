# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

#import sys
#sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'py4web'
copyright = '2020, BSDv3 License'
author = 'Massimo Di Pierro'

# The full version, including alpha/beta/rc tags

# get current_version from sources
pkg_init = '../py4web/__init__.py'
with open(pkg_init, 'r') as src:
    for line in src:
        if '__version__ = ' in line:
            values = line.split(sep = ' = ')
            current_version = values[1].strip('\n').strip('"')
            break
release = current_version
version = current_version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
    'sphinxcontrib.spelling',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# How to format the current date, used as the replacement for |today|
today_fmt = "%B %d, %Y"

# The default language to highlight source code in literal blocks.
# The value should be a valid Pygments lexer name,
# 'default' it is similar to 'python3'; it is mostly a superset of
# 'python' but it fallbacks to 'none' without warning if failed.
highlight_language = 'none'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = 'images/logo.png'
html_favicon = 'images/logo-32x32.ico'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}
# The master toctree document.
master_doc = 'index'

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ["_static/css"]

html_css_files = ["css/toggle.css"]
html_js_files = ["js/toggle.js"]

############################
# SETUP THE RTD LOWER-LEFT #
############################
try:
   html_context
except NameError:
   html_context = dict()
html_context['display_lower_left'] = True

# SET CURRENT_LANGUAGE
if 'current_language' in os.environ:
   # get the current_language env var set by buildDocs.sh
   current_language = os.environ['current_language']
else:
   # the user is probably doing `make html`
   # set this build's current language to english
   current_language = 'en'

# tell the theme which language to we're currently building
html_context['current_language'] = current_language

# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version

# POPULATE LINKS TO OTHER LANGUAGES
#html_context['languages'] = [ ('en', 'en/') ]
html_context['languages'] = [ ('en', '../en' + '/index.html') ]

languages = [lang.name for lang in os.scandir('locales') if lang.is_dir()]
for lang in languages:
   #html_context['languages'].append( (lang, lang + '/' ) )
   #html_context['languages'].append( (lang, '/../' + lang + '/' ) )
   html_context['languages'].append( (lang, '../' + lang + '/index.html') )

# POPULATE LINKS TO OTHER VERSIONS
html_context['versions'] = list()
#html_context['versions'].append( ('master', current_language + '/' ) )
html_context['versions'].append( ('current', 'index.html' ) )
#html_context['versions'].append( ('current', '/' ) )

# POPULATE LINKS TO OTHER FORMATS/DOWNLOADS
html_context['downloads'] = list()
html_context['downloads'].append( ('pdf', project + '_' + current_language + '.pdf') )
html_context['downloads'].append( ('epub', project + '_' + current_language + '.epub') )

##########################
# "EDIT ON GITHUB" LINKS #
##########################
html_context['display_github'] = True
html_context['github_user'] = 'web2py'
html_context['github_repo'] = 'py4web'
html_context['github_version'] = 'master/docs/'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',

    # Latex figure (float) alignment.
    #'figure_align': 'htbp',
}


# -- Options for PDF output --------------------------------------------------

# settings for creating PDF with rinoh
rinoh_documents = [dict(
    doc = master_doc,
    target = 'target',
    title = project + ' Documentation',
    date = '© ' + copyright,
    logo = 'images/logo.png'
)]


# -- Options for EPUB output -------------------------------------------------
epub_basename = 'target'


# ---- Options for spelling  -------------------------------------------------
spelling_lang='en_US'
spelling_word_list_filename='spelling_wordlist_en.txt'