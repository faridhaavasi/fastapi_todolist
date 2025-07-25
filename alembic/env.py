import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv
from pathlib import Path

# ────────────────────────────────
# Setup .env and project path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")
sys.path.append(str(BASE_DIR))

# ────────────────────────────────
# Alembic Config
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", default='sqlite:///sqlite.db')
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("SQLALCHEMY_DATABASE_URL not set in .env or environment")

config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

# ────────────────────────────────
# Import models and metadata
from core.database import Base  # Base = declarative_base() or SQLModel.metadata
from tasks.models import *  # Needed to register models with metadata
from users.models import *

target_metadata = Base.metadata

# ────────────────────────────────
# Run migrations

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

# ────────────────────────────────

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
