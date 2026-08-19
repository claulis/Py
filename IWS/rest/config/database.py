import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

load_dotenv()

# "sqlite" (padrão, não exige instalação de banco) ou "mysql".
DB_BACKEND = os.getenv("DB_BACKEND", "sqlite").strip().lower()


def _build_database_url(backend: str) -> str:
    if backend == "sqlite":
        # Caminho do arquivo .db, relativo ao diretório de onde a aplicação
        # é executada. Use ":memory:" para um banco volátil (perdido ao
        # encerrar o processo) — não recomendado para IWS/rest/app.py, pois
        # cada nova conexão do pool abriria um banco em memória diferente.
        sqlite_path = os.getenv("SQLITE_PATH", "./db_pedidos.db")
        return f"sqlite:///{sqlite_path}"

    if backend == "mysql":
        db_user = os.getenv("DB_USER", "root")
        db_password = os.getenv("DB_PASSWORD", "")
        db_host = os.getenv("DB_HOST", "localhost")
        db_name = os.getenv("DB_NAME", "db_pedidos")
        return f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}"

    raise ValueError(
        f"DB_BACKEND inválido: '{backend}'. Valores aceitos: 'sqlite' ou 'mysql'."
    )


DATABASE_URL = _build_database_url(DB_BACKEND)

# O driver sqlite3 recusa, por padrão, compartilhar uma conexão entre threads
# diferentes. O FastAPI executa rotas síncronas em uma thread de um pool,
# então essa checagem precisa ser desativada para o backend SQLite.
_connect_args = {"check_same_thread": False} if DB_BACKEND == "sqlite" else {}

engine = create_engine(DATABASE_URL, echo=False, connect_args=_connect_args)
SessionLocal = sessionmaker(bind=engine)
