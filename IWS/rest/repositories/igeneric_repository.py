from abc import ABC, abstractmethod
from typing import TypeVar, List, Generic

T = TypeVar("T")  # Tipo genérico para entidades

class IGenericRepository(Generic[T], ABC):
    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def read_by_id(self, entity_id: int) -> T:
        pass

    @abstractmethod
    def read_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> None:
        pass
