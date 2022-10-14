# Data-Analysis-Template

## Description of Repo
This template standardized the basic docker environment of customized data analysis environment with Python. The makefile commands are listed in the following:

---

## Data Analysis with Python
```bash
# To build image for containers
make build

# To start main
make start
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