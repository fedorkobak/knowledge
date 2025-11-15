from unittest import TestCase
from src.command_kernel import CommandMeta


class Commands(metaclass=CommandMeta):
    def method1(self):
        pass
    method1._command = "key1"

    def method2(self):
        pass
    method2._command = "key2"

    def method_witout_command(self):
        pass


class CommandsHeir(Commands):
    def heir_method(self):
        pass
    heir_method._command = "heir_command"

    def replace_method2(self):
        pass
    replace_method2._command = "key2"


class Heir2(CommandsHeir):
    pass


class TestCommandMeta(TestCase):
    def test_added_methods(self):
        """
        If `Commands` stores correct `_commands`
        """
        exp = {
            "key1": Commands.method1,
            "key2": Commands.method2
        }
        self.assertEqual(Commands._commands, exp)

    def test_heir_add(self):
        """
        If heir added `heir_method` correctly
        """
        self.assertTrue("heir_command" in CommandsHeir._commands)
        self.assertEqual(
            CommandsHeir._commands["heir_command"],
            CommandsHeir.heir_method
        )

    def test_replaced_in_heir(self):
        """
        If in heir the method under 'key2' correctly replaced.
        """
        self.assertEqual(
            CommandsHeir._commands["key2"],
            CommandsHeir.replace_method2
        )

    def test_order(self):
        """
        If command defined several times selects correct method.
        If `Heir2` takes the method from the latest ancestor `CommandHeir`,
        not from `Commands`.
        """
        self.assertEqual(
            Heir2._commands["key2"],
            CommandsHeir.replace_method2
        )
