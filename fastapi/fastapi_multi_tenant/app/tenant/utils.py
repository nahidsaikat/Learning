from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Dict, Optional
from contextlib import contextmanager
import contextvars

from app.config import get_tenant_db_url, get_main_db_url

_tenant_id = contextvars.ContextVar('tenant_id')

Base = declarative_base()

_engines: Dict[str, any] = {}
_session_factories: Dict[str, any] = {}

main_engine = create_engine(get_main_db_url())
MainSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=main_engine)


def get_tenant_id() -> Optional[str]:
    """Get the current tenant ID from thread-local storage."""
    return _tenant_id.get(None)


def set_tenant_id(tenant_id: str) -> None:
    """Set the current tenant ID in thread-local storage."""
    _tenant_id.set(tenant_id)


def get_tenant_engine(tenant_id: str):
    """Get or create SQLAlchemy engine for a tenant."""
    if tenant_id not in _engines:
        db_url = get_tenant_db_url(tenant_id)
        _engines[tenant_id] = create_engine(db_url)
    return _engines[tenant_id]


def get_tenant_db():
    """Get a database session factory for the current tenant."""
    tenant_id = get_tenant_id()
    if not tenant_id:
        raise ValueError("Tenant ID not set in context")
    
    if tenant_id not in _session_factories:
        engine = get_tenant_engine(tenant_id)
        _session_factories[tenant_id] = sessionmaker(
            autocommit=False, autoflush=False, bind=engine
        )
    
    return _session_factories[tenant_id]


def get_main_db():
    """Get a database session factory for the main tenant registry."""
    return MainSessionLocal


@contextmanager
def tenant_db_session():
    """Get a database session for the current tenant."""
    db = get_tenant_db()
    session = db()
    try:
        yield session
    finally:
        session.close()
        

@contextmanager
def main_db_session():
    """Get a database session for the main tenant registry."""
    db = get_main_db()
    session = db()
    try:
        yield session
    finally:
        session.close()


def create_tenant_database(tenant_id: str) -> None:
    """Create a new database for a tenant if it doesn't exist."""
    # Note: In a production environment, you would need proper error handling
    # and permissions to create databases
    engine = get_tenant_engine(tenant_id)
    Base.metadata.create_all(bind=engine)


def initialize_tenant_tables(tenant_id: str) -> None:
    """Initialize database tables for a tenant."""
    engine = get_tenant_engine(tenant_id)
    Base.metadata.create_all(bind=engine)
