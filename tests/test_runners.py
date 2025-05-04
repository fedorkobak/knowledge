from unittest import TestCase

from src.runners.runners import (
    PostgresRunner,
    ClickHouseRunner,
    SQLiteRunner
)


class TestExecuteOutput(TestCase):
    """
    Test the execute output of the database runners.
    """
    @classmethod
    def setUpClass(cls):
        cls.postgres_runner = PostgresRunner()
        cls.runners = [
            cls.postgres_runner,
            ClickHouseRunner(),
            SQLiteRunner()
        ]

    @classmethod
    def tearDownClass(cls):
        for runner in cls.runners:
            runner.stop()

    def test_simple_query(self):
        query = "SELECT 1 AS value, 2 AS value2;"
        exp_cols = ("value", "value2")
        exp_data = ((1, 2),)

        for r in self.runners:
            ans_cols, ans_data = r.execute(query)[0].content
            fail_msg = f"Failed for {r.__class__.__name__}"
            self.assertEqual(ans_cols, exp_cols, msg=fail_msg)
            self.assertEqual(ans_data, exp_data, msg=fail_msg)

    def test_system_messages_pg(self):
        """
        For some command postgres sends system messages. They have to be
        correct processed by PostgresRunner.
        """

        query = """
        CREATE TABLE test_system_messages; DROP TABLE test_system_messages;
        """

        ans = self.postgres_runner.execute(query)
        self.assertEqual(ans[0].content, "CREATE TABLE")
        self.assertEqual(ans[1].content, "DROP TABLE")

    def test_log_messages_pg(self):
        """
        In some cases, pg will throw special messages - log messages.
        They must be the first in the list of DatabaseResponses.
        """

        ans = self.postgres_runner.execute(
            "DROP TABLE IF EXISTS log_message;"
        )

        self.assertEqual(
            ans[0].content,
            'NOTICE: table "log_message" does not exist, skipping'
        )
