import pytest

from config.database import _build_database_url


def test_build_database_url_sqlite_usa_caminho_padrao(monkeypatch):
    monkeypatch.delenv("SQLITE_PATH", raising=False)
    url = _build_database_url("sqlite")
    assert url == "sqlite:///./db_pedidos.db"


def test_build_database_url_sqlite_respeita_caminho_customizado(monkeypatch):
    monkeypatch.setenv("SQLITE_PATH", ":memory:")
    url = _build_database_url("sqlite")
    assert url == "sqlite:///:memory:"


def test_build_database_url_mysql_monta_string_de_conexao(monkeypatch):
    monkeypatch.setenv("DB_USER", "usuario1")
    monkeypatch.setenv("DB_PASSWORD", "senha123")
    monkeypatch.setenv("DB_HOST", "meuhost")
    monkeypatch.setenv("DB_NAME", "meubanco")
    url = _build_database_url("mysql")
    assert url == "mysql+mysqlconnector://usuario1:senha123@meuhost/meubanco"


def test_build_database_url_backend_invalido_gera_erro():
    with pytest.raises(ValueError):
        _build_database_url("postgres")
