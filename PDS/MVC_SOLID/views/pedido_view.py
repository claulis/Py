from models.pedido import Pedido

class PedidoView:
    @staticmethod
    def exibir_pedidos(pedidos):
        for p in pedidos:
            print(f"Pedido {p.id} - Cliente: {p.cliente} - Data: {p.data_pedido}")
            for i in p.itens:
                print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}")

    @staticmethod
    def exibir_mensagem(mensagem):
        print(mensagem)

    @staticmethod
    def exibir_erro(erro):
        print(f"Erro: {erro}")