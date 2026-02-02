#!/bin/sh
set -e

dockerd-entrypoint.sh &

# optionally wait for docker:
# until docker info >/dev/null 2>&1; do sleep 1; done

# for some unknown reason, the docker in container requires this env var
export DOCKER_HOST=""

exec jupyter lab --ip 0.0.0.0 --allow-root
