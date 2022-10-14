# Data-Analysis-Template

This template standardized the basic docker environment of customized data analysis environment. The makefile commands are listed in the following:
```bash
# To build image for containers
make build

# To start main
make start

# To run Jupyter notebook server after main
make jupyter_up
# To specify a port for the notebook
make port=<port> jupyter_up

# To stop Jupyter notebook server
make jupyter_down

# To stop and remove all containers
make clean
```
