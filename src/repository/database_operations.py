from src.repository.database_session import DBSession
from sqlalchemy import select


class DatabaseRepository():
    def __init__(self, entity) -> None:
        self.db_session = DBSession()
        self.db_entity = entity

    def execute(self, query):
        return self.db_session.execute(query)

    def get_all(self):
        """Return all objects"""
        get_query = select(self.db_entity)
        return self.execute(get_query).scalars().fetchall()

    def get_vehicles_by_owner_id(self, id: int):
        """Return one object filter by owner.id"""
        get_query = select(self.db_entity)
        return self.execute(get_query.where(self.db_entity.owner_id == id)).scalars().fetchall()
   
    def get_owner_by_document_number(self, document_number: str):
        """Return one object filter by uuid"""
        get_query = select(self.db_entity)
        return self.execute(get_query.where(self.db_entity.document_number == document_number)).scalars().fetchall()
    
    def create(self, data: dict):
        entity_object = self.db_entity(**data)
        self.db_session.add(entity_object)
        self.db_session.commit()
        return True
