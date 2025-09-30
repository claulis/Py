# pedido.py
# Classe responsável por gerenciar os dados do pedido e calcular o total (SRP)

class Pedido:
    def __init__(self, id_pedido, itens):
        self.id_pedido = id_pedido
        self.itens = itens

    def calcular_total(self):
        return sum(item.preco for item in self.itens)