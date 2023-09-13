install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	black .
lint:
	pylint --disable=R,C src/*.py
test:
	# unit test using pytest and pytest-coverage
build:
	docker build -t mac-bff .
deploy:
	docker run -d -p 0.0.0.0:5000:5000 mac-bff

all: install format lint test build deploy