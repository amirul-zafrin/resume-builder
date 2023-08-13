from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Entity = TypeVar("Entity")
PostModel = TypeVar("PostModel")
PatchModel = TypeVar("PatchModel")


class GenericServiceInterface(
    ABC,
    Generic[
        Entity,
        PostModel,
        PatchModel,
    ],
):
    """
    service interface class should inherit from this class.
    >>> class ExampleServiceInterface(
    ...     GenericServiceInterface[
    ...         ExampleEntity,
    ...         ExamplePostModel,
    ...         ExamplePatchModel,
    ...     ],
    ... ):
    ...     pass
    """

    @abstractmethod
    def get_all(self) -> list[Entity]:
        ...

    @abstractmethod
    def get_by_id(self, id: int) -> Entity:
        ...

    @abstractmethod
    def create(self, data: PostModel) -> Entity:
        ...

    @abstractmethod
    def update(self, id: int, data: PatchModel) -> Entity:
        ...

    @abstractmethod
    def delete(self, id: int) -> Entity:
        ...
