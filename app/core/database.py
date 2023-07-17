import databases
from sqlalchemy import create_engine
from app.core.settings import config
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = config.database.url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()


metadata = Base.metadata
