from textwrap import dedent

from unittest import TestCase
from unittest.mock import patch, MagicMock, Mock, call

from src.command_kernel import CommandKernel, command


class Kernel(CommandKernel):
    @command('command1')
    def command1(self, code: str) -> str:
        return code

    @command('command2')
    def command2(self, code: str) -> str:
        return code


executed_code = dedent("""
    the code
    to be executed
""").strip()


kernel = Kernel()


@patch.object(kernel, attribute="command2", wraps=kernel.command2)
@patch.object(kernel, attribute="command1", wraps=kernel.command1)
class TestCommandsCall(TestCase):
    '''
    Test if commands called correctly.
    '''

    def test_order(self, command1: MagicMock, command2: MagicMock):
        '''
        Check that the methods are being called in correct order.
        '''

        recorder = Mock()
        recorder.attach_mock(command1, "c1")
        recorder.attach_mock(command2, "c2")

        kernel.do_execute(
            code="command1\n" + "command2\n" + executed_code
        )

        ans_order = recorder.mock_calls
        exp_order = [
            call.c1("command2\n" + executed_code),
            call.c2(executed_code)
        ]
        self.assertEqual(ans_order, exp_order)

    def test_pop_line(self, command1: MagicMock, command2: MagicMock):
        '''
        If method gets code to execute with command eliminated.
        '''
        kernel.do_execute(
            code="command2\n" + "command1\n" + executed_code
        )
        command2.assert_called_with("command1\n" + executed_code)
        command1.assert_called_with(executed_code)

    def test_code_update(self, command1: MagicMock, command2: MagicMock):
        '''
        If the otput of the command passed to the next command.
        '''
        command1_out = "updated code"
        command1.return_value = "command2\n" + command1_out
        kernel.do_execute(code="command1")
        command2.assert_called_with(command1_out)


@patch.object(kernel, attribute="always", wraps=kernel.command1)
class TestSpecialMethods(TestCase):
    """
    Test `always`: method that runned before any command.
    """
    @patch.object(kernel, attribute="command1", wraps=kernel.command2)
    def test_order(self, command1: MagicMock, always: MagicMock):
        '''
        Test if `always` is executed before command.
        '''
        recorder = Mock()
        recorder.attach_mock(always, "ar")
        recorder.attach_mock(command1, "c1")

        kernel.do_execute(code="command1")

        exp_order = [call.ar(code="command1"), call.c1('')]
        ans_order = recorder.mock_calls
        self.assertEqual(exp_order, ans_order)

    def test_input(self, always: MagicMock):
        '''
        Test if input passed correctly.
        '''
        code = ("command1\n" + "command2\n" + executed_code)
        kernel.do_execute(code=code)
        always.assert_called_once_with(code=code)


@patch.object(kernel, attribute="no_commands", wraps=kernel.command1)
class TestNoCommands(TestCase):
    '''
    Check that in case there is no specified commands the method
    `no_commands` is executed
    '''
    def test_no_commands(self, no_commands: MagicMock):
        kernel.do_execute(code=executed_code)
        no_commands.assert_called_once_with(executed_code)
