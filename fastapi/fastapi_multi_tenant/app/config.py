from pydantic_settings import BaseSettings
from typing import Dict, Optional
import os


class TenantSettings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    class Config:
        env_file = ".env"
        extra = "allow"


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Multi-Tenant App"
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Main database for tenant registry
    MAIN_DB_USER: str
    MAIN_DB_PASSWORD: str
    MAIN_DB_HOST: str
    MAIN_DB_PORT: str = "3306"
    MAIN_DB_NAME: str = "tenant_registry"
    
    # Tenant database connection string template
    TENANT_DB_URL_TEMPLATE: str = "mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
    
    # Default tenant settings
    DEFAULT_TENANT_DB_USER: str
    DEFAULT_TENANT_DB_PASSWORD: str
    DEFAULT_TENANT_DB_HOST: str
    DEFAULT_TENANT_DB_PORT: str = "3306"
    
    # Testing settings
    TESTING: bool = False
    TEST_DB_SUFFIX: str = "_test"
    
    class Config:
        env_file = ".env"


settings = Settings()


def get_tenant_db_url(tenant_id: str) -> str:
    """Get the database URL for a specific tenant."""
    # In a production environment, you might fetch these from a secure store
    # or from the tenant registry database
    tenant_settings = TenantSettings(
        DB_USER=settings.DEFAULT_TENANT_DB_USER,
        DB_PASSWORD=settings.DEFAULT_TENANT_DB_PASSWORD,
        DB_HOST=settings.DEFAULT_TENANT_DB_HOST,
        DB_PORT=settings.DEFAULT_TENANT_DB_PORT,
        DB_NAME=f"{tenant_id}{settings.TEST_DB_SUFFIX if settings.TESTING else ''}"
    )
    
    return settings.TENANT_DB_URL_TEMPLATE.format(
        user=tenant_settings.DB_USER,
        password="root",
        host=tenant_settings.DB_HOST,
        port=tenant_settings.DB_PORT,
        db_name=tenant_settings.DB_NAME
    )


def get_main_db_url() -> str:
    """Get the database URL for the main tenant registry database."""
    db_name = f"{settings.MAIN_DB_NAME}{settings.TEST_DB_SUFFIX if settings.TESTING else ''}"
    return settings.TENANT_DB_URL_TEMPLATE.format(
        user=settings.MAIN_DB_USER,
        password=settings.MAIN_DB_PASSWORD,
        host=settings.MAIN_DB_HOST,
        port=settings.MAIN_DB_PORT,
        db_name=db_name
    )
