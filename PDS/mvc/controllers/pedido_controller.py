from sqlalchemy.exc import SQLAlchemyError
from config.database import SessionLocal
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from views.pedido_view import PedidoView

class PedidoController:
    def __init__(self):
        self.db = SessionLocal()
        self.view = PedidoView()  # Instancia a View

    def salvar_pedido(self, cliente, itens_data):
        try:
            pedido = Pedido(cliente=cliente)
            pedido.itens = [ItemPedido(**item) for item in itens_data]
            self.db.add(pedido)
            self.db.commit()
            self.db.refresh(pedido)
            return pedido
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao salvar pedido: {str(e)}")
        except Exception as e:
            raise ValueError(f"Erro inesperado: {str(e)}")

    def atualizar_pedido(self, pedido_id, novo_cliente=None, nova_data=None):
        try:
            pedido = self.db.get(Pedido, pedido_id)
            if not pedido:
                raise ValueError("Pedido não encontrado")
            if novo_cliente is not None:
                pedido.cliente = novo_cliente
            if nova_data is not None:
                pedido.data_pedido = nova_data
            self.db.commit()
            return pedido
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao atualizar pedido: {str(e)}")
        except Exception as e:
            raise ValueError(f"Erro inesperado: {str(e)}")

    def deletar_pedido(self, pedido_id):
        try:
            pedido = self.db.get(Pedido, pedido_id)
            if not pedido:
                raise ValueError("Pedido não encontrado")
            self.db.delete(pedido)
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao deletar pedido: {str(e)}")
        except Exception as e:
            raise ValueError(f"Erro inesperado: {str(e)}")

    def listar_pedidos_com_itens(self):
        try:
            return self.db.query(Pedido).all()
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao listar pedidos: {str(e)}")
        except Exception as e:
            raise ValueError(f"Erro inesperado: {str(e)}")

    def fechar(self):
        self.db.close()

    # Métodos que integram com View
    def criar_e_salvar_pedido(self, cliente, itens_data):
        try:
            pedido = self.salvar_pedido(cliente, itens_data)
            self.view.exibir_mensagem("Pedido salvo com sucesso!")
            return pedido
        except ValueError as e:
            self.view.exibir_erro(str(e))

    def deletar_e_exibir(self, pedido_id):
        try:
            self.deletar_pedido(pedido_id)
            self.view.exibir_mensagem("Pedido deletado com sucesso!")
        except ValueError as e:
            self.view.exibir_erro(str(e))

    def listar_e_exibir(self):
        try:
            pedidos = self.listar_pedidos_com_itens()
            self.view.exibir_pedidos(pedidos)
        except ValueError as e:
            self.view.exibir_erro(str(e))