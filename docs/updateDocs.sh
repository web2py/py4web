#!/usr/bin/env bash

set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

if [[ ! $# -ge 1 || ( ! ${1} = 'all' && ! ${1} = 'html' ) ]]
then

    echo ' '
    echo '################################################################################'
    echo 'File:    updateDocs.sh'
    echo
    echo 'Purpose: A script that builds py4web documentation using Sphinx and updates'
    echo '          Pages. This script must be executed manually'
    echo 'Needs:   A Linux system with the packages "rsync python3-sphinx'
    echo '          python3-sphinx-rtd-theme python3-stemmer'
    echo '          python3-git python3-pip python3-virtualenv python3-setuptools"'
    echo '          and the python3 modules "rinohtype pygments"'
    echo
    echo 'How to run: "./updateDocs.sh [all|html]" from  inside the docs folder' 
    echo '################################################################################'
    echo
    
    exit 0
fi

set -x

#
#  nicozanf@gmail.com - 2020.11.16
# For more information on how this documentation is built using Sphinx, Read the Docs, and GitHub Actions/Pages, see:
#  
#  * https://tech.michaelaltfield.net/2020/07/18/sphinx-rtd-github-pages-1
#     thank you Michael Altfield!
#
 
#####################
# DECLARE VARIABLES #
#####################
  
pwd
ls -lah

# switching to root py4web folder
cd ..

pwd  

# exit if it doesn't have our docs dir & sphinx config
if [ ! -e 'docs/conf.py' ]; then
  echo -e "\tERROR: Couldn't find 'docs/conf.py'"
  exit 1
fi

destination="apps/_documentation/static"
# exit if it doesn't have our documentation app
if [ ! -e ${destination} ]; then
  echo -e "\tERROR: Couldn't find _documentation app!"
  exit 1
fi 


# make a new temp dir which will be our Pages docroot
docroot=`mktemp -d`
 
export PROJECT_NAME="py4web"
  
##############
# BUILD DOCS #
##############

# first, cleanup any old builds' static assets
make -C docs clean
  

# make the current language available to conf.py
languages="en `find docs/locales/ -mindepth 1 -maxdepth 1 -type d -exec basename '{}' \;`"

for current_language in ${languages}; do

  # make the current language available to conf.py
  export current_language

  ##########
  # BUILDS #
  ##########
  echo "INFO: Building for ${current_language}"

  # make HTML #
  sphinx-build -b html -D language="${current_language}" docs/ docs/_build/html/${current_language}
  mkdir -p "${docroot}/${current_language}"

  if [ ${1} = 'all' ]
  then
	  # make PDF #
	  sphinx-build -b rinoh -D language="${current_language}" docs/ docs/_build/rinoh
	  cp "docs/_build/rinoh/target.pdf" "${docroot}/${current_language}/${PROJECT_NAME}_${current_language}.pdf"

	  # make EPUB #
	  sphinx-build -b epub docs/ docs/_build/epub -D language="${current_language}"
	  cp "docs/_build/epub/target.epub" "${docroot}/${current_language}/${PROJECT_NAME}_${current_language}.epub"
  else
  	  # HTML only - backup previous pdf and epub if they exist #
  	  mkdir -p "${docroot}/${current_language}"
         destination_pdf="${destination}/${current_language}/${PROJECT_NAME}_${current_language}.pdf"
         if [ -e ${destination_pdf} ]; then
           cp "${destination_pdf}" "${docroot}/${current_language}"
         else
           echo "** WARNING ** : ${destination_pdf} not found!"
         fi
         destination_epub="${destination}/${current_language}/${PROJECT_NAME}_${current_language}.epub"
         if [ -e ${destination_epub} ]; then
           cp "${destination_epub}" "${docroot}/${current_language}"
         else
           echo "** WARNING ** : ${destination_epub} not found!"  
         fi 
  fi

  # copy the static html assets produced by the above build into our docroot
  rsync -av "docs/_build/html/" "${docroot}/"

done
  
  
#######################
# Update Pages #
#######################

# cleanup any remaining builds' static assets
make -C docs clean


# cleanup destination folder & copy new docs
rm -r ${destination}
rsync -av "${docroot}/" ${destination}
rm -r ${docroot}
  
# add redirect from the docroot to our default docs language/version
cat > "${destination}/index.html" <<EOF
<!DOCTYPE html>
<html>
   <head>
      <title>${PROJECT_NAME} Docs</title>
      <meta http-equiv = "refresh" content="0; url='en/index.html'" />
   </head>
   <body>
      <p>Please wait while you're redirected to our documentation.</p>
   </body>
</html>
EOF


set +x

echo
echo "#######################"
echo "# Finished            #"
echo "#######################"
echo
echo "FINISHED! Look the results on ${destination}/index.html"
echo
  
  
# exit cleanly
exit 0
