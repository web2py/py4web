.PHONY: clean build install test
clean:
	python3 setup.py clean
build:
	python3 setup.py clean
	python3 setup.py build
install:
	make clean
	make build
	python3 setup.py install
test:
	make install
	python3 -m unittest tests
deploy:
	rm dist/*
	make clean
	#http://guide.python-distribute.org/creation.html
	python3 setup.py sdist
	twine upload dist/*
