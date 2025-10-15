from sqlalchemy import Column, Integer, String
from .base import Base

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    idade = Column(Integer)
     