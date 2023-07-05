FROM continuumio/miniconda3:latest AS base
ARG TZ=Asia/Hong_Kong
ENV TZ=${TZ}

# Basic environment setup
RUN apt-get update && apt-get install -y tzdata python3 python3-pip -y

# Jupyter server (lab/notebook) setup
RUN pip3 install jupyterthemes notebook jupyter-c-kernel jupyterlab
RUN install_c_kernel
RUN conda install xeus-cling -c conda-forge

# Install packages for common utils
RUN pip3 install pyyaml seaborn numpy pandas scipy matplotlib

# Create same user in host machine
ARG USERNAME
ARG USER_ID
ARG GROUP_ID

RUN groupadd --gid ${GROUP_ID} ${USERNAME} && \
    adduser --disabled-password --gecos '' --uid ${USER_ID} --gid ${GROUP_ID} ${USERNAME}

# Enable dark mode
USER ${USERNAME}
RUN jt -t monokai
RUN mkdir -p /home/${USERNAME}/.jupyter/lab/user-settings/@jupyterlab/apputils-extension && \
    echo '{ "theme":"JupyterLab Dark" }' > /home/${USERNAME}/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings