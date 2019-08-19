.PHONY: clean build assets install test deploy
clean:
	find . -name '*.pyc' -delete
	find . -name '*~' -delete
	find . -name '#*' -delete
	rm -rf dist/*
	python3 setup.py clean
assets:
	rm -f py4web/assets/*
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
	python3 -m pip install -r requirements.txt --user
	python3 -m pip install -r test-requirements.txt --user
	python3 -m pytest -v -s tests/
deploy: test
	python setup.py sdist
	twine upload dist/*
run:
	./py4web-start -p password.txt apps/