from sqlalchemy.exc import SQLAlchemyError
from config.database import SessionLocal
from models.pedido import Pedido
from repositories.ipedido_repository import IPedidoRepository
from typing import List

class PedidoRepository(IPedidoRepository):
    def __init__(self):
        self.db = SessionLocal()

    def create(self, pedido: Pedido) -> Pedido:
        try:
            self.db.add(pedido)
            self.db.commit()
            self.db.refresh(pedido)
            return pedido
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao criar pedido: {str(e)}")

    def read_by_id(self, pedido_id: int) -> Pedido:
        try:
            return self.db.get(Pedido, pedido_id)
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao ler pedido: {str(e)}")

    def read_all(self) -> List[Pedido]:
        try:
            return self.db.query(Pedido).all()
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao listar pedidos: {str(e)}")

    def update(self, pedido: Pedido) -> Pedido:
        try:
            self.db.commit()
            self.db.refresh(pedido)
            return pedido
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao atualizar pedido: {str(e)}")

    def delete(self, pedido_id: int) -> None:
        try:
            pedido = self.read_by_id(pedido_id)
            if not pedido:
                raise ValueError("Pedido não encontrado")
            self.db.delete(pedido)
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao deletar pedido: {str(e)}")

    def close(self):
        self.db.close()