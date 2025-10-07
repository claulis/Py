import asyncio
import platform
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config.database import engine, SessionLocal
from models.base import Base
from repositories.pedido_repository import PedidoRepository
from services.pedido_service import PedidoService
from controllers.pedido_controller import PedidoController
from schemas.schema import PedidoCreateSchema, PedidoUpdateSchema, PedidoOutSchema
from typing import List

app = FastAPI(title="API de Gerenciamento de Pedidos")

# Criar tabelas no banco, se não existirem
Base.metadata.create_all(bind=engine)

# Dependência para sessão de banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependência para controlador
def get_controller(db: Session = Depends(get_db)):
    repository = PedidoRepository(db)
    service = PedidoService(repository)
    return PedidoController(service)

@app.get("/pedidos", response_model=List[PedidoOutSchema])
def listar_pedidos(controller: PedidoController = Depends(get_controller)):
    return controller.listar_pedidos()

@app.get("/pedidos/{pedido_id}", response_model=PedidoOutSchema)
def ler_pedido(pedido_id: int, controller: PedidoController = Depends(get_controller)):
    return controller.ler_pedido(pedido_id)

@app.post("/pedidos", response_model=PedidoOutSchema, status_code=201)
def criar_pedido(pedido_data: PedidoCreateSchema, controller: PedidoController = Depends(get_controller)):
    return controller.criar_pedido(pedido_data)

@app.put("/pedidos/{pedido_id}", response_model=PedidoOutSchema)
def atualizar_pedido(pedido_id: int, update_data: PedidoUpdateSchema, controller: PedidoController = Depends(get_controller)):
    return controller.atualizar_pedido(pedido_id, update_data)

@app.delete("/pedidos/{pedido_id}", status_code=204)
def deletar_pedido(pedido_id: int, controller: PedidoController = Depends(get_controller)):
    controller.deletar_pedido(pedido_id)
    return None

if __name__ == "__main__":
    import uvicorn
    # Configurar SelectorEventLoop no Windows para evitar erros de conexão
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    uvicorn.run(app, host="localhost", port=8000, timeout_graceful_shutdown=10)