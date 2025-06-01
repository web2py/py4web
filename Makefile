.PHONY: clean docs clean-assets assets test setup run build deploy
asset-apps := _dashboard _default _scaffold _minimal _documentation showcase
asset-zips := $(asset-apps:%=py4web/assets/py4web.app.%.zip)
clean:
	find . -name '*.pyc' -delete
	find . -name '*~' -delete
	find . -name '#*' -delete
	rm -rf dist/*
	rm -rf build/*
	rm -rf py4web.egg-info

clean-assets: clean
	rm -f py4web/assets/*
	mkdir -p py4web/assets

assets: clean-assets $(asset-zips)

py4web/assets/py4web.app.%.zip: apps/%
	cd $< && find . | \
	egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt|mm|ico)$$" | \
	zip -@ $(addprefix ../../, $@)

uv:
	which uv || curl -LsSf https://astral.sh/uv/install.sh | sh

lock: uv
	uv lock

docs: uv
	docs/updateDocs.sh html

check: uv
	uv tool run ruff check

format: uv
	uv tool run ruff format

test: uv
	uv run --extra test pytest --cov=py4web --cov-report html:cov.html -v tests/

setup: uv
	uv run py4web.py setup apps
	uv run py4web.py set_password

run: uv
	uv run py4web.py run -p password.txt apps -L20

build: clean assets check test
	uv build --sdist --wheel

publish:
	uv run --extra manage python -m twine upload dist/*

upgrade-utils:
	find apps -name "utils.js" -exec cp apps/_dashboard/static/js/utils.js {} \;

upgrade-vue:
	curl -L https://unpkg.com/vue/dist/vue.min.js > apps/_dashboard/static/js/vue.min.js
	find apps -name "vue.min.js" -exec cp apps/_dashboard/static/js/vue.min.js {} \;

requirements.txt:
	uv sync --no-dev
	uv pip freeze > requirements.txt
