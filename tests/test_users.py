import requests
import pytest

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"


# =============================
# GET
# =============================

def test_get_all_users():
    response = requests.get(f"{BASE_URL}/Users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0

def test_get_user_by_id():
    response = requests.get(f"{BASE_URL}/Users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "userName" in user
    assert "password" in user

@pytest.mark.parametrize("user_id", [1, 2, 3, 10])
def test_get_user(user_id):
    response = requests.get(f"{BASE_URL}/Users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

def test_get_invalid_user():
    response = requests.get(f"{BASE_URL}/Users/999999")
    assert response.status_code == 404


# =============================
# POST
# =============================

def test_create_user():
    # arrange
    payload = {
        "id": 100,
        "userName": "Pytest Automation",
        "password": "testing"
    }
    #act
    response = requests.post(
        f"{BASE_URL}/Users", 
        json=payload
    )
    #assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["userName"] == payload["userName"]
    assert response_data["password"] == payload["password"]
    

# =============================
# PUT
# =============================

def test_update_user():
    # arrange
    user_id = 1
    payload = {
        "id": user_id,
        "userName": "Updated username",
        "password": "Updated password",
    }
    #act
    response = requests.put(
        f"{BASE_URL}/Users/{user_id}", 
        json=payload
    )
    #assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["userName"] == payload["userName"]
    assert response_data["password"] == payload["password"]
    
def test_update_wrong_id_format():
    user_id = "abc" #wrong format
    payload = {
        "id": user_id,
        "userName": "Updated",
        "password": "Updated",
    }
    response = requests.put(
        f"{BASE_URL}/Users/{user_id}",
        json=payload
    )
    print(response.status_code)
    print(response.json())
    assert response.status_code == 400


# =============================
# DELETE
# =============================

def test_delete_user():
    user_id = 1
    response = requests.delete(f"{BASE_URL}/Users/{user_id}")
    assert response.status_code == 200    

@pytest.mark.xfail(reason="FakeRestAPI does not validate resource existence")
def test_delete_non_existing_user():
    user_id = 999999
    response = requests.delete(f"{BASE_URL}/Users/{user_id}")
    assert response.status_code == 404