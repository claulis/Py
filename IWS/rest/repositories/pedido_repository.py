from sqlalchemy.orm import Session
from models.pedido import Pedido
from repositories.ipedido_repository import IPedidoRepository
from repositories.generic_repository import GenericRepository

class PedidoRepository(GenericRepository[Pedido], IPedidoRepository):
    def __init__(self, db: Session):
        super().__init__(db, Pedido)