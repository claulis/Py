# item.py
# Classes para itens do pedido, respeitando LSP

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class ItemFisico(Item):
    def calcular_custo_envio(self):
        return 10.0  # Custo fixo de envio

class ItemDigital(Item):
    def calcular_custo_envio(self):
        return 0.0  # Produtos digitais não têm custo de envio