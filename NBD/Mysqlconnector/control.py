from models import Pedido, ItemPedido
from models import Pedido, ItemPedido

class PedidoControl:
    def __init__(self, db):
        self.db = db

    def salvar_pedido(self, pedido):
        pedido_query = "INSERT INTO pedido (cliente, data_pedido) VALUES (%s, %s)"
        cursor = self.db.execute_query(pedido_query, (pedido.cliente, pedido.data_pedido))
        if cursor:
            pedido.id = cursor.lastrowid
            item_query = "INSERT INTO item_pedido (pedido_id, produto, quantidade, preco) VALUES (%s, %s, %s, %s)"
            for item in pedido.itens:
                self.db.execute_query(item_query, (pedido.id, item.produto, item.quantidade, item.preco))

    def atualizar_pedido(self, pedido):
        if not pedido.id:
            raise ValueError("Pedido precisa ter ID para ser atualizado.")

        # Iniciar transação
        try:
            # Atualizar cabeçalho do pedido
            pedido_query = "UPDATE pedido SET cliente = %s, data_pedido = %s WHERE id = %s"
            self.db.execute_query(pedido_query, (pedido.cliente, pedido.data_pedido, pedido.id))

            # Deletar itens antigos
            delete_itens_query = "DELETE FROM item_pedido WHERE pedido_id = %s"
            self.db.execute_query(delete_itens_query, (pedido.id,))

            # Inserir novos itens
            item_query = "INSERT INTO item_pedido (pedido_id, produto, quantidade, preco) VALUES (%s, %s, %s, %s)"
            for item in pedido.itens:
                self.db.execute_query(item_query, (pedido.id, item.produto, item.quantidade, item.preco))

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def deletar_pedido(self, pedido_id):
        try:
            # Deletar itens primeiro (por FK)
            delete_itens_query = "DELETE FROM item_pedido WHERE pedido_id = %s"
            self.db.execute_query(delete_itens_query, (pedido_id,))

            # Deletar pedido
            delete_pedido_query = "DELETE FROM pedido WHERE id = %s"
            self.db.execute_query(delete_pedido_query, (pedido_id,))

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def listar_pedidos_com_itens(self):
        query = """
        SELECT p.id, p.cliente, p.data_pedido, i.produto, i.quantidade, i.preco
        FROM pedido p
        JOIN item_pedido i ON p.id = i.pedido_id
        ORDER BY p.id;
        """
        cursor = self.db.execute_query(query)
        pedidos = {}
        if cursor:
            for pedido_id, cliente, data_pedido, produto, quantidade, preco in cursor:
                if pedido_id not in pedidos:
                    pedidos[pedido_id] = Pedido(cliente, data_pedido)
                    pedidos[pedido_id].id = pedido_id
                item = ItemPedido(produto, quantidade, preco)
                pedidos[pedido_id].add_item(item)
        return list(pedidos.values())  # Retorna lista explícita