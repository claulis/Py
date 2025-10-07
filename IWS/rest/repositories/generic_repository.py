from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from typing import TypeVar, List, Type, Generic
from repositories.igeneric_repository import IGenericRepository

T = TypeVar("T")

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
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao criar entidade: {str(e)}")

    def read_by_id(self, entity_id: int) -> T:
        try:
            return self.db.get(self.model, entity_id)
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao ler entidade: {str(e)}")

    def read_all(self) -> List[T]:
        try:
            return self.db.query(self.model).all()
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao listar entidades: {str(e)}")

    def update(self, entity: T) -> T:
        try:
            self.db.commit()
            self.db.refresh(entity)
            return entity
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao atualizar entidade: {str(e)}")

    def delete(self, entity_id: int) -> None:
        try:
            entity = self.read_by_id(entity_id)
            if not entity:
                raise ValueError("Entidade não encontrada")
            self.db.delete(entity)
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Erro ao deletar entidade: {str(e)}")