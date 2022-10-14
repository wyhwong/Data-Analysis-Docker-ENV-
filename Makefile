export DOCKER_BUILDKIT=1

port ?= 8888

build:
	port=${port} docker-compose build

start:
	port=${port} docker-compose up data_analysis

jupyter_up:
	port=${port} docker-compose up -d data_analysis_jupyter

jupyter_down:
	port=${port} docker-compose kill data_analysis_jupyter

clean:
	port=${port} docker-compose down --remove-orphans