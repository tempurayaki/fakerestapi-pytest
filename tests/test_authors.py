import requests
import pytest

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"


# =============================
# GET
# =============================

def test_get_all_authors():
    response = requests.get(f"{BASE_URL}/Authors")
    assert response.status_code == 200
    authors = response.json()
    assert isinstance(authors, list)
    assert len(authors) > 0

def test_get_author_by_id():
    response = requests.get(f"{BASE_URL}/Authors/1")
    assert response.status_code == 200
    author = response.json()
    assert author["id"] == 1
    assert "idBook" in author
    assert "firstName" in author
    assert "lastName" in author

def test_get_author_by_bookid():
    response = requests.get(f"{BASE_URL}/Authors/authors/books/1")
    assert response.status_code == 200
    authors = response.json()
    assert isinstance(authors, list)
    assert len(authors) > 0
    for author in authors:
        assert author["idBook"] == 1
        assert "firstName" in author
        assert "lastName" in author
     

@pytest.mark.parametrize("author_id", [1, 2, 3, 10, 50])
def test_get_authors(author_id):
    response = requests.get(f"{BASE_URL}/Authors/{author_id}")
    assert response.status_code == 200
    assert response.json()["id"] == author_id

def test_get_invalid_author():
    response = requests.get(f"{BASE_URL}/Authors/999999")
    assert response.status_code == 404


# =============================
# POST
# =============================

def test_create_author():
    # arrange
    payload = {
        "id": 201,
        "idBook": 10,
        "firstName": "Jane",
        "lastName": "Doe",
    }
    #act
    response = requests.post(
        f"{BASE_URL}/Authors", 
        json=payload
    )
    #assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["idBook"] == payload["idBook"]
    assert response_data["firstName"] == payload["firstName"]
    assert response_data["lastName"] == payload["lastName"]
    

# =============================
# PUT
# =============================

def test_update_author():
    # arrange
    author_id = 1
    payload = {
        "id": author_id,
        "idBook": 1,
        "firstName": "Updated Name",
        "lastName": "Updated Name"
    }
    #act
    response = requests.put(
        f"{BASE_URL}/Authors/{author_id}", 
        json=payload
    )
    #assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["idBook"] == payload["idBook"]
    assert response_data["firstName"] == payload["firstName"]
    assert response_data["lastName"] == payload["lastName"]
    
def test_update_wrong_book_id_format():
    author_id = 1
    payload = {
        "id": author_id,
        "idBook": "abc",
        "firstName": "Updated Name",
        "lastName": "Updated Name"
    }
    response = requests.put(
        f"{BASE_URL}/Authors/{author_id}",
        json=payload
    )
    print(response.status_code)
    print(response.json())
    assert response.status_code == 400


# =============================
# DELETE
# =============================

def test_delete_author():
    author_id = 1
    response = requests.delete(f"{BASE_URL}/Authors/{author_id}")
    assert response.status_code == 200    

@pytest.mark.xfail(reason="FakeRestAPI does not validate resource existence")
def test_delete_non_existing_author():
    author_id = 999999
    response = requests.delete(f"{BASE_URL}/Authors/{author_id}")
    assert response.status_code == 404