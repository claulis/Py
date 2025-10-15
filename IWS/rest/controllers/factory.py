from sqlalchemy.orm import Session
from repositories.pedido_repository import PedidoRepository
from repositories.cliente_repository import ClienteRepository
from services.pedido_service import PedidoService
from services.cliente_service import ClienteService
from controllers.pedido_controller import PedidoController
from controllers.cliente_controller import ClienteController

class ControllerFactory:
    
    @staticmethod
    def create_pedido_controller(db: Session) -> PedidoController:
        repository = PedidoRepository(db)
        service = PedidoService(repository)
        return PedidoController(service)

    @staticmethod
    def create_cliente_controller(db: Session) -> ClienteController:
        repository = ClienteRepository(db)
        service = ClienteService(repository)
        return ClienteController(service)
