from abc import ABC, abstractmethod
from typing import Self, TypeVar

from .service import ServiceInterface

T = TypeVar("T")


class ContainerContextInterface(ABC):
    """Container Context Interface. Used to define context values for the Container.

    Definitions:
        Context's binding: the last layer of resolving before error: associate an
            expected argument name to a value: useful for environment variables
        Context's target: list of dependencies in current resolving process.
            Used to detect circular dependencies.
        Context's instance: Used for context related class resolving.
            Used for example for the current Request in a web framework.
    """

    @abstractmethod
    def add_binding(self, key: str, value: T) -> Self:
        """Add a binding to the container context.

        Args:
            key (str): The binding key.
            value (T): The binding value.
        """

    @abstractmethod
    def get_binding(self, key: str) -> T:
        """Get a binding from the container context.

        Args:
            key (str): The binding key.
        Returns:
            T: The binding value.
        """

    @abstractmethod
    def add_target(self, target: type[ServiceInterface]) -> Self:
        """Add a target to the container context.

        Args:
            target (type[ServiceInterface]): The target to add.
        """

    @abstractmethod
    def get_targets(self) -> list[type[ServiceInterface]]:
        """Get all targets from the container context.

        Returns:
            list[type[ServiceInterface]]: The list of targets.
        """

    @abstractmethod
    def add_instance(self, target: object) -> Self:
        """Add a scoped instance to the container context.

        Args:
            target (object): The target to add.
        """

    @abstractmethod
    def get_instance_from_type(self, target_type: type[T]) -> T | None:
        """Get a scoped instance from the container context by its type.

        Args:
            target_type (type[T]): The type of the target to get.
        Returns:
            T | None: The target instance or None if not found.
        """

    @abstractmethod
    def clear_instances(self) -> None:
        """Clear all scoped instances from the container context."""
