import typeguard

from unittest import TestCase
from unittest.mock import patch

from src.runners.abs import DatabaseResponse, DatabaseInDockerRunner


class TestDataResponse(TestCase):
    """src.runners.abs.DatabaseResponse"""
    def test_type_mistake(self):
        """If a particular `type` is passed with content that doesn't match."""
        with self.assertRaises(typeguard.TypeCheckError):
            DatabaseResponse(type="table", content="This is wrong")


class TestDockerRunner(TestCase):

    class TestRunner(DatabaseInDockerRunner):
        _default_container_name = "test_container"
        _image = "alpine:latest"
        _port = 1234

        def execute(self, query):
            pass

        def start(self):
            pass

    @patch.object(target=TestRunner, attribute="_port", new=1234)
    @patch.object(target=TestRunner, attribute="_proc_params")
    @patch.object(target=TestRunner, attribute="_get_container")
    def test_init_pipe(self, get_container, proc_params):
        '''
        Check if init calls everything in the right order.
        '''
        input = {"param1": "value1", "param2": "value2"}
        proc_params.return_value = {
            "param3": "value3",
            "param4": "value4",
            "ports": {self.TestRunner._port: 1234}
        }
        get_container.return_value = "container"
        my_runner = self.TestRunner(**input)
        proc_params.assert_called_once_with(**input)
        get_container.assert_called_once_with(**proc_params.return_value)

        self.assertEqual(my_runner._connection_port, 1234)
        self.assertEqual(my_runner.container, "container")

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
            ports=10
        )
        self.assertEqual(ans["image"], self.TestRunner._image)
        self.assertEqual(ans["name"], "some_name")
        self.assertEqual(ans["detach"], True)
        self.assertEqual(ans["remove"], True)
        self.assertEqual(ans["ports"], {self.TestRunner._port: free_port_out})

    @patch.object(
        target=TestRunner,
        attribute="_other_params",
        create=True,
        new={"param1": "value1", "remove": False}
    )
    def test_other_params(self):
        '''
        Test if other parameters passed correctly. Parameters that doesn't
        have special meaning must ignore values specified in the
        `other_params`.
        '''
        res = self.TestRunner._proc_params()
        self.assertEqual(res["param1"], "value1")
        # remove key any way takes `True` - other_params doesn't influence
        self.assertEqual(res["remove"], True)
