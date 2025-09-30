# impressora_notificador.py
# Classes para impressão e notificação, respeitando ISP
from interfaces import Imprimivel, Notificavel

class ImpressoraPedido(Imprimivel):
    def imprimir_fatura(self):
        print("Imprimindo fatura do pedido")

class NotificadorCliente(Notificavel):
    def enviar_notificacao(self):
        print("Enviando notificação ao cliente")