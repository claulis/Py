from models import Base, Pedido, ItemPedido
from database import engine
from control import PedidoControl

# Criar tabelas no banco, se não existirem
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    control = PedidoControl()

    pedido = Pedido(cliente='Ana Paula')
    pedido.itens = [
        ItemPedido(produto='Smartphone', quantidade=1, preco=1500.00),
        ItemPedido(produto='Capinha', quantidade=1, preco=50.00)
    ]

    
    control.salvar_pedido(pedido)
    control.deletar_pedido(6)
    pedidos = control.listar_pedidos_com_itens()
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente} - Data: {p.data_pedido}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}")
    
    control.fechar()


