# py4web documentation
  
In this folder you can see the source files for all the documentation, in RST format.

When needed, they are manually converted to HTML, PDF and EPUB file formats (using the enclosed updateDocs.sh
script). The result is also placed in the _documentation py4web app in order to be read locally by the end users.
The conversion is made with [Sphinx](https://www.sphinx-doc.org) and the result uses the
[Read the docs style](https://readthedocs.org/)

NOTE: if you use a local git repository and you wish to update the documentation to the remote repository, too, you have to force the changes
because they are not normally allowed by .gitignore. In order to do it, you have to issue a 'git add --force apps/_documentation/*' from
the py4web folder
