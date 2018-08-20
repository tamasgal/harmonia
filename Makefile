PKGNAME=harmonia

default: build

all: install

install: 
	pip install .

install-dev:
	pip install -e .

test: 
	py.test --junitxml=./reports/junit.xml -o junit_suite_name=$(PKGNAME) $(PKGNAME)

test-cov:
	py.test --cov ./ --cov-report term-missing --cov-report xml:reports/coverage.xml --cov-report html:reports/coverage $(PKGNAME) 

test-loop: 
	py.test
	ptw --ext=.py,.pyx --ignore=doc

flake8: 
	py.test --flake8
	py.test --flake8 km3modules

pep8: flake8

docstyle: 
	py.test --docstyle
	py.test --docstyle km3modules

lint: 
	py.test --pylint

dependencies:
	pip install -Ur requirements.txt

.PHONY: yapf
yapf:
	yapf -i -r $(PKGNAME)
	yapf -i setup.py

.PHONY: all install install-dev test test-cov test-loop flake8 pep8 lint dependencies docstyle yapf
