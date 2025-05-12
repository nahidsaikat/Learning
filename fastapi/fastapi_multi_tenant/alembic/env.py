from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Add the parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app.user.models import User
from app.article.models import Article
from app.tenant.models import Tenant
from app.tenant.utils import Base
from app.config import get_tenant_db_url

# Alembic Config object
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Set up the MetaData object
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    tenant_id = os.environ.get("TENANT_ID")
    if not tenant_id:
        raise ValueError("TENANT_ID environment variable is required")
    
    url = get_tenant_db_url(tenant_id)
    context.configure(
        url=url, 
        target_metadata=target_metadata, 
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    tenant_id = os.environ.get("TENANT_ID")
    if not tenant_id:
        raise ValueError("TENANT_ID environment variable is required")
    
    url = get_tenant_db_url(tenant_id)
    configuration = config.get_section(config.config_ini_section)
    configuration['sqlalchemy.url'] = url
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
