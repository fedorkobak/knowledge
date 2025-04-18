from unittest import TestCase
from unittest.mock import patch

from src.runners import DatabaseInDockerRunner


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
