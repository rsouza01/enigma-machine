.DEFAULT_GOAL := help

help:
	@echo 'Available commands:'

run-tests:
	python setup.py pytest