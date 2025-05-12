from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.tenant.utils import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    schema_name = Column(String(255), nullable=False)
    domain_url = Column(String(255), nullable=False)
    licensed_till = Column(DateTime(timezone=True), server_default=func.now())

    db_name = Column(String(255), nullable=True)
    db_user = Column(String(255), nullable=True)
    db_password = Column(String(255), nullable=True)
    db_host = Column(String(255), nullable=True)
    db_port = Column(String(255), nullable=True)
    
    active = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
