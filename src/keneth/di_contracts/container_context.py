from abc import ABC, abstractmethod
from typing import Any, Self

from .container_context_target import ContainerContextTarget

class ContainerContextInterface(ABC):
    """Container Context Interface. Used to define context values for the DI Container."""
    
    @abstractmethod
    def add_binding(self, key: str, value: Any) -> Self:
        """
        Add a binding to the container context.

        Args:
            key (str): The binding key.
            value (Any): The binding value.
        """
    
    @abstractmethod
    def get_binding(self, key: str) -> Any:
        """
        Get a binding from the container context.

        Args:
            key (str): The binding key.
        Returns:
            Any: The binding value.
        """
    
    @abstractmethod
    def add_target(self, target: ContainerContextTarget) -> Self:
        """
        Add a target to the container context.

        Args:
            target (ContainerContextTarget): The target to add.
        """
    
    @abstractmethod
    def get_targets(self) -> list[ContainerContextTarget]:
        """
        Get all targets from the container context.

        Returns:
            list[ContainerContextTarget]: The list of targets.
        """
