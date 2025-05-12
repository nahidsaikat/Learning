from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import re

from app.tenant.utils import get_tenant_id, set_tenant_id

# Regular expression for tenant ID validation
TENANT_ID_PATTERN = re.compile(r'^[a-z0-9_]+$')


class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        # Extract tenant ID from header or subdomain
        tenant_id = self._get_tenant_id(request)
        
        if not tenant_id:
            return Response(
                status_code=status.HTTP_400_BAD_REQUEST,
                content="Tenant ID not provided",
            )
        
        # Validate tenant ID format
        if not TENANT_ID_PATTERN.match(tenant_id):
            return Response(
                status_code=status.HTTP_400_BAD_REQUEST,
                content="Invalid tenant ID format",
            )
        
        # Set tenant ID in thread-local context
        set_tenant_id(tenant_id)
        
        # Process the request
        response = await call_next(request)
        
        return response
    
    def _get_tenant_id(self, request: Request) -> str:
        """
        Extract tenant ID from request.
        Priority: 
        1. X-Tenant-ID header
        2. Subdomain
        """
        # Try to get from header
        tenant_id = request.headers.get("X-Tenant-ID")
        if tenant_id:
            return tenant_id
        
        # Try to get from subdomain
        host = request.headers.get("host", "")
        if host and "." in host:
            subdomain = host.split(".")[0]
            if subdomain != "www":
                return subdomain
        
        return None
