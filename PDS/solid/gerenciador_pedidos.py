# gerenciador_pedidos.py
# Classe para gerenciar pedidos, respeitando DIP
from processador_pagamento import ProcessadorPagamento
from repositorio_pedido import RepositorioPedido

class GerenciadorPedidos:
    def __init__(self, processador_pagamento: ProcessadorPagamento, repositorio: RepositorioPedido):
        self.processador_pagamento = processador_pagamento
        self.repositorio = repositorio

    def processar_pedido(self, pedido):
        total = pedido.calcular_total()
        self.processador_pagamento.processar_pagamento(total)
        self.repositorio.salvar(pedido)