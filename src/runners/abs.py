'''
Abstrations that is used to create runners.
'''
import socket
import docker
import warnings
from typing import Any
from abc import ABC, abstractmethod


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        return s.getsockname()[1]


# Annotation of the `execute` method
execute_output = tuple[tuple[str, ...], tuple[tuple[Any, ...], ...]]


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
    def execute(self, query: str) -> execute_output:
        '''
        Execute a query in the database and return the results.
        Resutls are suppoesd to be:
        - Sequence of column names.
        - Sequence of rows, where each row is a sequence of values.
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
    def _get_container_name(cls) -> None:
        '''
        Create a name for the container. This is ususally a value returned by
        `_default_container_name` with a number suffix.
        '''
        suffix = 1
        containres_names = cls._get_containers_names()
        while True:
            container_name = cls._default_container_name + "_" + str(suffix)
            if container_name in containres_names:
                suffix += 1
            else:
                return container_name

    def _get_container(self, **kwargs) -> docker.models.containers.Container:
        '''
        Get the container object.
        '''
        return self.client.containers.run(**kwargs)

    def stop(self):
        self.container.stop()
