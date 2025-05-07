'''
Implementation of database runners.
'''
import sqlite3
import psycopg
import typeguard
from time import sleep
import clickhouse_connect
from .abs import (
    DatabaseRunner,
    DatabaseInDockerRunner,
    execute_output,
    DatabaseResponse
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
    ) -> list[DatabaseResponse]:
        """
        Read messages from the current result set of the specified cursor.
        """
        ans = [
            DatabaseResponse(type="text", content=log)
            for log in self._logs
        ]
        self._logs.clear()

        if not (cursor.statusmessage is None):
            ans.append(
                DatabaseResponse(type='text', content=cursor.statusmessage)
            )

        if not (cursor.description is None):
            columns = [desc.name for desc in cursor.description]
            data = cursor.fetchall()
            ans.append(
                DatabaseResponse(
                    type="table",
                    content=(tuple(columns), tuple(data))
                )
            )

        return ans

    @typeguard.typechecked
    def execute(self, code: str) -> execute_output:
        with self.connection.cursor() as cursor:
            cursor.execute(code)

            res = self._read_result_set(cursor=cursor)
            while cursor.nextset():
                res += self._read_result_set(cursor=cursor)
            return res

    def stop(self):
        if hasattr(self, "connection"):
            self.connection.close()
        super().stop()


class ClickHouseRunner(DatabaseInDockerRunner):
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
    def execute(self, code: str) -> execute_output:
        result = self.connection.query(code)
        result = (result.column_names, tuple(result.result_rows))
        return [DatabaseResponse(type="table", content=result)]

    def stop(self):
        if hasattr(self, "connection"):
            self.connection.close()
        super().stop()


class SQLiteRunner(DatabaseRunner):
    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        self.connection = None
        super().__init__()

    def start(self):
        self.connection = sqlite3.connect(self.db_path)

    @typeguard.typechecked
    def execute(self, query: str) -> execute_output:
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        self.connection.commit()
        columns = [d[0] for d in cursor.description]
        result = DatabaseResponse(
            type="table", content=(tuple(columns), tuple(data))
        )
        return [result]

    def stop(self):
        if self.connection:
            self.connection.close()
