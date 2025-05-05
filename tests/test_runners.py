from unittest import TestCase

from src.runners.runners import (
    PostgresRunner,
    ClickHouseRunner,
    SQLiteRunner
)
from src.runners.abs import DatabaseRunner


class RunnerBaseCase:
    """
    This is a base class for testing runners. It realies creating and
    stopping runners. And simple query test with just "SELECT 1;" query.

    Implement
    ---------
    runner_class
        Is an ancestor of the DatabaseRunner that will be tested in this class.

    Attributes
    ----------
    runner: DatabaseRunner
        Instance of the runner.
    """
    @classmethod
    def setUpClass(cls):
        if not hasattr(cls, "runner_class"):
            raise NotImplementedError(
                "runner_class expect to be implemented."
            )
        cls.runner: DatabaseRunner = cls.runner_class()
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.runner.stop()
        return super().tearDownClass()

    def test_simple_query(self):
        query = "SELECT 1 AS value, 2 AS value2;"
        exp_cols = ("value", "value2")
        exp_data = ((1, 2),)

        # Looking for a first response that have "table" type
        for response in self.runner.execute(query):
            if response.type == "table":
                break
        ans_cols, ans_data = response.content

        fail_msg = f"Failed for {self.__class__.__name__}"
        self.assertEqual(ans_cols, exp_cols, msg=fail_msg)
        self.assertEqual(ans_data, exp_data, msg=fail_msg)


class TestPostgres(RunnerBaseCase, TestCase):
    """
    Test the execute output of the database runners.
    """
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

        ans = self.runner.execute(query)
        self.assertEqual(ans[0].content, "CREATE TABLE")
        self.assertEqual(ans[1].content, "DROP TABLE")

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

        ans = self.runner.execute(
            "DROP TABLE IF EXISTS log_message;"
        )

        self.assertEqual(
            ans[0].content,
            'NOTICE: table "log_message" does not exist, skipping'
        )


class TestClickhouse(RunnerBaseCase, TestCase):
    runner_class = ClickHouseRunner


class TestSQLite(RunnerBaseCase, TestCase):
    runner_class = SQLiteRunner
