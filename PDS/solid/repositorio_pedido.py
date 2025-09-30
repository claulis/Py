# repositorio_pedido.py
# Classe responsável por salvar o pedido, respeitando SRP

class RepositorioPedido:
    def salvar(self, pedido):
        print(f"Salvando pedido {pedido.id_pedido} no banco de dados")