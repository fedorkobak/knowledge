#!/bin/sh
clickhouse-server &

jupyter lab --ip 0.0.0.0 --allow-root "$@"

ENTRYPOINT ["/usr/local/bin/start.sh"]
