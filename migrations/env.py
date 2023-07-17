import app.blog.models
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

from app.core.settings import config as app_config
from app.core.database import metadata as db

config = context.config
fileConfig(config.config_file_name)
target_metadata = db


def run_migrations_online():
    connectable = create_engine(app_config.database.url)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()