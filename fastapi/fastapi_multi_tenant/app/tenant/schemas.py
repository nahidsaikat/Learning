from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TenantResponse(BaseModel):
    id: int
    name: str
    schema_name: str
    domain_url: str
    licensed_till: datetime
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class CreateTenant(BaseModel):
    name: str
    schema_name: str
    domain_url: str
    licensed_till: datetime
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
