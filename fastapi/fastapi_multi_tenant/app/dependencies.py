from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Generator

from app.tenant.utils import tenant_db_session, main_db_session


def get_db() -> Generator[Session, None, None]:
    """
    Dependency to get the database session for the current tenant.
    """
    with tenant_db_session() as session:
        yield session


def get_main_db() -> Generator[Session, None, None]:
    """
    Dependency to get the database session for the main tenant registry.
    """
    with main_db_session() as session:
        yield session
