export DOCKER_BUILDKIT=1

port ?= 8888

build:
	docker-compose build

develop:
	docker-compose -f docker-compose.yml -f docker-compose-dev.yml up -d data_analysis

start:
	docker-compose up data_analysis

jupyter_up:
	port=${port} docker-compose up -d data_analysis_jupyter

jupyter_down:
	docker-compose kill data_analysis_jupyter

clean:
	docker-compose down --remove-orphans
