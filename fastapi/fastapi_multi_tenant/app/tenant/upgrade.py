import os
import subprocess


def upgrade_database(tenant_id: str):
    """
    Upgrade the database for a tenant
    """
    os.environ["TENANT_ID"] = tenant_id
    subprocess.run(["alembic", "upgrade", "head"], check=True, cwd="../../")

upgrade_database("tenant9")
