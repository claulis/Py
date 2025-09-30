from models.base import Base
from config.database import engine
from controllers.pedido_controller import PedidoController

# Criar tabelas no banco, se não existirem
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    controller = PedidoController()

    # Exemplo de criação e salvamento
    itens_data = [
        {'produto': 'Smartphone', 'quantidade': 1, 'preco': 1500.00},
        {'produto': 'Capinha', 'quantidade': 1, 'preco': 50.00}
    ]
    controller.criar_e_salvar_pedido('Ana Paula', itens_data)

    # Exemplo de deleção
    controller.deletar_e_exibir(18)  # Ajuste o ID conforme necessário

    # Exemplo de listagem
    controller.listar_e_exibir()

    controller.fechar()