.PHONY: help pull install build restart

help:
	@echo "Available commands:"
	@echo " help                  - Shows this message"
	@echo " .env                  - Creates .env variables file"
	@echo " install               - Install Python dependencies"
	@echo " pull                  - Pulls required docker images"
	@echo " build                 - Builds Celery worker container with Selenium"
	@echo " start                 - Start containers"
	@echo " restart               - Performs clean restart of worker container"

.env:
	cp sample.env .env

.venv:
	python3 -m venv .venv

install: .venv
	@. .venv/bin/activate \
	&& pip install -r requirements.txt

pull:
	docker-compose pull

build:
	docker-compose build

restart:
	docker-compose rm -sf worker
	docker-compose up -d worker
