from sqlalchemy import Column, Integer, String, Date, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship, declarative_base
from datetime import date

Base = declarative_base()

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente = Column(String(100))
    data_pedido = Column(Date, default=date.today)

    itens = relationship("ItemPedido", back_populates="pedido", cascade="all, delete-orphan")

class ItemPedido(Base):
    __tablename__ = 'item_pedido'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id'))
    produto = Column(String(100))
    quantidade = Column(Integer)
    preco = Column(DECIMAL(10,2))

    pedido = relationship("Pedido", back_populates="itens")
