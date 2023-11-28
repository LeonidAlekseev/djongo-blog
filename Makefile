.PHONY: dev prod up-dev up-prod


dev:
	docker-compose --env-file ./envs/docker-compose.env build mongodb dev dev-nginx

prod:
	docker-compose --env-file ./envs/docker-compose.env build mongodb prod prod-nginx

up-dev:
	docker-compose --env-file ./envs/docker-compose.env up mongodb dev dev-nginx

up-prod:
	docker-compose --env-file ./envs/docker-compose.env up -d mongodb prod prod-nginx
