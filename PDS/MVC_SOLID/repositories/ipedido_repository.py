from abc import ABC, abstractmethod
from typing import List
from datetime import date
from models.pedido import Pedido

class IPedidoRepository(ABC):
    @abstractmethod
    def create(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def read_by_id(self, pedido_id: int) -> Pedido:
        pass

    @abstractmethod
    def read_all(self) -> List[Pedido]:
        pass

    @abstractmethod
    def update(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def delete(self, pedido_id: int) -> None:
        pass