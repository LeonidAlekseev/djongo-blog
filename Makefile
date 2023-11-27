.PHONY: build dev up-dev prod up-prod


build: dev prod

dev:
	docker-compose build dev

up-dev:
	docker-compose up dev

prod:
	docker-compose build prod

up-prod:
	docker-compose up -d prod
