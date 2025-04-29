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
    def test_simple_query(self):
        runners = [
            PostgresRunner,
            ClickHouseRunner,
            SQLiteRunner
        ]
        query = "SELECT 1 AS value, 2 AS value2;"
        exp_cols = ("value", "value2")
        exp_data = ((1, 2),)

        for runner_class in runners:
            r = runner_class()
            ans_cols, ans_data = r.execute(query)
            fail_msg = f"Failed for {r.__class__.__name__}"
            self.assertEqual(ans_cols, exp_cols, msg=fail_msg)
            self.assertEqual(ans_data, exp_data, msg=fail_msg)
            r.stop()
