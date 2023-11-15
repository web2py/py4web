.PHONY: clean venv docs clean-assets assets test setup run build deploy
asset-apps := _dashboard _default _scaffold _minimal _documentation showcase
asset-zips := $(asset-apps:%=py4web/assets/py4web.app.%.zip)
clean:
	find . -name '*.pyc' -delete
	find . -name '*~' -delete
	find . -name '#*' -delete
	rm -rf dist/*
clean-assets:
	rm -f py4web/assets/*
	mkdir -p py4web/assets
assets: clean-assets $(asset-zips)
py4web/assets/py4web.app.%.zip: apps/%
	cd $< && find . | \
	egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt|mm|ico)$$" | \
	zip -@ $(addprefix ../../, $@)
venv:
	python -m venv venv
	venv/bin/pip install -U pip
	venv/bin/pip install -U -r requirements.txt
	venv/bin/pip install ./
docs: venv
	venv/bin/pip install -U -r docs/requirements.txt
	cd docs; . ../venv/bin/activate && ./updateDocs.sh html
test: venv
	venv/bin/pip install -U -r test-requirements.txt
	venv/bin/python -m pytest --cov=py4web --cov-report html:cov.html -v tests/
setup:
	venv/bin/python py4web.py setup apps
	venv/bin/python py4web.py set_password
run:
	venv/bin/python py4web.py run -p password.txt apps
upgrade-utils:
	find apps -name "utils.js" -exec cp apps/_dashboard/static/js/utils.js {} \;
upgrade-vue:
	curl -L https://unpkg.com/vue/dist/vue.min.js > apps/_dashboard/static/js/vue.min.js
	find apps -name "vue.min.js" -exec cp apps/_dashboard/static/js/vue.min.js {} \;
build: clean assets
	python -m pip install --upgrade build
	python -m pip install --upgrade twine
	python -m build
deploy: build
	python -m twine upload dist/*
