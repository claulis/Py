from abc import ABC
from models.cliente import Cliente
from repositories.igeneric_repository import IGenericRepository

class IClienteRepository(IGenericRepository[Cliente], ABC):
    pass