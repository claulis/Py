# interfaces.py
# Interfaces abstratas para impressão e notificação, respeitando ISP
from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir_fatura(self):
        pass

class Notificavel(ABC):
    @abstractmethod
    def enviar_notificacao(self):
        pass