from typing import List, Dict
from datetime import date
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from repositories.ipedido_repository import IPedidoRepository

class PedidoService:
    def __init__(self, repository: IPedidoRepository):
        self.repository = repository

    def create_pedido(self, cliente: str, itens_data: List[Dict[str, any]]) -> Pedido:
        if not cliente:
            raise ValueError("Cliente é obrigatório")
        if not itens_data:
            raise ValueError("Pelo menos um item é obrigatório")
        
        pedido = Pedido(cliente=cliente)
        pedido.itens = [ItemPedido(**item) for item in itens_data]
        return self.repository.create(pedido)

    def read_pedido_by_id(self, pedido_id: int) -> Pedido:
        pedido = self.repository.read_by_id(pedido_id)
        if not pedido:
            raise ValueError("Pedido não encontrado")
        return pedido

    def read_all_pedidos(self) -> List[Pedido]:
        return self.repository.read_all()

    def update_pedido(self, pedido_id: int, novo_cliente: str = None, nova_data: date = None) -> Pedido:
        pedido = self.read_pedido_by_id(pedido_id)
        if novo_cliente:
            pedido.cliente = novo_cliente
        if nova_data:
            pedido.data_pedido = nova_data
        return self.repository.update(pedido)

    def delete_pedido(self, pedido_id: int) -> None:
        self.repository.delete(pedido_id)