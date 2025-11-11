"""
An extension over the bash_kernel that allows hidden commands to be run
"""
from typing import Callable, Self
from bash_kernel.kernel import BashKernel


class CommandKernel(BashKernel):
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
    commands_dict: dict[str, Callable[[Self, str], str]]

    def always_runs(self, code: str) -> str:
        return code

    def no_commands_run(self, code: str) -> str:
        return code

    def _parce_commands(self, code: str) -> str:
        """
        Looks for commands in the begining of the sent by the client content.
        """
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
