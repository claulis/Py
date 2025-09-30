# main.py
# Exemplo de uso do sistema de gerenciamento de pedidos
from pedido import Pedido
from item import ItemFisico, ItemDigital
from processador_pagamento import PagamentoCartaoCredito
from repositorio_pedido import RepositorioPedido
from impressora_notificador import ImpressoraPedido, NotificadorCliente
from gerenciador_pedidos import GerenciadorPedidos

if __name__ == "__main__":
    # Criando itens
    livro = ItemFisico("Livro", 50.0)
    ebook = ItemDigital("E-book", 30.0)
    
    # Criando pedido
    pedido = Pedido(1, [livro, ebook])
    
    # Configurando dependências
    processador_pagamento = PagamentoCartaoCredito()
    repositorio = RepositorioPedido()
    impressora = ImpressoraPedido()
    notificador = NotificadorCliente()
    
    # Processando pedido
    gerenciador = GerenciadorPedidos(processador_pagamento, repositorio)
    gerenciador.processar_pedido(pedido)
    
    # Imprimindo e notificando
    impressora.imprimir_fatura()
    notificador.enviar_notificacao()
    
    # Calculando custos de envio
    print(f"Custo de envio do livro: {livro.calcular_custo_envio()}")
    print(f"Custo de envio do e-book: {ebook.calcular_custo_envio()}")