from unittest import TestCase

from runners.runners import (
    PostgresRunner,
    ClickHouseRunner,
    SQLiteRunner
)


# To avoid creating each time a new database each time runners created globally
postgres_runner = PostgresRunner()
clikchouse_runner = ClickHouseRunner()
sqlite_runner = SQLiteRunner()


class TestExecuteOutput(TestCase):
    """
    Test the execute output of the database runners.
    """
    def test_postgres(self):
        """
        Test the execute output of the Postgres runner.
        """
        query = "SELECT 1 AS value, 2 AS value2;"
        ans_cols, ans_data = postgres_runner.execute(query)
        exp_cols = ["value", "value2"]
        exp_data = [(1, 2)]
        self.assertEqual(ans_cols, exp_cols)
        self.assertEqual(ans_data, exp_data)
