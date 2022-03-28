#!/bin/bash
# vim: set ts=4 noet ai:

#
#  nicozanf@gmail.com - 2020.11.16
# For more information on how this documentation is built using Sphinx,
# Read the Docs, and GitHub Actions/Pages, see:
#  
#  * https://tech.michaelaltfield.net/2020/07/18/sphinx-rtd-github-pages-1
#     thank you Michael Altfield!
#
 
t=${1:-help}
if [ $t != 'all' -a $t != 'html' ]; then
	cat << EOF
##############################################################################
File:    $0

Purpose: A script that builds py4web documentation using Sphinx and updates
          Pages. This script must be executed manually
Needs:   A Linux system with the packages "rsync python3-sphinx
          python3-sphinx-rtd-theme python3-stemmer
          python3-git python3-pip python3-virtualenv python3-setuptools"
          and the python3 modules "rinohtype pygments"

How to run: "$0 [all|html]" from  inside the docs folder
##############################################################################

EOF
	exit 0
fi

#####################
# DECLARE VARIABLES #
#####################

# go to py4web root folder
cd ..

project_name=py4web
destination=apps/_documentation/static

# check for docs dir & sphinx config
if [ ! -e docs/conf.py ]; then
	echo "$0: missing docs/conf.py" 1>&2
	exit 1
fi

# check for _documentation app
if [ ! -e ${destination} ]; then
	echo "$0: missing _documentation app" 1>&2
	exit 1
fi

##############
# BUILD DOCS #
##############

# abort on nonzero exit status
set -o errexit

# cleanup old sphinx builds
make -C docs clean

languages='en '
# find other available languages (translations)
languages+=$(find docs/locales/ -mindepth 1 -maxdepth 1 -type d -exec basename \{\} \;)

# use a temp dir as docroot
docroot=$(mktemp -d)

for current_language in ${languages}; do

	echo "Building for ${current_language}"
	# make the current language available to conf.py
	export current_language

	# make spelling if english
	if [ ${current_language} = 'en' ]
	then
	sphinx-build -b spelling docs/ docs/_build/spelling
	fi	

	# make HTML
	# NOTE: this affect files in docs/locales/${current_language}/LC_MESSAGES/	sphinx-build -b html -D language="${current_language}" docs/ docs/_build/html/${current_language}
	sphinx-build -b html -D language="${current_language}" docs/ docs/_build/html/${current_language}
	mkdir -p "${docroot}/${current_language}"

	base_target="${docroot}/${current_language}/${project_name}_${current_language}"
	if [ $t = 'all' ]
	then
		# make PDF
		sphinx-build -b rinoh -D language="${current_language}" docs/ docs/_build/rinoh
		cp docs/_build/rinoh/target.pdf "${base_target}.pdf"

		# make EPUB
		sphinx-build -b epub -D language="${current_language}" docs/ docs/_build/epub
		cp docs/_build/epub/target.epub "${base_target}.epub"
	else
		# HTML only, backup previous pdf and epub if any
		target_pdf="${base_target}.pdf"
		if [ -e "${target_pdf}" ]; then
			cp "${target_pdf}" "${docroot}/${current_language}"
		else
			echo "WARNING: ${target_pdf} not found"
		fi
		target_epub="${base_target}.epub"
		if [ -e "${target_epub}" ]; then
			cp "${target_epub}" "${docroot}/${current_language}"
		else
			echo "WARNING: ${target_epub} not found"  
		fi 
	fi

	# removes unuseful folders
	rm -fr docs/_build/html/${current_language}/.doctrees
	rm -fr docs/_build/html/${current_language}/_sources

	# copy html files into docroot
	rsync -a docs/_build/html/ ${docroot}

done

# copy favicon
favicon=apps/_scaffold/static/favicon.ico
cp ${favicon} ${docroot}

# final cleanup
make -C docs clean

# move docroot to destination
rm -fr ${destination}
#mv ${docroot} ${destination}
rsync -a "${docroot}/" ${destination} && rm -r ${docroot}

################
# CUSTOM INDEX #
################

echo "Writing ${destination}/index.html"

cat > ${destination}/index.html <<EOF
<!DOCTYPE html>
<html>
   <head>
      <title>${project_name} Docs</title>
      <meta http-equiv = "refresh" content="0; url='en/index.html'" />
   </head>
   <body>
      <p>Please wait while you're redirected to our documentation.</p>
   </body>
</html>
EOF
