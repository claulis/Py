from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from datetime import date
from .base import Base

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente = Column(String(100))
    data_pedido = Column(Date, default=date.today)
    itens = relationship("ItemPedido", back_populates="pedido", cascade="all, delete-orphan")