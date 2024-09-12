default:
	pylint src/**/*.py tests/**/*.py

test:
	pytest -v

run:
	python src/main.py
