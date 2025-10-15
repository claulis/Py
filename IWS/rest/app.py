import asyncio
import platform
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config.database import engine, SessionLocal
from models.base import Base
from controllers.factory import ControllerFactory
from schemas.schema import *
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
def get_pedido_controller(db: Session = Depends(get_db)): 
    return ControllerFactory.create_pedido_controller(db)

def get_cliente_controller(db: Session = Depends(get_db)):
    return ControllerFactory.create_cliente_controller(db)

@app.get("/pedidos", response_model=List[PedidoOutSchema])
def listar_pedidos(controller = Depends(get_pedido_controller)):
    return controller.listar_pedidos()

@app.get("/pedidos/{pedido_id}", response_model=PedidoOutSchema)
def ler_pedido(pedido_id: int, controller = Depends(get_pedido_controller)):
    return controller.ler_pedido(pedido_id)

@app.post("/pedidos", response_model=PedidoOutSchema, status_code=201)
def criar_pedido(pedido_data: PedidoCreateSchema, controller = Depends(get_pedido_controller)):
    return controller.criar_pedido(pedido_data)

@app.put("/pedidos/{pedido_id}", response_model=PedidoOutSchema)
def atualizar_pedido(pedido_id: int, update_data: PedidoUpdateSchema, controller = Depends(get_pedido_controller)):
    return controller.atualizar_pedido(pedido_id, update_data)

@app.delete("/pedidos/{pedido_id}", status_code=204)
def deletar_pedido(pedido_id: int, controller= Depends(get_pedido_controller)):
    controller.deletar_pedido(pedido_id)
    return None

@app.get("/clientes", response_model=List[ClienteOutSchema])
def listar_clientes(controller = Depends(get_cliente_controller)):
    return controller.listar_clientes()

@app.get("/clientes/{cliente_id}", response_model=ClienteOutSchema)
def ler_cliente(cliente_id: int, controller = Depends(get_cliente_controller)):
    return controller.ler_cliente(cliente_id)

@app.post("/clientes", response_model=ClienteOutSchema, status_code=201)
def criar_cliente(cliente_data: ClienteCreateSchema, controller = Depends(get_cliente_controller)):
    return controller.criar_cliente(cliente_data)

@app.put("/clientes/{cliente_id}", response_model=ClienteOutSchema)
def atualizar_cliente(cliente_id: int, update_data: ClienteUpdateSchema, controller = Depends(get_cliente_controller)):
    return controller.atualizar_cliente(cliente_id, update_data)

@app.delete("/clientes/{cliente_id}", status_code=204)
def deletar_cliente(cliente_id: int, controller = Depends(get_cliente_controller)):
    controller.deletar_cliente(cliente_id)
    return None

if __name__ == "__main__":
    import uvicorn
    # Configurar SelectorEventLoop no Windows para evitar erros de conexão
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    uvicorn.run("app:app", host="localhost",port=8000, timeout_graceful_shutdown=10,
                   reload=True)