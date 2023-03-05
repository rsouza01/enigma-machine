.DEFAULT_GOAL := help

help:
	@echo 'Available commands:'

run-app:
	python -m enigma -v
	python -m enigma --help

run-tests:
	python setup.py pytest