FROM python:3.12.8-slim

# Surprisingly for Python examples, a bash kernel is required. The following 
# code installs and configures it.
RUN pip install bash_kernel && \
    python3 -m bash_kernel.install && \
    apt update && apt install -y jq