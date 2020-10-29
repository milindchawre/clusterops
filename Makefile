.PHONY: default install lint lint-check test

default: test

install:
	pipenv install --dev flake8 black pytest boto3

lint:
	black .
	flake8

lint-check:
	flake8
	black --check --diff .

test:
	PYTHONPATH=./src pytest
