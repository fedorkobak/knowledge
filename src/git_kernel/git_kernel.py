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

    def _init_new_repo(self):
        command = self._render_script()
        self.bashwrapper.run_command(command=command)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._init_new_repo()

    def _render_script(self) -> str:
        '''
        Builds the script that creates a new git repo.
        '''
        path = Path(__file__)
        env = Environment(loader=FileSystemLoader(path.parent))
        template = env.get_template("create_repo.sh.j2")
        return template.render(repo_path=self.repo_path)

    def process_code(self, code: str) -> tuple[bool, str]:
        '''
        Takes code and looks for magic pattern in it.

        Parameters
        ----------
        code: str
            Code to be processed.

        Returns
        -------
        - True if new git repo has to be created.
        - Code that have to be executed.
        '''
        lines = code.splitlines()
        new_repo = lines[0].strip() == "%init"
        if new_repo:
            out_code = "\n".join(lines[1:])
        else:
            out_code = code

        return new_repo, out_code

    def do_execute(
        self,
        code,
        silent,
        store_history=True,
        user_expressions=None,
        allow_stdin=False
    ):
        new_repo, code = self.process_code(code=code)

        if new_repo:
            self._init_new_repo()

        return super().do_execute(
            code, silent, store_history,
            user_expressions, allow_stdin
        )
