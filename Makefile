.PHONY: clean build install test deploy
clean:
	find . -name '*.pyc' -delete
	find . -name '*~' -delete
	find . -name '#*' -delete
	rm -rf dist/*
	python3 setup.py clean
build: clean
	python3 setup.py build
install: build
	python3 setup.py install
test: build
	pip3 install -r requirements.txt
	python3 -m pytest -v -s tests/
deploy: test
	python setup.py sdist
	twine upload dist/*
