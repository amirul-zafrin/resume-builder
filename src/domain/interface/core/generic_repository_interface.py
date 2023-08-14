from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

Entity = TypeVar("Entity")


class GenericRepositoryInterface(
    ABC,
    Generic[Entity],
):
    """
    repository interface class should inherit from this class.
    >>> class ExampleRepositoryInterface(
    ...     GenericRepositoryInterface[ExampleEntity]
    ... ):
    ...     pass
    """

    @abstractmethod
    def get_all(self) -> list[Optional[Entity]]:
        ...

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Entity]:
        ...

    @abstractmethod
    def create(self, data: dict) -> Entity:
        ...

    @abstractmethod
    def update(self, id: int, data: dict, target: Entity) -> Entity:
        ...

    @abstractmethod
    def delete(self, id: int, target: Entity) -> bool:
        ...
