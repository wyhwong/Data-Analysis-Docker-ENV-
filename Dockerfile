FROM continuumio/miniconda3:latest
ENV TZ=Asia/Hong_Kong
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y tzdata python3 python3-pip -y
RUN pip3 install seaborn numpy pandas matplotlib jupyterthemes notebook jupyter-c-kernel
RUN install_c_kernel
RUN conda install xeus-cling -c conda-forge
RUN jt -t monokai

COPY . /app
WORKDIR /app
