from typing import Type
from unittest import TestCase

from src.runners.runners import (
    PostgresRunner,
    ClickHouseRunner,
    SQLiteRunner
)
from src.runners.abs import DatabaseRunner


class BaseClasses:
    """
    Base classes are not supposed to be executed.
    https://stackoverflow.com/questions/1323455/python-unit-test-with-base-and-sub-class
    """
    class RunnerBaseCase(TestCase):
        """
        This is a base class for testing runners. It realies creating and
        stopping runners. And simple query test with just "SELECT 1;" query.

        Implement
        ---------
        runner_class
            Is an ancestor of the DatabaseRunner that will be tested in this
            class.

        Attributes
        ----------
        runner: DatabaseRunner
            Instance of the runner.
        """
        runner_class: Type
        runner: DatabaseRunner

        @classmethod
        def setUpClass(cls):
            if not hasattr(cls, "runner_class"):
                raise NotImplementedError(
                    "runner_class expect to be implemented."
                )
            cls.runner = cls.runner_class()
            return super().setUpClass()

        @classmethod
        def tearDownClass(cls):
            cls.runner.stop()
            return super().tearDownClass()

        def test_simple_query(self):
            query = "SELECT 1 AS value, 2 AS value2;"
            exp_cols = ("value", "value2")
            exp_data = ((1, 2),)

            messages, tables = self.runner.execute(query)
            # Looking for a first response that have "table" type
            ans_cols, ans_data = tables[0]

            fail_msg = f"Failed for {self.__class__.__name__}"
            self.assertEqual(ans_cols, exp_cols, msg=fail_msg)
            self.assertEqual(ans_data, exp_data, msg=fail_msg)

        def test_create_insert_command(self):
            """
            If runners ok with CREATE/INSERT commands.
            """
            code = """
            CREATE TABLE create_table_test (col INT);
            INSERT INTO create_table_test (col) VALUES (45), (87);
            """
            self.runner.execute(code)


class TestPostgres(BaseClasses.RunnerBaseCase, TestCase):
    """
    Test the execute output of the database runners.
    """
    runner: PostgresRunner
    runner_class = PostgresRunner

    def test_system_messages_pg(self):
        """
        For some command postgres sends system messages. They have to be
        correct processed by PostgresRunner.
        """

        query = """
        CREATE TABLE test_system_messages (val INT);
        DROP TABLE test_system_messages;
        """

        messages, tables = self.runner.execute(query)
        self.assertEqual(messages, ["CREATE TABLE", "DROP TABLE"])
        self.assertEqual(tables, [])

    def test_logs_savers(self):
        """
        Each call to `connection.execute` should add log messages to the
        `_logs` attribute.
        """
        self.runner.connection.execute(
            "DROP TABLE IF EXISTS log_message;"
        )
        self.assertEqual(
            self.runner._logs[-1],
            'NOTICE: table "log_message" does not exist, skipping'
        )
        self.runner._logs.clear()

    def test_log_messages_pg(self):
        """
        In some cases, pg will throw special messages - log messages.
        They must be the first in the list of DatabaseResponses.
        """

        messages, tables = self.runner.execute(
            "DROP TABLE IF EXISTS log_message;"
        )

        self.assertEqual(
            messages[0],
            'NOTICE: table "log_message" does not exist, skipping'
        )


class TestClickhouse(BaseClasses.RunnerBaseCase, TestCase):
    runner_class = ClickHouseRunner

    def test_create_insert_command(self):
        '''
        Redefine this method for clickhouse as it has different syntax for
        CREATE operation.
        '''
        code = """
        CREATE TABLE test_table (col Int) ENGINE=MergeTree ORDER BY col;
        INSERT INTO test_table (col) VALUES (10), (20);
        """
        self.runner.execute(code=code)


class TestSQLite(BaseClasses.RunnerBaseCase, TestCase):
    runner_class = SQLiteRunner
