import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import Header, HTTPException, status

load_dotenv()

API_KEY = os.getenv("API_KEY", "changeme")


def verificar_api_key(x_api_key: Optional[str] = Header(default=None)) -> None:
    # Header opcional de propósito: se fosse obrigatório (Header(...)), o
    # FastAPI devolveria 422 quando ausente, antes de chegar aqui. Queremos
    # sempre 401 para chave ausente ou inválida.
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Chave de API inválida ou ausente",
        )
