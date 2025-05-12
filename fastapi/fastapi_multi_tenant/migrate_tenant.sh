# Set the tenant ID
export TENANT_ID=tenant1

# Run migrations
alembic revision --autogenerate -m "modify tenant model"
