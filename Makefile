.PHONY: clean build install test
clean:
	find . -name '*.pyc' -delete
	find . -name '*~' -delete
	find . -name '#*' -delete
	python3 setup.py clean
build:
	python3 setup.py clean
	python3 setup.py build
install:
	make clean
	make build
	python3 setup.py install
test:
	python3 -m pytest -v -s web3py/tests/
deploy:
	rm dist/*
	make clean
	#http://guide.python-distribute.org/creation.html
	python3 setup.py sdist
	twine upload dist/*
