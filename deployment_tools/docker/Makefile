# https://codeblog.dotsandbrackets.com/quick-intro-to-docker-compose/


DOCKER_COMPOSE=docker-compose
#DOCKER_COMPOSE=docker compose
# On latest docker version, use 'docker compose'

up: ## Start all containers in foreground
	@$(DOCKER_COMPOSE) up -d

down: ## Stop all containers
	@$(DOCKER_COMPOSE) down

restart: ## Restart all containers in foreground
	@$(DOCKER_COMPOSE) restart -d

rebuild: ## Force rebuild of all containers
	@$(DOCKER_COMPOSE) up --build --force-recreate postgres web

ssh: ## Interactive run
	@$(DOCKER_COMPOSE) exec web bash
