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

    def test_postgres(self):
        """
        Test the execute output of the Postgres runner.
        """
        postgres_runner = PostgresRunner()

        query = "SELECT 1 AS value, 2 AS value2;"
        ans_cols, ans_data = postgres_runner.execute(query)
        exp_cols = ["value", "value2"]
        exp_data = [(1, 2)]
        self.assertEqual(ans_cols, exp_cols)
        self.assertEqual(ans_data, exp_data)

        postgres_runner.stop()

    def test_clickhouse(self):
        """
        Test the execute output of the ClickHouse runner.
        """
        clickhouse_runner = ClickHouseRunner()

        query = "SELECT 1 AS value, 2 AS value2;"
        ans_cols, ans_data = clickhouse_runner.execute(query)
        exp_cols = ("value", "value2")
        exp_data = [(1, 2)]
        self.assertEqual(ans_cols, exp_cols)
        self.assertEqual(ans_data, exp_data)

        clickhouse_runner.stop()

    def test_sqlite(self):
        """
        Test the execute output of the SQLite runner.
        """
        sqlite_runner = SQLiteRunner()

        query = "SELECT 1 AS value, 2 AS value2;"
        ans_cols, ans_data = sqlite_runner.execute(query)
        exp_cols = ["value", "value2"]
        exp_data = [(1, 2)]
        self.assertEqual(ans_cols, exp_cols)
        self.assertEqual(ans_data, exp_data)

        sqlite_runner.stop()
