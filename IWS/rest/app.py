import asyncio
import platform
from contextlib import asynccontextmanager
from typing import List

from fastapi import APIRouter, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from config.database import engine, SessionLocal
from config.security import verificar_api_key
from controllers.factory import ControllerFactory
from models.base import Base
from schemas.schema import (
    ClienteCreateSchema,
    ClienteOutSchema,
    ClienteUpdateSchema,
    PedidoCreateSchema,
    PedidoOutSchema,
    PedidoUpdateSchema,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Criar tabelas no banco, se não existirem. Executado no startup em vez de no
    # momento da importação do módulo, para que importar `app` (ex.: em testes)
    # não dependa de uma conexão de banco disponível.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="API de Gerenciamento de Pedidos", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/health", tags=["health"])
def health_check():
    """Endpoint sem autenticação, usado por ferramentas de monitoramento."""
    return {"status": "ok"}


pedidos_router = APIRouter(
    prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_api_key)]
)
clientes_router = APIRouter(
    prefix="/clientes", tags=["clientes"], dependencies=[Depends(verificar_api_key)]
)


@pedidos_router.get("", response_model=List[PedidoOutSchema])
def listar_pedidos(
    skip: int = 0, limit: int = 100, controller=Depends(get_pedido_controller)
):
    return controller.listar_pedidos(skip, limit)


@pedidos_router.get("/{pedido_id}", response_model=PedidoOutSchema)
def ler_pedido(pedido_id: int, controller=Depends(get_pedido_controller)):
    return controller.ler_pedido(pedido_id)


@pedidos_router.post("", response_model=PedidoOutSchema, status_code=201)
def criar_pedido(pedido_data: PedidoCreateSchema, controller=Depends(get_pedido_controller)):
    return controller.criar_pedido(pedido_data)


@pedidos_router.put("/{pedido_id}", response_model=PedidoOutSchema)
def atualizar_pedido(
    pedido_id: int, update_data: PedidoUpdateSchema, controller=Depends(get_pedido_controller)
):
    return controller.atualizar_pedido(pedido_id, update_data)


@pedidos_router.delete("/{pedido_id}", status_code=204)
def deletar_pedido(pedido_id: int, controller=Depends(get_pedido_controller)):
    controller.deletar_pedido(pedido_id)
    return None


@clientes_router.get("", response_model=List[ClienteOutSchema])
def listar_clientes(
    skip: int = 0, limit: int = 100, controller=Depends(get_cliente_controller)
):
    return controller.listar_clientes(skip, limit)


@clientes_router.get("/{cliente_id}", response_model=ClienteOutSchema)
def ler_cliente(cliente_id: int, controller=Depends(get_cliente_controller)):
    return controller.ler_cliente(cliente_id)


@clientes_router.post("", response_model=ClienteOutSchema, status_code=201)
def criar_cliente(cliente_data: ClienteCreateSchema, controller=Depends(get_cliente_controller)):
    return controller.criar_cliente(cliente_data)


@clientes_router.put("/{cliente_id}", response_model=ClienteOutSchema)
def atualizar_cliente(
    cliente_id: int, update_data: ClienteUpdateSchema, controller=Depends(get_cliente_controller)
):
    return controller.atualizar_cliente(cliente_id, update_data)


@clientes_router.delete("/{cliente_id}", status_code=204)
def deletar_cliente(cliente_id: int, controller=Depends(get_cliente_controller)):
    controller.deletar_cliente(cliente_id)
    return None


app.include_router(pedidos_router)
app.include_router(clientes_router)


if __name__ == "__main__":
    import uvicorn

    # Configurar SelectorEventLoop no Windows para evitar erros de conexão
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    uvicorn.run(
        "app:app", host="localhost", port=8000, timeout_graceful_shutdown=10, reload=True
    )
