.DEFAULT_GOAL := help

help:
	@echo 'Available commands:'

run-app:
	python -m enigma -v
	@echo "--------------------------------"
	python -m enigma --help --suppress-banner
	@echo "--------------------------------"
	python -m enigma --suppress-banner encrypt -p "enigma"
	@echo "--------------------------------"
	python -m enigma --suppress-banner decrypt -p "enigma"

run-tests:
	python -m pytest tests/