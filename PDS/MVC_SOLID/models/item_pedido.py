from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base

class ItemPedido(Base):
    __tablename__ = 'item_pedido'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id'))
    produto = Column(String(100))
    quantidade = Column(Integer)
    preco = Column(DECIMAL(10,2))

    pedido = relationship("Pedido", back_populates="itens")