# TraefikLab

This repository provides a Docker environment for running Jupyter Lab/Notebook with the Traefik reverse proxy. It supports multiple languages including Python, C, and C++ and can easily combined with extra services.

---

## Prerequisites

- Docker: [https://www.docker.com/](https://www.docker.com/)

- Docker-compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

- GNU make: [https://www.gnu.org/software/make/manual/make.html](https://www.gnu.org/software/make/manual/make.html)

---

## Usage

The Makefile commands are listed in the following:

```bash
# Build docker images
make build

# Create docker network
make network

# Start containers (default: Jupyer Lab)
make start
# Start containers (Jupyer Notebook)
JUPYTER_MODE=notebook make start
```

---

## After deployment

You can go to [localhost:1001](http://localhost:1001) for the traefik dashboard and [localhost:1002](https://localhost:1002) for the Jupyter Lab/Notebook.

---

## Authors
[@wyhwong](https://github.com/wyhwong)
