'''
Implementation of database runners.
'''
import sqlite3
import psycopg2
import typeguard
from time import sleep
import clickhouse_connect
from .abs import DatabaseRunner, DatabaseInDockerRunner, execute_output


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

    @typeguard.typechecked
    def execute(self, query: str) -> execute_output:
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            try:
                columns = [desc.name for desc in cursor.description]
                data = cursor.fetchall()
                return columns, data
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
