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
    
    def deletar_pedido(self, pedido_id):
        pedido = self.db.query(Pedido).filter(Pedido.id == pedido_id).first()
        if not pedido:
            raise ValueError(f"Pedido com ID {pedido_id} não encontrado.")

        # Deleta os itens associados (geralmente feito automaticamente pelo cascade, mas vamos garantir)
        for item in pedido.itens:
            self.db.delete(item)

        # Deleta o pedido
        self.db.delete(pedido)
        self.db.commit()
    
    def atualizar_pedido(self, pedido):
        self.db.add(pedido)
        self.db.commit()
        self.db.refresh(pedido)
        return pedido

    def atualizar_pedido(self, pedido):
        # Verifica se o pedido existe no banco
        db_pedido = self.db.query(Pedido).filter(Pedido.id == pedido.id).first()
        if not db_pedido:
            raise ValueError(f"Pedido com ID {pedido.id} não encontrado.")

        # Atualiza os campos do cabeçalho
        db_pedido.cliente = pedido.cliente
        db_pedido.data_pedido = pedido.data_pedido

        # Se os itens forem gerenciados como relationship (ex: pedido.itens), 
        # podemos substituir completamente a lista (abordagem simples e segura)
        # Isso requer que `pedido.itens` seja uma lista atualizada de objetos ItemPedido

        # Primeiro, remove todos os itens antigos (opcional: só se quiser substituir tudo)
        for item in db_pedido.itens:
            self.db.delete(item)

        # Adiciona os novos itens
        for item in pedido.itens:
                 # Se necessário, associa o item ao pedido (caso não esteja feito)
            item.pedido_id = db_pedido.id  # ou item.pedido = db_pedido, dependendo do modelo
            self.db.add(item)

        self.db.commit()
        self.db.refresh(db_pedido)
        return db_pedido
    
    def listar_pedidos_com_itens(self):
        return self.db.query(Pedido).all()

    def fechar(self):
        self.db.close()
