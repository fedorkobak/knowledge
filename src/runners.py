import socket
import docker
import sqlite3
import psycopg2
import clickhouse_connect
from abc import ABC, abstractmethod
from time import sleep


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        return s.getsockname()[1]


class DatabaseRunner(ABC):
    def __init__(self):
        self.start()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def execute(self, query: str):
        pass

    @abstractmethod
    def stop(self):
        pass

    def __del__(self):
        self.stop()


class DatabaseInDockerRunner(DatabaseRunner):
    def __init__(self, container_name: str | None = None):
        self.client = docker.from_env()
        self.container_name = (
            self._get_container_name()
            if container_name is None
            else container_name
        )
        self.port = find_free_port()
        super().__init__()

    def _get_container_name(self) -> None:
        suffix = 1
        self._default_container_name
        containres_names = [
            container.name for container in self.client.containers.list()
        ]
        while True:
            container_name = self._default_container_name + "_" + str(suffix)
            if container_name in containres_names:
                suffix += 1
            else:
                return container_name

    @property
    @abstractmethod
    def _default_container_name(self) -> str:
        pass


class PostgresRunner(DatabaseInDockerRunner):
    def __init__(self, container_name="postgres_db"):
        super().__init__()

    @property
    def _default_container_name(self) -> str:
        return "postgres_db"

    def start(self):
        self.container = self.client.containers.run(
            "postgres",
            name=self.container_name,
            environment={"POSTGRES_PASSWORD": "example"},
            ports={"5432/tcp": self.port},
            detach=True,
            remove=True,
        )
        sleep(5)
        self.connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="example",
            host="localhost",
            port=self.port
        )

    def execute(self, query: str):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            try:
                return cursor.fetchall()
            except psycopg2.ProgrammingError:
                return None

    def stop(self):
        if hasattr(self, "connection"):
            self.connection.close()
        if hasattr(self, "container"):
            self.container.stop()


class ClickHouseRunner(DatabaseInDockerRunner):
    def __init__(self, container_name="clickhouse_db"):
        super().__init__()

    @property
    def _default_container_name(self) -> str:
        return "clickhouse_db"

    def start(self):
        self.container = self.client.containers.run(
            "clickhouse/clickhouse-server",
            environment={"CLICKHOUSE_PASSWORD": "example"},
            name=self.container_name,
            ports={"8123/tcp": self.port},
            detach=True,
            remove=True
        )
        sleep(5)
        self.connection = clickhouse_connect.get_client(
            host="localhost",
            port=self.port,
            password="example"
        )

    def execute(self, query: str):
        return self.connection.query(query).result_rows

    def stop(self):
        if hasattr(self, "connection"):
            self.connection.close()
        if hasattr(self, "container"):
            self.container.stop()


class SQLiteRunner(DatabaseRunner):
    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        self.connection = None
        super().__init__()

    def start(self):
        self.connection = sqlite3.connect(self.db_path)

    def execute(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        self.connection.commit()
        return results

    def stop(self):
        if self.connection:
            self.connection.close()
