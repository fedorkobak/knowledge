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
        cls.runners = [
            PostgresRunner(),
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
            ans_cols, ans_data = r.execute(query)
            fail_msg = f"Failed for {r.__class__.__name__}"
            self.assertEqual(ans_cols, exp_cols, msg=fail_msg)
            self.assertEqual(ans_data, exp_data, msg=fail_msg)
