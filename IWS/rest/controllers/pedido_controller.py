from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from services.pedido_service import PedidoService
from schemas.schema import PedidoCreateSchema, PedidoUpdateSchema, PedidoOutSchema
from typing import List

class PedidoController:
    def __init__(self, service: PedidoService):
        self.service = service

    def listar_pedidos(self) -> List[PedidoOutSchema]:
        return self.service.read_all_pedidos()

    def ler_pedido(self, pedido_id: int) -> PedidoOutSchema:
        try:
            return self.service.read_pedido_by_id(pedido_id)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    def criar_pedido(self, pedido_data: PedidoCreateSchema) -> PedidoOutSchema:
        try:
            return self.service.create_pedido(pedido_data)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    def atualizar_pedido(self, pedido_id: int, update_data: PedidoUpdateSchema) -> PedidoOutSchema:
        try:
            return self.service.update_pedido(pedido_id, update_data)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    def deletar_pedido(self, pedido_id: int) -> None:
        try:
            self.service.delete_pedido(pedido_id)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))