# repositorio_pedido.py
# Interface e classe responsáveis por salvar o pedido, respeitando SRP e DIP
from abc import ABC, abstractmethod

class RepositorioPedidoInterface(ABC):
    @abstractmethod
    def salvar(self, pedido):
        pass

class RepositorioPedido(RepositorioPedidoInterface):
    def salvar(self, pedido):
        print(f"Salvando pedido {pedido.id_pedido} no banco de dados")