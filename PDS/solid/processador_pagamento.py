# processador_pagamento.py
# Classes para processamento de pagamento, respeitando OCP
from abc import ABC, abstractmethod

class ProcessadorPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

class PagamentoCartaoCredito(ProcessadorPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} via cartão de crédito")

class PagamentoPayPal(ProcessadorPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} via PayPal")