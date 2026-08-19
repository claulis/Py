import logging
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from typing import TypeVar, List, Type, Generic
from repositories.igeneric_repository import IGenericRepository

T = TypeVar("T")

logger = logging.getLogger(__name__)


class GenericRepository(IGenericRepository[T], Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def create(self, entity: T) -> T:
        try:
            self.db.add(entity)
            self.db.commit()
            self.db.refresh(entity)
            return entity
        except SQLAlchemyError:
            self.db.rollback()
            logger.exception("Erro ao criar entidade do tipo %s", self.model.__name__)
            raise ValueError("Erro ao criar entidade")

    def read_by_id(self, entity_id: int) -> T:
        try:
            return self.db.get(self.model, entity_id)
        except SQLAlchemyError:
            logger.exception(
                "Erro ao ler entidade do tipo %s (id=%s)", self.model.__name__, entity_id
            )
            raise ValueError("Erro ao ler entidade")

    def read_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        try:
            return self.db.query(self.model).offset(skip).limit(limit).all()
        except SQLAlchemyError:
            logger.exception("Erro ao listar entidades do tipo %s", self.model.__name__)
            raise ValueError("Erro ao listar entidades")

    def update(self, entity: T) -> T:
        try:
            self.db.commit()
            self.db.refresh(entity)
            return entity
        except SQLAlchemyError:
            self.db.rollback()
            logger.exception("Erro ao atualizar entidade do tipo %s", self.model.__name__)
            raise ValueError("Erro ao atualizar entidade")

    def delete(self, entity_id: int) -> None:
        entity = self.read_by_id(entity_id)
        if not entity:
            raise ValueError("Entidade não encontrada")
        try:
            self.db.delete(entity)
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            logger.exception(
                "Erro ao deletar entidade do tipo %s (id=%s)", self.model.__name__, entity_id
            )
            raise ValueError("Erro ao deletar entidade")
