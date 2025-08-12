'''
Implementation of database runners.
'''
import sqlite3
import psycopg
import typeguard
from time import sleep
import clickhouse_connect
from .abs import (
    table_output,
    DatabaseInDockerRunner,
    SeparateQueryRunner
)


class PostgresRunner(DatabaseInDockerRunner):
    _default_container_name = "postgres_db"
    _image = "postgres"
    _port = 5432
    _other_params = {
        "environment": {"POSTGRES_PASSWORD": "example"}
    }

    def __init__(self):
        super().__init__()
        self._logs = []

    def _logs_saver(self, diag):
        """
        Handler for the cursor that saves logs line by line in `self._logs`.
        """
        self._logs.append(f"{diag.severity}: {diag.message_primary}")

    def start(self):
        sleep(5)
        self.connection = psycopg.connect(
            dbname="postgres",
            user="postgres",
            password="example",
            host="localhost",
            port=self._connection_port
        )
        self.connection.add_notice_handler(self._logs_saver)

    def _read_result_set(
        self,
        cursor: psycopg.Cursor
    ) -> tuple[list[str], list[table_output]]:
        """
        Read messages from the current result set of the specified cursor.
        """
        messages = [log for log in self._logs]
        self._logs.clear()

        if not (cursor.statusmessage is None):
            messages.append(cursor.statusmessage)

        tables = list[table_output]()
        if not (cursor.description is None):
            columns = [desc.name for desc in cursor.description]
            data = cursor.fetchall()
            tables.append((tuple(columns), tuple(data)))

        return messages, tables

    @typeguard.typechecked
    def execute(self, code: str) -> tuple[list[str], list[table_output]]:
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(code.encode())
            except psycopg.errors.Error as e:
                self.connection.rollback()
                raise e

            messages, tables = self._read_result_set(cursor=cursor)
            while cursor.nextset():
                m, t = self._read_result_set(cursor=cursor)
                messages.extend(m)
                tables.extend(t)
            return messages, tables

    def stop(self):
        if hasattr(self, "connection"):
            self.connection.close()
        super().stop()


class ClickHouseRunner(DatabaseInDockerRunner, SeparateQueryRunner):
    _default_container_name = "clickhouse_db"
    _image = "clickhouse/clickhouse-server"
    _port = 8123
    _password = "example"
    _other_params = {
        "environment": {"CLICKHOUSE_PASSWORD": _password}
    }

    def start(self):
        sleep(5)
        self.connection = clickhouse_connect.get_client(
            host="localhost",
            port=self._connection_port,
            password=self._password
        )

    @typeguard.typechecked
    def _execute_one(
        self, command: str
    ) -> tuple[list[str], list[table_output]]:
        result = self.connection.query(command)
        data = [tuple(row) for row in result.result_rows]
        result = (result.column_names, tuple(data))
        return [], [result]

    def stop(self):
        if hasattr(self, "connection"):
            self.connection.close()
        super().stop()


class SQLiteRunner(SeparateQueryRunner):
    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        self.connection = None
        super().__init__()

    def start(self):
        self.connection = sqlite3.connect(self.db_path)

    @typeguard.typechecked
    def _execute_one(
        self, command: str
    ) -> tuple[list[str], list[table_output]]:
        if self.connection is None:
            raise RuntimeError("Database connection is not established.")
        cursor = self.connection.cursor()
        cursor.execute(command)

        data = cursor.fetchall()
        columns = (
            [d[0] for d in cursor.description]
            if cursor.description
            else []
        )
        result = (tuple(columns), tuple(data))

        cursor.close()
        return [], [result]

    def stop(self):
        if self.connection:
            self.connection.close()
