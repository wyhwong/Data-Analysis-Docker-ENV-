FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3 python3-pip -y
RUN pip3 install jupyterthemes notebook
RUN jt -t monokai
