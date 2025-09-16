from datetime import date

class Pedido:
    def __init__(self, cliente, data_pedido=None):
        self.id = None
        self.cliente = cliente
        self.data_pedido = data_pedido or date.today()
        self.itens = []

    def add_item(self, item):
        self.itens.append(item)

class ItemPedido:
    def __init__(self, produto, quantidade, preco):
        self.id = None
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
