from datetime import date
from models.base import Base
from config.database import engine
from repositories.pedido_repository import PedidoRepository
from services.pedido_service import PedidoService
from views.pedido_view import PedidoView
from controllers.pedido_controller import PedidoController

# Criar tabelas no banco, se não existirem
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    repository = PedidoRepository()
    service = PedidoService(repository)
    view = PedidoView()
    controller = PedidoController(service, view)

    # Exemplo de criação e salvamento
    itens_data = [
        {'produto': 'Smartphone', 'quantidade': 1, 'preco': 1500.00},
        {'produto': 'Capinha', 'quantidade': 1, 'preco': 50.00}
    ]
    controller.criar_e_salvar_pedido('Claudio Ulisse', itens_data)

    # Exemplo de leitura por ID
    #controller.ler_e_exibir_pedido(1)  # Ajuste o ID conforme necessário

    # Exemplo de atualização
    # from datetime import date
    #controller.atualizar_e_exibir_pedido(20, novo_cliente="Claudio", nova_data=date(2025, 10, 1))

    # Exemplo de deleção
    #controller.deletar_e_exibir(19)  # Ajuste o ID conforme necessário

    # Exemplo de listagem
    controller.listar_e_exibir_pedidos()

    repository.close()