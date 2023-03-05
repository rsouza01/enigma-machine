.DEFAULT_GOAL := help

help:
	@echo 'Available commands:'

run-app:
	python -m enigma -v
	@echo "--------------------------------"
	python -m enigma --help
	@echo "--------------------------------"
	python -m enigma encrypt -p "enigma"
	@echo "--------------------------------"
	python -m enigma decrypt -p "enigma"

run-tests:
	python -m pytest tests/