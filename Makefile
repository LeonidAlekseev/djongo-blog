.PHONY: build dev up-dev prod up-prod


build: dev prod

dev:
	docker-compose build dev

up-dev:
	docker-compose up dev

prod:
	docker-compose build prod

up-prod:
	docker run --log-driver json-file --log-opt max-size=32m --log-opt max-file=1 --restart=always -it -d -p 80:80 djongo-blog/project:latest-prod
