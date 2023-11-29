.PHONY: dev prod up-dev up-prod down-dev down-prod


dev:
	docker-compose --env-file ./envs/docker-compose.env build mongodb dev nginx-dev

prod:
	docker-compose --env-file ./envs/docker-compose.env build mongodb prod nginx-prod

up-dev:
	docker-compose --env-file ./envs/docker-compose.env up mongodb dev nginx-dev

up-prod:
	docker-compose --env-file ./envs/docker-compose.env up -d mongodb prod nginx-prod

down-dev:
	docker-compose --env-file ./envs/docker-compose.env down mongodb dev nginx-dev

down-prod:
	docker-compose --env-file ./envs/docker-compose.env down mongodb prod nginx-prod
