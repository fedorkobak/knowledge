"""
An extension over the bash_kernel that allows hidden commands to be run
"""
from typing import Callable, Any
from bash_kernel.kernel import BashKernel
from traitlets.traitlets import MetaHasTraits


class CommandMeta(MetaHasTraits):
    '''
    Meta class that stores methods with the specified `_command` attribute in
    the `_commands` dictionary.
    '''
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls._commands = dict[str, Callable]()

        for base in bases:
            if hasattr(base, "_commands"):
                cls._commands.update(base._commands)

        for attribute in namespace.values():
            if hasattr(attribute, "_command"):
                cls._commands[attribute._command] = attribute


def command(command: str) -> Callable[
    [Callable[[Any, str], str]],
    Callable[[Any, str], str]
]:
    """
    The decorator adds the `_command` attribute to the decorated method.
    """
    def fun(method: Callable[[Any, str], str]) -> Callable[[Any, str], str]:
        method._command = command
        return method
    return fun


class CommandKernel(BashKernel, metaclass=CommandMeta):
    """
    You can define child classes where you implement additional functionality
    by defining methods and mapping them to the commands expected from the
    client in `command_dict`.
    Additionaly in the:
    - `always_runs`: method you can define the behaviour that will be executed
    each time any command executed.
    - `no_commands_run`: method you can define the behaviour that will be
    excuted if there is no commands provided in the input content.
    """
    def always_runs(self, code: str) -> str:
        return code

    def no_commands_run(self, code: str) -> str:
        return code

    def _run_commands(self, code: str) -> str:
        return code

    def do_execute(
        self,
        code: str,
        silent,
        store_history=True,
        user_expressions=None,
        allow_stdin=False
    ):
        pass
