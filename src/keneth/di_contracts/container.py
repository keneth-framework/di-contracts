from abc import ABC, abstractmethod

from .container_context import ContainerContextInterface
from .service import ServiceInterface


class ContainerInterface(ABC):
    """Interface for dependency injection container."""

    @abstractmethod
    def call(self, func: callable) -> ServiceInterface:
        """Call a function or method with dependencies resolved.

        Args:
            func (callable): The function or method to call.
        Returns:
            ServiceInterface: An instance of the requested service.
        """

    @abstractmethod
    def provide(self, service_type: type[ServiceInterface]) -> ServiceInterface:
        """Provide an instance of the requested service type.

        Args:
            service_type (type[ServiceInterface]): The type of the service to provide.
        Returns:
            ServiceInterface: An instance of the requested service.
        """

    @abstractmethod
    def get_context(self) -> ContainerContextInterface:
        """Get the current container context.

        Returns:
            ContainerContextInterface: The current container context.
        """

    @abstractmethod
    def get_permanent_context(self) -> ContainerContextInterface:
        """Get the permanent container context.

        Returns:
            ContainerContextInterface: The permanent container context.
        """

    def get_binding(self, key: str) -> object | None:
        """Get a binding from the container context or permanent context.

        Args:
            key (str): The binding key.
        Returns:
            object | None: The binding value or None if not found.
        """
        val = self.get_context().get_binding(key)
        if val is not None:
            return val
        return self.get_permanent_context().get_binding(key)

    def get_instance_from_type(self, target_type: type) -> object | None:
        """Get a scoped instance from the container context by its type.

        Args:
            target_type (type): The type of the target to get.
        Returns:
            object | None: The target instance or None if not found.
        """
        instance = self.get_context().get_instance_from_type(target_type)
        if instance is not None:
            return instance
        return self.get_permanent_context().get_instance_from_type(target_type)
