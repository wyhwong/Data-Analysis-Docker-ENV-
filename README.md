# Docker Environment for Data Analysis

This repository aims to provide a docker environment for data analysis with Python/C/C++.

---

## Description and Usage

This repository standardized a basic docker environment of customized data analysis needs with Python/C/C++. The makefile commands are listed in the following:

```bash
# To build image for containers
make build

# To start main
make start

# To develop
make develop
docker exec -it data_analysis bash
```

---

## Data Visualization with Jupyter Notebook Server
```bash
# To run Jupyter notebook server
make jupyter_up
# To specify a port for the notebook
make port=<port> jupyter_up

# To stop Jupyter notebook server
make jupyter_down

# To stop and remove all containers
make clean
```

---

## Authors
[@wyhwong](https://github.com/wyhwong)

---
