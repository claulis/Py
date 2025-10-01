from services.pedido_service import PedidoService
from views.pedido_view import PedidoView
from typing import List, Dict
from datetime import date

class PedidoController:
    def __init__(self, service: PedidoService, view: PedidoView):
        self.service = service
        self.view = view

    def criar_e_salvar_pedido(self, cliente: str, itens_data: List[Dict[str, any]]):
        try:
            pedido = self.service.create_pedido(cliente, itens_data)
            self.view.exibir_mensagem("Pedido salvo com sucesso!")
            return pedido
        except ValueError as e:
            self.view.exibir_erro(str(e))

    def ler_e_exibir_pedido(self, pedido_id: int):
        try:
            pedido = self.service.read_pedido_by_id(pedido_id)
            self.view.exibir_pedidos([pedido])
        except ValueError as e:
            self.view.exibir_erro(str(e))

    def listar_e_exibir_pedidos(self):
        try:
            pedidos = self.service.read_all_pedidos()
            self.view.exibir_pedidos(pedidos)
        except ValueError as e:
            self.view.exibir_erro(str(e))

    def atualizar_e_exibir_pedido(self, pedido_id: int, novo_cliente: str = None, nova_data: date = None):
        try:
            pedido = self.service.update_pedido(pedido_id, novo_cliente, nova_data)
            self.view.exibir_mensagem("Pedido atualizado com sucesso!")
            self.view.exibir_pedidos([pedido])
        except ValueError as e:
            self.view.exibir_erro(str(e))

    def deletar_e_exibir(self, pedido_id: int):
        try:
            self.service.delete_pedido(pedido_id)
            self.view.exibir_mensagem("Pedido deletado com sucesso!")
        except ValueError as e:
            self.view.exibir_erro(str(e))