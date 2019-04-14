.PHONY: clean build install test
clean:
	python setup.py clean
build:
	python setup.py clean
	python setup.py build
install:
	make clean
	make build
	python setup.py install
test:
	make install
	python -m unittest tests
deploy:
	make clean
	#http://guide.python-distribute.org/creation.html
	python setup.py sdist
	twine upload dist/*
