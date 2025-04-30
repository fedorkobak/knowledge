import traceback
from typing import Any
from tabulate import tabulate
from ipykernel.kernelbase import Kernel

from .runners.runners import (
    DatabaseRunner,
    PostgresRunner,
    ClickHouseRunner,
    SQLiteRunner
)


def display_data(
    header: tuple[str],
    rows: tuple[tuple[Any]]
) -> dict[str, Any]:
    d = {
        'data': {
            'text/latex': tabulate(rows, header, tablefmt='latex_booktabs'),
            'text/plain': tabulate(rows, header, tablefmt='simple'),
            'text/html': tabulate(rows, header, tablefmt='html'),
        },
        'metadata': {}
    }
    return d


class SQLKernel(Kernel):
    implementation = 'sql'
    implementation_version = '0.0'
    language_info = {
        'name': 'sql',
        'mimetype': 'text/plain',
        'file_extentions': '.sql'
    }
    banner = "Special implementation of sql"

    # Mapping to which header corresponds which runner
    runners: dict[str, DatabaseRunner] = {
        "postgreSQL": PostgresRunner(),
        "ClickHouse": ClickHouseRunner(),
        "sqlite": SQLiteRunner()
    }

    runner_parsing_error = ValueError(
        "The first line must start with '--<runner identifier>'. ",
        "Where <runner identifier> can take values:",
        ", ".join(runners.keys())
    )

    def _parse_runner(self, code: str) -> DatabaseRunner:
        first_line = code.strip().splitlines()[0]

        if not first_line.startswith("--"):
            raise self.runner_parsing_error

        runner_identifier = first_line[2:].strip()
        runner = self.runners.get(runner_identifier)
        if runner is None:
            raise self.runner_parsing_error

        return runner

    def do_execute(
        self,
        code: str,
        silent,
        store_history=True,
        user_expressions=None,
        allow_stdin=False
    ):
        try:
            runner = self._parse_runner(code=code)
            header, rows = runner.execute(code)
        except Exception as e:
            tb_list = traceback.format_exception(type(e), e, e.__traceback__)
            self.send_response(
                self.iopub_socket,
                "stream",
                {
                    'name': 'stderr',
                    'text': "".join(tb_list)
                }
            )
            return {
                'status': 'error',
                'ename': str(type(e).__name__),
                'evalue': str(e),
                'traceback': tb_list
            }

        self.send_response(
            self.iopub_socket,
            'display_data',
            display_data(header=header, rows=rows)
        )

        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }

    def do_shutdown(self, restart: bool):
        for runner in self.runners.values():
            runner.stop()


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=SQLKernel)
