import requests
import pytest

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"


# =============================
# GET
# =============================

def test_get_all_activities():
    response = requests.get(f"{BASE_URL}/Activities")
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, list)
    assert len(activities) > 0

def test_get_activities_by_id():
    response = requests.get(f"{BASE_URL}/Activities/1")
    assert response.status_code == 200
    activities = response.json()
    assert activities["id"] == 1
    assert "title" in activities
    assert "dueDate" in activities
    assert "completed" in activities

@pytest.mark.parametrize("activity_id", [1, 2, 3, 10])
def test_get_activities(activity_id):
    response = requests.get(f"{BASE_URL}/Activities/{activity_id}")
    assert response.status_code == 200
    assert response.json()["id"] == activity_id

def test_get_invalid_activities():
    response = requests.get(f"{BASE_URL}/Activities/999999")
    assert response.status_code == 404


# =============================
# POST
# =============================

def test_create_activities():
    # arrange
    payload = {
        "id": 100,
        "title": "Pytest Automation",
        "dueDate": "2026-07-08T00:00:00Z",
        "completed": True
    }
    #act
    response = requests.post(
        f"{BASE_URL}/Activities", 
        json=payload
    )
    #assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["title"] == payload["title"]
    assert response_data["dueDate"] == payload["dueDate"]
    assert response_data["completed"] == payload["completed"]
    

# =============================
# PUT
# =============================

def test_update_activities():
    # arrange
    activity_id = 1
    payload = {
        "id": activity_id,
        "title": "Updated title",
        "dueDate": "2026-07-08T00:00:00Z",
        "completed": True
    }
    #act
    response = requests.put(
        f"{BASE_URL}/Activities/{activity_id}", 
        json=payload
    )
    #assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["title"] == payload["title"]
    assert response_data["dueDate"] == payload["dueDate"]
    assert response_data["completed"] == payload["completed"]
    
def test_update_wrong_id_format():
    activity_id = "abc" #wrong format
    payload = {
        "id": activity_id,
        "title": "Updated title",
        "dueDate": "2026-07-08T00:00:00Z",
        "completed": True
    }
    response = requests.put(
        f"{BASE_URL}/Activities/{activity_id}",
        json=payload
    )
    print(response.status_code)
    print(response.json())
    assert response.status_code == 400


# =============================
# DELETE
# =============================

def test_delete_activities():
    activity_id = 1
    response = requests.delete(f"{BASE_URL}/Activities/{activity_id}")
    assert response.status_code == 200    

@pytest.mark.xfail(reason="FakeRestAPI does not validate resource existence")
def test_delete_non_existing_activities():
    activity_id = 999999
    response = requests.delete(f"{BASE_URL}/Activities/{activity_id}")
    assert response.status_code == 404