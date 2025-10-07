from abc import ABC
from models.pedido import Pedido
from repositories.igeneric_repository import IGenericRepository

class IPedidoRepository(IGenericRepository[Pedido], ABC):
    pass