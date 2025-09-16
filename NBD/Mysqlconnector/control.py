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
        return pedidos.values()
