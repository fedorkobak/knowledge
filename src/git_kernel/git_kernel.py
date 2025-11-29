from command_kernel import command
from tempdir_kernel import TempDirKernel


class GitKernel(TempDirKernel):
    '''
    The kernel that hides the process of creating a git repo.
    To start working with a new git repo,
    simply start the cell with the "magic" `%init`.
    '''

    @command('#init')
    def _init_dir(self, code: str = '') -> str:
        super()._init_dir()
        self.bashwrapper.run_command("git init")
        return code

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._init_dir('')
