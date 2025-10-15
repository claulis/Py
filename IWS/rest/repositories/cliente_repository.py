from sqlalchemy.orm import Session
from models.cliente import Cliente
from repositories.icliente_repository import IClienteRepository
from repositories.generic_repository import GenericRepository

class ClienteRepository(GenericRepository[Cliente], IClienteRepository):
    def __init__(self, db: Session):
        super().__init__(db, Cliente)