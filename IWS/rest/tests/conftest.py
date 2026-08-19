import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ.setdefault("API_KEY", "test-key")
# Garante que importar `app` (que importa config.database) nunca dependa de
# um MySQL disponível, mesmo que o ambiente de quem roda os testes tenha um
# .env configurado para produção. O engine real destas variáveis não chega a
# ser usado (a fixture `client` substitui get_db pelo `db_session` abaixo),
# mas fixamos os valores para que a simples importação seja sempre segura.
os.environ.setdefault("DB_BACKEND", "sqlite")
os.environ.setdefault("SQLITE_PATH", ":memory:")

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

import models.cliente  # noqa: F401 - garante o registro das tabelas em Base.metadata
import models.item_pedido  # noqa: F401
import models.pedido  # noqa: F401
from models.base import Base

TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture()
def db_session():
    # StaticPool mantém uma única conexão viva durante todo o teste: um
    # banco SQLite em memória existe apenas dentro de uma conexão, então o
    # pool padrão (que abre uma nova conexão por checkout) faria cada
    # operação enxergar um banco vazio diferente.
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client(db_session):
    import app as app_module

    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    # Sem "with": evita disparar o lifespan (que chamaria create_all no
    # engine real de produção) — as tabelas de teste já são criadas pela
    # fixture db_session, no engine SQLite em memória.
    app_module.app.dependency_overrides[app_module.get_db] = override_get_db
    test_client = TestClient(app_module.app)
    test_client.headers.update({"x-api-key": "test-key"})
    yield test_client
    app_module.app.dependency_overrides.clear()
