from unittest import TestCase
from unittest.mock import patch

from src.runners.abs import DatabaseInDockerRunner


class TestDockerRunner(TestCase):

    class TestRunner(DatabaseInDockerRunner):
        _default_container_name = "test_container"
        _image = "alpine:latest"

        def execute(self, query):
            pass

    @patch.object(target=TestRunner, attribute="_proc_params")
    @patch.object(target=TestRunner, attribute="_get_container")
    def test_init_pipe(self, get_container, proc_params):
        '''
        Check if init calls everything in the right order.
        '''
        input = {"param1": "value1", "param2": "value2"}
        proc_params.return_value = {"param3": "value3", "param4": "value4"}
        self.TestRunner(**input)
        proc_params.assert_called_once_with(**input)
        get_container.assert_called_once_with(**proc_params.return_value)

    @patch.object(target=TestRunner, attribute="_get_containers_names")
    def test_name(self, get_containers_names):
        '''
        Test that name of the container is created correctly.
        '''
        get_containers_names.return_value = [
            self.TestRunner._default_container_name + "_1",
            self.TestRunner._default_container_name + "_2",
        ]
        res = self.TestRunner._get_container_name()
        exp = "test_container_3"
        self.assertEqual(res, exp)

    @patch("src.runners.abs.find_free_port")
    def test_container_parameters(self, find_free_port):
        '''
        Test if container parameters processed
        '''

        free_port_out = 1234
        find_free_port.return_value = free_port_out

        ans = self.TestRunner._proc_params(
            image="some_image",
            name="some_name",
            detach=False,
            remove=False,
            port=10
        )
        self.assertEqual(ans["image"], self.TestRunner._image)
        self.assertEqual(ans["name"], "some_name")
        self.assertEqual(ans["detach"], True)
        self.assertEqual(ans["remove"], True)
        self.assertEqual(ans["ports"], free_port_out)
