from unittest import TestCase
from unittest.mock import patch

from src.runners import (
    DatabaseInDockerRunner,
    PostgresRunner,
    ClickHouseRunner,
    SQLiteRunner
)


class TestDockerRunner(TestCase):

    default_container_name = "test_container"

    class TestRunner(DatabaseInDockerRunner):
        @property
        def _default_container_name(self) -> str:
            return TestDockerRunner.default_container_name

        def execute(self, query):
            pass

        def start(self):
            pass

        def stop(self):
            pass

    @patch.object(target=TestRunner, attribute="_get_containers_names")
    def test_name(self, get_containers_names):
        get_containers_names.return_value = [
            self.default_container_name + "_1",
            self.default_container_name + "_2",
        ]
        res = self.TestRunner()._get_container_name()
        exp = "test_container_3"
        self.assertEqual(res, exp)


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
