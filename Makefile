.PHONY: default
default: build;

clean:
	rm -rf ./dist

build: clean
	python setup.py sdist
	python setup.py bdist_wheel --universal

install:
	python setup.py install

upload: build
	twine upload ./dist/*
