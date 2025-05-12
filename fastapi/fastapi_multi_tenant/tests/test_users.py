import pytest
from fastapi import status


def test_register_user(client):
    """Test user registration."""
    response = client.post(
        "/api/register",
        json={
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "strongpassword123"
        }
    )
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["email"] == "newuser@example.com"
    assert data["username"] == "newuser"
    assert "id" in data


def test_register_duplicate_email(client, test_user):
    """Test registration with duplicate email."""
    response = client.post(
        "/api/register",
        json={
            "email": test_user.email,
            "username": "uniqueusername",
            "password": "strongpassword123"
        }
    )
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
