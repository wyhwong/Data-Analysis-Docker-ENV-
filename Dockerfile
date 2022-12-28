FROM ubuntu:20.04
ENV TZ=Asia/Hong_Kong
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y tzdata python3 python3-pip -y
RUN pip3 install seaborn numpy pandas matplotlib jupyterthemes notebook
RUN jt -t monokai
