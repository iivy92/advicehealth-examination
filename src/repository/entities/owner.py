from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from src.repository.entities.base import BaseOrmEntity
from src.repository.entities.vehicle import Vehicle

class Owner(BaseOrmEntity):
    __tablename__ = 'owners'
    name = Column(String(128), nullable=False)
    document_number = Column(String(32), nullable=False, unique=True)
    sale_oportunity = Column(Boolean(), default=True)
    vehicle = relationship('Vehicle', back_populates='owner')

