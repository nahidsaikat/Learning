import pytest
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid

from app.main import app
from app.dependencies import get_db, get_main_db
from app.tenant.utils import Base, set_tenant_id
from app.config import settings, get_tenant_db_url
from app.user.models import User

# Set testing mode
settings.TESTING = True

# Generate a unique test tenant ID
TEST_TENANT_ID = f"test_{uuid.uuid4().hex[:8]}"


@pytest.fixture(scope="session")
def test_db_url():
    """Create a test database URL."""
    return get_tenant_db_url(TEST_TENANT_ID)


@pytest.fixture(scope="session")
def test_engine(test_db_url):
    """Create a test database engine."""
    engine = create_engine(test_db_url)
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    yield engine
    
    # Drop all tables after tests
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def test_db(test_engine):
    """Create a test database session."""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    db = TestingSessionLocal()
    
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(test_db):
    """Create a test client with the test database."""
    def override_get_db():
        try:
            yield test_db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_main_db] = override_get_db
    
    with TestClient(app) as client:
        # Set tenant ID for testing
        client.headers.update({"X-Tenant-ID": TEST_TENANT_ID})
        yield client
    
    # Reset dependency overrides
    app.dependency_overrides = {}


@pytest.fixture(scope="function")
def test_user(test_db):
    """Create a test user."""
    user = User(
        email="test@example.com",
        username="testuser",
        hashed_password=User.get_password_hash("password123"),
        is_active=True
    )
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    
    yield user
    
    # Clean up
    test_db.delete(user)
    test_db.commit()


@pytest.fixture(scope="function")
def auth_headers(client, test_user):
    """Get authentication headers."""
    response = client.post(
        "/api/token",
        data={
            "username": test_user.username,
            "password": "password123",
        },
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
