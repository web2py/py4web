.PHONY: clean docs clean-assets assets tests setup run build deploy
asset-apps := _dashboard _default _scaffold _minimal _documentation showcase
asset-zips := $(asset-apps:%=py4web/assets/py4web.app.%.zip)
clean:
	find . -name '*.pyc' -delete
	find . -name '*~' -delete
	find . -name '#*' -delete
	rm -rf dist/*
clean-assets: clean
	rm -f py4web/assets/*
	mkdir -p py4web/assets
assets: clean-assets $(asset-zips)
py4web/assets/py4web.app.%.zip: apps/%
	cd $< && find . | \
	egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt|mm|ico)$$" | \
	zip -@ $(addprefix ../../, $@)
docs:
	pip install -U -r docs/requirements.txt
	cd docs; ./updateDocs.sh html
tests:
	pip install -U -r test-requirements.txt
	python -m pytest --cov=py4web --cov-report html:cov.html -v tests/
setup:
	python py4web.py setup apps
	python py4web.py set_password
run:
	python py4web.py run -p password.txt apps -L20
upgrade-utils:
	find apps -name "utils.js" -exec cp apps/_dashboard/static/js/utils.js {} \;
upgrade-vue:
	curl -L https://unpkg.com/vue/dist/vue.min.js > apps/_dashboard/static/js/vue.min.js
	find apps -name "vue.min.js" -exec cp apps/_dashboard/static/js/vue.min.js {} \;
build: clean assets
	pip install --upgrade build
	pip install --upgrade twine
	python -m build
deploy: build
	python -m twine upload dist/*
install:
	python -m pip install .
