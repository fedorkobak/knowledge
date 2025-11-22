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
    def always(self, code: str) -> str:
        return code

    def no_commands(self, code: str) -> str:
        return code

    def _pop_command(self, code: str) -> tuple[str, str]:
        """
        Pops potential command.

        Returns
        -------
        - First line of the input.
        - The remining input. Empty string if there is only one line in passed
        code.
        """
        ans = code.split("\n", 1)
        return (ans[0], ans[1]) if len(ans) > 1 else (ans[0], "")

    def _run_commands(self, code: str) -> str:
        """
        It pops the first line of `code` if it matches a command executes,
        that command passing the remaining `code`, and replaces `code` with
        the command's return value.
        The `always_runs` executes before all commands.
        If no commands found `no_commands_run` executes.
        """
        self.always(code=code)
        first = True
        while True:
            command, remaining = self._pop_command(code=code)

            if command in self._commands:
                # code = self._commands[command](self, remaining) Wrong
                # the method bounded to the command have to runned as attibute
                method = self._commands[command]
                method = getattr(self, method.__name__)
                code = method(remaining)
            else:
                if first:
                    code = self.no_commands(code)
                break

            first = False
        return code

    def do_execute(
        self,
        code: str,
        silent=True,
        store_history=True,
        user_expressions=None,
        allow_stdin=False
    ):
        code = self._run_commands(code)
        return super().do_execute(
            code, silent, store_history,
            user_expressions, allow_stdin
        )
