from typing import List
from models.cliente import Cliente
from repositories.icliente_repository import IClienteRepository
from schemas.schema import ClienteCreateSchema, ClienteUpdateSchema, ClienteOutSchema

class ClienteService:
    def __init__(self, repository: IClienteRepository):
        self.repository = repository

    def create_cliente(self, cliente_data: ClienteCreateSchema) -> Cliente:
        if not cliente_data.nome:
            raise ValueError(" Nome do cliente é obrigatório")
              
        cliente = Cliente(nome=cliente_data.nome,idade=cliente_data.idade)
        return self.repository.create(cliente)

    def read_cliente_by_id(self, cliente_id: int) -> Cliente:
        cliente = self.repository.read_by_id(cliente_id)
        if not cliente:
            raise ValueError("Cliente não encontrado")
        return cliente

    def read_all_clientes(self) -> List[Cliente]:
        return self.repository.read_all()

    def update_cliente(self, cliente_id: int, update_data: ClienteUpdateSchema) -> Cliente:
        cliente = self.read_cliente_by_id(cliente_id)
        if update_data.nome:
            cliente.nome = update_data.nome
        if update_data.idade:
            cliente.idade = update_data.idade
        return self.repository.update(cliente)

    def delete_cliente(self, cliente_id: int) -> None:
        self.repository.delete(cliente_id)