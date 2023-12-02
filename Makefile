.PHONY: dev up-dev down-prod prod up-prod down-dev


dev:
	docker-compose --env-file ./envs/development.env build mongodb dev nginx-dev

up-dev:
	docker-compose --env-file ./envs/development.env up mongodb dev nginx-dev

down-dev:
	docker-compose --env-file ./envs/development.env down mongodb dev nginx-dev

prod:
	docker-compose --env-file ./envs/production.env build mongodb prod nginx-prod

up-prod:
	docker-compose --env-file ./envs/production.env up -d mongodb prod nginx-prod

down-prod:
	docker-compose --env-file ./envs/production.env down mongodb prod nginx-prod
