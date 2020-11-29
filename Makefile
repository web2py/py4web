.PHONY: clean build docs assets install test deploy
clean:
	find . -name '*.pyc' -delete
	find . -name '*~' -delete
	find . -name '#*' -delete
	rm -rf dist/*
	python3 setup.py clean
docs:
	# cd docs; ./updateDocs.sh all
assets: docs
	rm -f py4web/assets/*
	mkdir -p py4web/assets
	cd apps/_dashboard; \
	find . | egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt)$$" | \
	zip -@ ../../py4web/assets/py4web.app._dashboard.zip
	cd apps/_default; \
	find . | egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt)$$" | \
	zip -@ ../../py4web/assets/py4web.app._default.zip
	cd apps/_scaffold; \
	find . | egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt)$$" | \
	zip -@ ../../py4web/assets/py4web.app._scaffold.zip
	cd apps/_minimal; \
	find . | egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt)$$" | \
	zip -@ ../../py4web/assets/py4web.app._minimal.zip	
	cd apps/_documentation; \
	find . | egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt|mm)$$" | \
	zip -@ ../../py4web/assets/py4web.app._documentation.zip
build: clean assets
	python3 setup.py build
install: build
	python3 setup.py install
test: build
	python3 -m pip install -r requirements.txt
	python3 -m pip install -r test-requirements.txt
	python3 -m pytest --cov=py4web --cov-report html:cov.html -v -s tests/
push:	test
	git push origin master
deploy: test
	python2.7 setup.py sdist
	twine upload dist/*
setup:
	./py4web.py setup apps
	./py4web.py set_password
run:
	./py4web.py run -p password.txt apps
upgrade-utils:
	find apps -name "utils.js" -exec cp apps/_dashboard/static/js/utils.js {} \;
upgrade-axios:
	curl -L https://unpkg.com/axios/dist/axios.min.js > apps/_dashboard/static/js/axios.min.js
	find apps -name "axios.min.js" -exec cp apps/_dashboard/static/js/axios.min.js {} \;
upgrade-vue:
	curl -L https://unpkg.com/vue/dist/vue.min.js > apps/_dashboard/static/js/vue.min.js
	find apps -name "vue.min.js" -exec cp apps/_dashboard/static/js/vue.min.js {} \;

