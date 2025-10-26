from pathlib import Path
from bash_kernel.kernel import BashKernel
from jinja2 import Environment, FileSystemLoader


class GitKernel(BashKernel):
    '''
    The kernel that hides the process of creating a git repo.
    To start working with a new git repo,
    simply start the cell with the "magic" `%init`.
    '''

    repo_path = "/tmp/git_temp"

    def _render_script(self) -> str:
        '''
        Builds the script that creates a new git repo.
        '''
        path = Path(__file__)
        env = Environment(loader=FileSystemLoader(path.parent))
        template = env.get_template("create_repo.sh.j2")
        return template.render(repo_path=self.repo_path)

    def do_execute(
        self,
        code,
        silent,
        store_history=True,
        user_expressions=None,
        allow_stdin=False
    ):
        command = self._render_script()
        self.bashwrapper.run_command(command=command)
        return super().do_execute(
            code, silent, store_history,
            user_expressions, allow_stdin
        )
