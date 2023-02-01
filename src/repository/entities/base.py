from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy.orm.decl_api import DeclarativeMeta


class Base:
    id = Column(Integer(), primary_key=True, unique=True)


BaseOrmEntity: DeclarativeMeta = declarative_base(
    cls=Base
)
