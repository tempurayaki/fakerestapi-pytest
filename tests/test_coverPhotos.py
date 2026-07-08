import requests
import pytest

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"


# =============================
# GET
# =============================

def test_get_all_coverPhotos():
    response = requests.get(f"{BASE_URL}/CoverPhotos")
    assert response.status_code == 200
    coverPhotos = response.json()
    assert isinstance(coverPhotos, list)
    assert len(coverPhotos) > 0

def test_get_coverPhotos_by_id():
    response = requests.get(f"{BASE_URL}/CoverPhotos/1")
    assert response.status_code == 200
    coverPhotos = response.json()
    assert coverPhotos["id"] == 1
    assert "idBook" in coverPhotos
    assert "url" in coverPhotos

def test_get_coverPhotos_by_bookid():
    response = requests.get(f"{BASE_URL}/CoverPhotos/books/covers/1")
    assert response.status_code == 200
    coverPhotos = response.json()
    assert isinstance(coverPhotos, list)
    assert len(coverPhotos) > 0
    for coverPhotos in coverPhotos:
        assert coverPhotos["idBook"] == 1
        assert "id" in coverPhotos
        assert "url" in coverPhotos

@pytest.mark.parametrize("coverPhotos_id", [1, 2, 3, 10])
def test_get_coverPhotos(coverPhotos_id):
    response = requests.get(f"{BASE_URL}/CoverPhotos/{coverPhotos_id}")
    assert response.status_code == 200
    assert response.json()["id"] == coverPhotos_id

def test_get_invalid_coverPhotos():
    response = requests.get(f"{BASE_URL}/CoverPhotos/999999")
    assert response.status_code == 404


# =============================
# POST
# =============================

def test_create_coverPhotos():
    # arrange
    payload = {
        "id": 100,
        "idBook": 2,
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/960px-Red_Apple.jpg",
    }
    #act
    response = requests.post(
        f"{BASE_URL}/CoverPhotos", 
        json=payload
    )
    #assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["idBook"] == payload["idBook"]
    assert response_data["url"] == payload["url"]
    

# =============================
# PUT
# =============================

def test_update_coverPhotos():
    # arrange
    coverPhoto_id = 1
    payload = {
        "id": 100,
        "idBook": 2,
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/960px-Red_Apple.jpg",
    }
    #act
    response = requests.put(
        f"{BASE_URL}/CoverPhotos/{coverPhoto_id}", 
        json=payload
    )
    #assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["idBook"] == payload["idBook"]
    assert response_data["url"] == payload["url"]

def test_update_wrong_id_format():
    coverPhoto_id = "abc" #wrong format
    payload = {
        "id": coverPhoto_id,
        "idBook": 2,
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/960px-Red_Apple.jpg",
    }
    response = requests.put(
        f"{BASE_URL}/CoverPhotos/{coverPhoto_id}",
        json=payload
    )
    print(response.status_code)
    print(response.json())
    assert response.status_code == 400


# =============================
# DELETE
# =============================

def test_delete_coverPhotos():
    coverPhoto_id = 1
    response = requests.delete(f"{BASE_URL}/CoverPhotos/{coverPhoto_id}")
    assert response.status_code == 200    

@pytest.mark.xfail(reason="FakeRestAPI does not validate resource existence")
def test_delete_non_existing_coverPhotos():
    coverPhoto_id = 999999
    response = requests.delete(f"{BASE_URL}/CoverPhotos/{coverPhoto_id}")
    assert response.status_code == 404