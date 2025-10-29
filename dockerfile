FROM python:3.12.8-slim

COPY ./src /src
COPY ./pyproject.toml /pyproject.toml

RUN pip install bash_kernel && \
    python3 -m bash_kernel.install && \
    apt update && apt install -y jq && \
    pip install --no-cache-dir --upgrade -e .