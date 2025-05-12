from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.tenant.services import create_connection, create_database, upgrade_database
from app.tenant.utils import get_tenant_id
from app.utils.auth import get_current_active_user
from app.user.models import User
from app.dependencies import get_db
from app.tenant.schemas import CreateTenant, TenantResponse
from app.tenant.models import Tenant


tenant_router = APIRouter(tags=["tenant"])

@tenant_router.post("/tenant", response_model=TenantResponse)
def create_tenant(
    tenant: CreateTenant,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    tenant_id = get_tenant_id()
    if tenant_id != "tenant_registry":
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to create a tenant"
        )

    db_tenant = Tenant(
        **tenant.model_dump()
    )
    
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)

    connection = create_connection(db_tenant.db_host, db_tenant.db_user, db_tenant.db_password)
    create_database_query = f"CREATE DATABASE IF NOT EXISTS {db_tenant.db_name}"
    create_database(connection, create_database_query)

    upgrade_database(tenant_id=db_tenant.db_name)
    
    return db_tenant
