from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.repository.entities.base import BaseOrmEntity
from sqlalchemy.dialects.postgresql import UUID


class Vehicle(BaseOrmEntity):
    __tablename__ = 'vehicles'
    license_plate = Column(String(32), nullable=False, unique=True)
    color = Column(String(32), nullable=False)
    model = Column(String(32), nullable=False)
    owner_id = Column(Integer(), ForeignKey("owners.id"), nullable=False)
    owner = relationship('Owner', back_populates='vehicle')