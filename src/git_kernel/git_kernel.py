from pathlib import Path
from command_kernel import CommandKernel, command
from jinja2 import Environment, FileSystemLoader


class GitKernel(CommandKernel):
    '''
    The kernel that hides the process of creating a git repo.
    To start working with a new git repo,
    simply start the cell with the "magic" `%init`.
    '''

    repo_path = "/tmp/git_temp"

    @command('%init')
    def _init_new_repo(self, code: str = '') -> str:
        command = self._render_script()
        self.bashwrapper.run_command(command=command)
        return code

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._init_new_repo('')

    def _render_script(self) -> str:
        '''
        Builds the script that creates a new git repo.
        '''
        path = Path(__file__)
        env = Environment(loader=FileSystemLoader(path.parent))
        template = env.get_template("create_repo.sh.j2")
        return template.render(repo_path=self.repo_path)
