import unittest
from unittest import TestCase
from unittest.mock import patch

from src.runners.abs import (
    table_output,
    DatabaseInDockerRunner,
    SeparateQueryRunner
)


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


class TestSeparateQueryRunner(TestCase):

    class TestRunner(SeparateQueryRunner):
        def start(self):
            pass

        def _execute_one(
            self, code: str
        ) -> tuple[list[str], list[table_output]]:
            return (
                ["Message"],
                [(("Column1", "Column2"), (("Value1", "Value2"),))]
            )

        def stop(self):
            pass

    def test_separate_code(self):
        inp_out = [
            (
                """
                    SELECT 10; SELECT 20;
                    INSERT SOME HELLO;
                """,
                ["SELECT 10", "SELECT 20", "INSERT SOME HELLO"]
            ),
            ("SELECT 10", ["SELECT 10"]),
            ("SELECT 10;", ["SELECT 10"])
        ]
        for inp, out in inp_out:
            res = SeparateQueryRunner._separate_code(inp)
            self.assertEqual(out, res, msg=f"Wrong result for {inp}.")

    def test_execute(self):
        """
        If the `execute` method correctly prepares the code
        for execution and composes the output correctly.
        """
        code = "Here are some; code"
        commands = self.TestRunner._separate_code(code)
        returns = (
            ["Message", "Message2"],
            [
                (("Column1", "Column2"), (("Value1", "Value2"),)),
                (("Column1", "Column2"), ((1, 2), (3, 4)))
            ]
        )
        separate_patch = patch.object(
            target=SeparateQueryRunner,
            attribute="_separate_code",
            return_value=commands
        )
        execute_one_patch = patch.object(
            target=self.TestRunner,
            attribute="_execute_one",
            return_value=returns
        )

        with separate_patch as separate_code, execute_one_patch as execute_one:
            runner = self.TestRunner()
            result = runner.execute(code=code)
            separate_code.assert_called_once_with(code)

            self.assertEqual(
                result,
                (
                    returns[0] * len(commands),
                    returns[1] * len(commands)
                ),
                msg="The output doesn't correspond to expected."
            )
            for call, command in zip(execute_one.mock_calls, commands):
                self.assertEqual(call.kwargs, {"command": command})


if __name__ == "__main__":
    unittest.main()
