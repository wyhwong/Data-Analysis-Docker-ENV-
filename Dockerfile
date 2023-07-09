FROM continuumio/miniconda3:23.3.1-0 AS base
ARG TZ=Asia/Hong_Kong
ENV TZ=${TZ}

# Basic environment setup
RUN apt-get update && apt-get install tzdata python3 python3-pip -y

# Jupyter lab setup
RUN pip3 install jupyterthemes notebook jupyterlab

# Jupyter kernal (R)
RUN conda config --set auto_update_conda False
RUN conda install r-irkernel -c r --no-update-deps --freeze-installed -y

# Jupyter kernal (C/C++)
RUN pip3 install jupyter-c-kernel && \
    install_c_kernel --sys-prefix
RUN conda install xeus-cling -c conda-forge -y

# Jupyter kernal (Java)
RUN apt-get install unzip default-jdk -y
RUN wget https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip && \
    unzip ijava-1.3.0.zip && \
    python3 install.py --sys-prefix

# Jupyter kernal (Javascript)
RUN curl -s https://deb.nodesource.com/setup_20.x | bash && \
    apt-get install nodejs -y
RUN npm install -g npm@9.8.0 && \
    npm install -g --unsafe-perm ijavascript && \
    ijsinstall --install=global

# Jupyter kernal (Golang)
RUN rm -rf /usr/local/go && \
    wget https://go.dev/dl/go1.20.5.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.20.5.linux-amd64.tar.gz
ENV PATH=$PATH:/usr/local/go/bin
RUN go install github.com/gopherdata/gophernotes@v0.7.5 && \
    mkdir -p /usr/local/share/jupyter/kernels/gophernotes && \
    cd /usr/local/share/jupyter/kernels/gophernotes && \
    cp "$(go env GOPATH)"/pkg/mod/github.com/gopherdata/gophernotes@v0.7.5/kernel/*  "." && \
    chmod +w ./kernel.json # in case copied kernel.json has no write permission && \
    sed "s|gophernotes|$(go env GOPATH)/bin/gophernotes|" < kernel.json.in > kernel.json

# Jupyter kernal (Ruby)
RUN apt-get install ruby-full -y
RUN apt-get install libzmq3-dev -y && \
    gem install iruby && \
    iruby register --force && \
    mv /root/.local/share/jupyter/kernels/ruby /usr/local/share/jupyter/kernels/ruby

# # Jupyter kernal (Julia)
RUN wget https://julialang-s3.julialang.org/bin/linux/x64/1.9/julia-1.9.2-linux-x86_64.tar.gz && \
    tar -C /usr/local -zxf julia-1.9.2-linux-x86_64.tar.gz
ENV PATH=$PATH:/usr/local/julia-1.9.2/bin
RUN julia -e 'using Pkg; Pkg.add("IJulia")' && \
    mv /root/.local/share/jupyter/kernels/julia-1.9 /usr/local/share/jupyter/kernels/julia-1.9

# Create same user in host machine
ARG USERNAME
ARG USER_ID
ARG GROUP_ID
RUN groupadd --gid ${GROUP_ID} ${USERNAME} && \
    adduser --disabled-password --gecos '' --uid ${USER_ID} --gid ${GROUP_ID} ${USERNAME}

USER ${USERNAME}
WORKDIR /home/${USERNAME}/jupyter

# Enable dark mode
RUN jt -t monokai && \
    mkdir -p /home/${USERNAME}/.jupyter/lab/user-settings/@jupyterlab/apputils-extension && \
    echo '{ "theme":"JupyterLab Dark" }' > /home/${USERNAME}/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings
