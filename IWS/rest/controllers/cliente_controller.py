from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from services.cliente_service import ClienteService
from schemas.schema import ClienteCreateSchema, ClienteUpdateSchema, ClienteOutSchema
from typing import List

class ClienteController:
    def __init__(self, service: ClienteService):
        self.service = service

    def listar_clientes(self) -> List[ClienteOutSchema]:
        return self.service.read_all_clientes()

    def ler_cliente(self, cliente_id: int) -> ClienteOutSchema:
        try:
            return self.service.read_cliente_by_id(cliente_id)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    def criar_cliente(self, cliente_data: ClienteCreateSchema) -> ClienteOutSchema:
        try:
            return self.service.create_cliente(cliente_data)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    def atualizar_cliente(self, cliente_id: int, update_data: ClienteUpdateSchema) -> ClienteOutSchema:
        try:
            return self.service.update_cliente(cliente_id, update_data)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    def deletar_cliente(self, cliente_id: int) -> None:
        try:
            self.service.delete_cliente(cliente_id)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))