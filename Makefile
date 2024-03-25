venv:
	python -m venv venv

install:
	pip install --upgrade pip;
	pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C *.py

docker:
	docker build -t bugarin10/embedder:latest .
