from models import Pedido
from database import SessionLocal

class PedidoControl:
    def __init__(self):
        self.db = SessionLocal()

    def salvar_pedido(self, pedido):
        self.db.add(pedido)
        self.db.commit()
        self.db.refresh(pedido)
        return pedido

    def listar_pedidos_com_itens(self):
        return self.db.query(Pedido).all()

    def fechar(self):
        self.db.close()
