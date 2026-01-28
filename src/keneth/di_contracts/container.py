from abc import ABC, abstractmethod
from typing import Optional, Type

from .container_context import ContainerContextInterface
from .service import ServiceInterface


class ContainerInterface(ABC):
    """
    Interface for dependency injection.
    """

    @abstractmethod
    def call(
        self, func: callable, context: Optional[ContainerContextInterface] = None
    ) -> ServiceInterface:
        """
        Call a function or method with dependencies resolved.

        Args:
            service_type (Type[ServiceInterface]): The type of the service to provide.
            context (Optional[ContainerContextInterface], optional): The container context. Defaults to None.
        Returns:
            ServiceInterface: An instance of the requested service.
        """

    @abstractmethod
    def provide(
        self,
        service_type: Type[ServiceInterface],
        context: Optional[ContainerContextInterface] = None,
    ) -> ServiceInterface:
        """
        Provide an instance of the requested service type.

        Args:
            service_type (Type[ServiceInterface]): The type of the service to provide.
            context (Optional[ContainerContextInterface], optional): The container context. Defaults to None.
        Returns:
            ServiceInterface: An instance of the requested service.
        """
