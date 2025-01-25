FROM python:3.12.8-slim

# Surprisingly for Python examples, a bash kernel is required. The following 
# code installs and configures it.
RUN pip install bash_kernel && \
    python3 -m bash_kernel.install && \
    apt update && apt install -y jq && \
    jq '.argv[0] = "/usr/local/bin/python3.12"' /usr/local/share/jupyter/kernels/bash/kernel.json > /tmp/kernel.json && \
    mv /tmp/kernel.json /usr/local/share/jupyter/kernels/bash/kernel.json