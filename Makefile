.PHONY: help init up down build pull prune ps clean lint lint-src lint-tests
.ONESHELL:
SHELL = /bin/bash

PROJECT := distributed_audit_hub
.DEFAULT_GOAL := help

help: ## Print help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_.-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# ---- Core commands ----

init: down build up ## Initialize only this project (no global prune)

up: build ## Run all services (build first if needed)
	docker compose up -d
	make ps

build: ## Build Docker services
	docker compose build

pull: ## Pull images (only if needed from remote)
	docker compose pull

down: ## Stop only this project's services
	docker compose down --remove-orphans

ps: ## Show this project's running services
	docker compose ps

prune: ## Remove only this project's containers, images, and volumes
	docker compose down -v --remove-orphans --rmi local

clean: ## Remove Python cache files
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete
	find . -name '__pycache__' -delete

# ---- Linting ----

lint: lint-src lint-tests ## Run all linters

lint-src: ## Lint and format source code
	black src/ && isort src/ --profile black && flake8 src/

lint-tests: ## Lint and format test code
	black tests/ && isort tests/ --profile black
