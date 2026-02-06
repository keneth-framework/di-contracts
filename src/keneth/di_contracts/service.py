from abc import ABC, abstractmethod


class ServiceInterface(ABC):
    """Service Interface used by DI container to detect services to instantiate."""

    @abstractmethod
    def is_service() -> bool:
        """Check if the class is a service."""
        return True
