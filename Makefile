.PHONY: clean build assets install test deploy
clean:
	find . -name '*.pyc' -delete
	find . -name '*~' -delete
	find . -name '#*' -delete
	rm -rf dist/*
	python3 setup.py clean
assets:
	rm -f web3py/assets/*
	cd apps/_dashboard; \
	find . | egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt)$$" | \
	zip -@ ../../web3py/assets/web3py.app._dashboard.zip
	cd apps/_default; \
	find . | egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt)$$" | \
	zip -@ ../../web3py/assets/web3py.app._default.zip
	cd apps/_scaffold; \
	find . | egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt)$$" | \
	zip -@ ../../web3py/assets/web3py.app._scaffold.zip
	cd apps/_minimal; \
	find . | egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt)$$" | \
	zip -@ ../../web3py/assets/web3py.app._minimal.zip
	cd apps/_documentation; \
	find . | egrep "\.(py|html|css|js|png|jpg|gif|json|yaml|md|txt|mm)$$" | \
	zip -@ ../../web3py/assets/web3py.app._documentation.zip
build: clean assets
	python3 setup.py build
install: build
	python3 setup.py install
test: build
	pip3 install -r requirements.txt
	python3 -m pytest -v -s tests/
deploy: test
	python setup.py sdist
	twine upload dist/*
run:
	./web3py-start -p password.txt apps/