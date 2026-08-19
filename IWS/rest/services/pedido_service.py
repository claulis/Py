from typing import List
from datetime import date
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from repositories.ipedido_repository import IPedidoRepository
from schemas.schema import PedidoCreateSchema, PedidoUpdateSchema, PedidoOutSchema

class PedidoService:
    def __init__(self, repository: IPedidoRepository):
        self.repository = repository

    def create_pedido(self, pedido_data: PedidoCreateSchema) -> Pedido:
        if not pedido_data.cliente:
            raise ValueError("Cliente é obrigatório")
        if not pedido_data.itens:
            raise ValueError("Pelo menos um item é obrigatório")
        
        pedido = Pedido(cliente=pedido_data.cliente)
        pedido.itens = [ItemPedido(**item.model_dump()) for item in pedido_data.itens]
        return self.repository.create(pedido)

    def read_pedido_by_id(self, pedido_id: int) -> Pedido:
        pedido = self.repository.read_by_id(pedido_id)
        if not pedido:
            raise ValueError("Pedido não encontrado")
        return pedido

    def read_all_pedidos(self, skip: int = 0, limit: int = 100) -> List[Pedido]:
        return self.repository.read_all(skip, limit)

    def update_pedido(self, pedido_id: int, update_data: PedidoUpdateSchema) -> Pedido:
        pedido = self.read_pedido_by_id(pedido_id)
        if update_data.cliente is not None:
            pedido.cliente = update_data.cliente
        if update_data.data_pedido is not None:
            pedido.data_pedido = update_data.data_pedido
        if update_data.itens is not None:
            pedido.itens = [ItemPedido(**item.model_dump()) for item in update_data.itens]
        return self.repository.update(pedido)

    def delete_pedido(self, pedido_id: int) -> None:
        self.repository.delete(pedido_id)