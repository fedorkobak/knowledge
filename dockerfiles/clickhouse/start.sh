#!/bin/sh
service clickhouse-server start
jupyter lab --ip 0.0.0.0 --allow-root "$@"
