from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.tenant.views import tenant_router
from app.tenant.middleware import TenantMiddleware
from app.article.views import article_router
from app.config import settings
from app.user.views import user_router

app = FastAPI(
    title=settings.APP_NAME,
    description="A multi-tenant RESTful API with user authentication and article management",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(TenantMiddleware)

app.include_router(tenant_router)
app.include_router(article_router, prefix="/api")
app.include_router(user_router, prefix="/api")


@app.get("/", tags=["root"])
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
