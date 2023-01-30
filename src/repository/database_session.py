from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.repository.entities.owner import Owner
from src.repository.entities.vehicle import Vehicle


engine = create_engine(url="postgresql+psycopg2://default:root@postgres/carford", pool_size=3)

Owner.__table__.create(bind=engine, checkfirst=True)
Vehicle.__table__.create(bind=engine, checkfirst=True)


DBSession = sessionmaker(engine, expire_on_commit=False, autoflush=False, autocommit=False)
