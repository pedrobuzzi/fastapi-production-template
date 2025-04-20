.PHONY: run install test format lint clean

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest

lint:
	flake8 app

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete