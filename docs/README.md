# py4web documentation
  
In this /doc folder you can see the source files for all the documentation, in RST format. Their translations are
in the /doc/locales folders, in PO format.

# help with the documentation

You can help us with the documentation, it's really simple! Just change the .RST and .PNG files in the /doc folder and create a Push Request on
the GitHub repository at https://github.com/web2py/py4web - you can even do it within your browser.
Once the PR is accepted, your changes will be written on the master branch, and will be reflected on the web pages / pdf / epub at
the next output generation on the branch. 

A good starting point for the RST format is this RST cheatsheet https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/CheatSheet.html
and also this tools walkthrough https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/ToolsEditRest/Index.html.

# obtaining outputs

When needed, all the sources are manually converted by the maintainers to HTML, PDF and EPUB file formats.
This could also be done by yourself using the enclosed updateDocs.sh script or the "make docs" command on the root py4web folder. The result
is placed in the /apps/_documentation/static folder in order to be read locally by the end users manually or with the _documentation py4web app.
The conversion is made with [Sphinx](https://www.sphinx-doc.org) and the result uses the
[Read the docs style](https://readthedocs.org/)


The updateDocs.sh program needs a Linux/Mac system with the packages
"rsync python3-sphinx python3-sphinx-rtd-theme python3-stemmer python3-git python3-pip python3-virtualenv python3-setuptools"
and the python3 modules "rinohtype pygments sphinx-tabs".
It accepts the **html** parameter (that builds/updates only the html outputs), or the **all** parameters that build also the PDF and EPUB files.
If lauched without any options it displays the help message.

After the updateDocs run, the results are available only locally.
If you use a local git repository and you wish to update the documentation to the remote repository, too, you have to force the changes
because they are not normally allowed by the py4web .gitignore file. In order to do it, you have to issue a 'git add --force apps/_documentation/*' from
the py4web folder. 

Please, do NOT make PR for publishing new outputs because we prefer to leave it to the maintainers. PR should contain .RST and .PNG files only. 


# Help with translations

If you want to help with translations, you are also welcome!
The translations files are in the /doc/locales folders, in PO format. For editing them, we strongly suggest the use of the free multiplatform program POEDIT v2 (https://poedit.net/)
Once you've finished your work with the PO files, just make a PR to the main py4web repository.

The current official translators are listed here:

* Portuguese: Carlos José da Costa (https://github.com/yamandu)
* Spanish:    Ricardo Strusberg (strusberg@gmail.com)


## New translation

If your language does not still exist in the documentation, for example the Italian one, you need to build its PO files. Setup a working environment as described before for updatDocs.sh, go to the
/docs folder and run:
```
make gettext
sphinx-intl update -p _build/gettext -l it
```
(where 'it' is the language code for Italian).  
This will create the PO files to be translated in `/docs/locales/it/LC_MESSAGES`

After their translation, make a PR for them. If you want, you can also generate the local HTML outputs as usual with the `updateDocs.sh` program.

## Update translation

When the english source files will be updated, the translated work will not be lost - but the new strings will appear inside your translated ones.
In order import the updated sources without loosing your previous work, you need to run:
```
sphinx-build -b gettext . _build/gettext
```
This creates the updates .pot files on /docs/_build/gettext. 
With poedit you have to load the old translated .po file in your language. Then you use the menu "Catalog" -> "Update from POT file ..." in order to collect the updates from the .pot file.
The new additions / changes will be loaded and marked to be fixed. You can now save the updated PO file and work on it. 

