'''
Abstrations that is used to create runners.
'''
import socket
import docker
import warnings
from abc import ABC, abstractmethod

from typing import Any
from typeguard import typechecked


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        return s.getsockname()[1]


# Format of the table output:
# The first element of the tuple is a tuple of column names.
# The second element is a tuple of rows, where each row is a separate tuple.
table_output = tuple[tuple[str, ...], tuple[tuple[Any, ...], ...]]


class DatabaseRunner(ABC):
    '''
    Describes database runner interface.
    '''
    def __init__(self):
        self.start()

    @abstractmethod
    def start(self):
        '''
        Initialization procedures. Called in the constructor.
        '''
        pass

    @abstractmethod
    def execute(self, code: str) -> tuple[list[str], list[table_output]]:
        '''
        Execute a query in the database and return the results.
        Resutls are suppoesd to be
        '''
        pass

    @abstractmethod
    def stop(self) -> None:
        '''
        Stop the runner and release the resources it uses.
        '''
        pass


class DatabaseInDockerRunner(DatabaseRunner):
    '''
    Abstract class for database runners that run in Docker containers.
    Determines:
    - Name of the container.
    - Port to connect to the database.

    Implement
    ---------
    _deafult_container_name: str
        Default name of the container to which will be added prefix.
    _image: str
        The image name to run.
    _port: int
        Port in the container to which will be mapped the port on the host.
    _other_params: dict[str, Any]
        Other parameters that are used by the `DockerClient.containers.run`
        method. For example, `environment` parameter for Postgres.

    Note: run `stop` method to remove the container. It's not correct to stop
    it automatically with the `__del__` method, because `container.stop()`
    requires some python features that can be destroyed by the moment `__del__`
    is callled.

    Parameters
    ----------
    Parameters that are used by the `DockerClient.containers.run` method.
    But note:
    - You can not to specify `name` parameter, because it will be generated
    automatically.
    - You can not to specify `detach` parameter, because it will be set to
    `True` automatically.
    - You can not to specify `remove` parameter, because it will be set to
    `True` automatically.

    Attributes
    -----------
    client: docker.client
        Docker client.
    _connection_port: int
        Port to connect to the database.
    container: docker.models.containers.Container
        Container object.
    '''
    _image: str
    _port: int
    _other_params: dict[str, Any]
    _default_container_name: str
    client = docker.from_env()

    def __init_subclass__(cls):
        attributes = ["_default_container_name", "_image", "_port"]
        for attr in attributes:
            if not hasattr(cls, attr):
                raise NotImplementedError(
                    f"Class {cls.__name__} must implement {attr} attribute"
                )
        return super().__init_subclass__()

    def __init__(self, **kwargs):
        params = self._proc_params(**kwargs)
        self._connection_port = params["ports"][self._port]
        self.container = self._get_container(**params)
        super().__init__()

    @classmethod
    def _proc_params(cls, **kwargs) -> dict[str, Any]:
        '''
        Process parameters for the container. Throw warnings if some
        parameters are redundant.
        '''
        redundant_params = {
            "image": cls._image,
            "detach": True,
            "remove": True,
            "ports": {cls._port: find_free_port()}
        }
        for param in redundant_params:
            if param in kwargs:
                warnings.warn(
                    f"Parameter {param} is redundant. It will be set "
                    "automatically."
                )
        kwargs.update(redundant_params)

        name = kwargs.get("name", None)
        kwargs["name"] = (
            cls._get_container_name() if name is None else name
        )

        if hasattr(cls, "_other_params"):
            kwargs = cls._other_params | kwargs

        return kwargs

    @classmethod
    def _get_containers_names(cls) -> list[str]:
        '''
        List all conatainers names.

        Returns
        -------
        list[str]
            List of all containers names.
        '''
        return [
            container.name for container in cls.client.containers.list()
        ]

    @classmethod
    def _get_container_name(cls) -> str:
        '''
        Create a name for the container. This is ususally a value returned by
        `_default_container_name` with a number suffix.
        '''
        suffix = 1
        containres_names = cls._get_containers_names()

        while True:
            container_name = (
                cls._default_container_name + "_" + str(suffix)
            )
            if container_name in containres_names:
                suffix += 1
            else:
                break
        return container_name

    def _get_container(self, **kwargs):
        '''
        Get the container object.
        '''
        return self.client.containers.run(**kwargs)

    def stop(self):
        self.container.stop()


class SeparateQueryRunner(DatabaseRunner):
    """
    Some database drivers don't allow to run SQL code that contains multiple
    statemnts. This class implements an `execute` method that splits code into
    into unit statements and send them to the `_execute_one` method, which
    should be reloaded by the ancestros.
    """
    @staticmethod
    def _separate_code(code: str) -> list[str]:
        """
        Splits a multi-statement SQL query into separate queries.
        """
        res: list[str] = code.split(";")
        res = [command.strip() for command in res]

        # If there is no any text after the last ';', remove everything.
        if res[-1].strip() == "":
            del res[-1]

        return res

    @abstractmethod
    def _execute_one(
        self, command: str
    ) -> tuple[list[str], list[table_output]]:
        """
        Execute separate query.

        Parameters
        ----------
        command: str
            SQL command to execute.

        Returns
        -------
        tuple[list[str], list[table_output]]
            - Messages returned by the query.
            - Tables returned by the query.
        """
        pass

    @typechecked
    def execute(self, code: str) -> tuple[list[str], list[table_output]]:
        """
        Executea SQL code that can contain multiple statements.

        Parameters
        ----------
        code: str
            SQL code to execute. It can contain multiple statements
            separated by semicolons.

        Returns
        -------
        tuple[list[str], list[table_output]]
            - Messages returned by the query.
            - Tables returned by the query.
        """
        commands = SeparateQueryRunner._separate_code(code)
        results = [self._execute_one(command=command) for command in commands]
        messages = [m for r in results for m in r[0]]
        tables = [t for r in results for t in r[1]]
        return messages, tables
