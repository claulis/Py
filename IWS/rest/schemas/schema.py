from pydantic import BaseModel, ConfigDict, Field
from datetime import date
from typing import List, Optional


class ItemPedidoSchema(BaseModel):
    produto: str
    quantidade: int = Field(gt=0)
    preco: float = Field(ge=0)


class PedidoCreateSchema(BaseModel):
    cliente: str
    itens: List[ItemPedidoSchema]


class PedidoUpdateSchema(BaseModel):
    cliente: Optional[str] = None
    data_pedido: Optional[date] = None
    itens: Optional[List[ItemPedidoSchema]] = None


class ItemPedidoOutSchema(ItemPedidoSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    pedido_id: int


class PedidoOutSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    cliente: str
    data_pedido: date
    itens: List[ItemPedidoOutSchema]


class ClienteOutSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    idade: int = Field(ge=0)


class ClienteCreateSchema(BaseModel):
    nome: str
    idade: int = Field(ge=0)


class ClienteUpdateSchema(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = Field(default=None, ge=0)
