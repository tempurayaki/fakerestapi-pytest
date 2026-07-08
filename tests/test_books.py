import requests
import pytest

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"


# =============================
# GET
# =============================

def test_get_all_books():
    response = requests.get(f"{BASE_URL}/Books")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    assert len(books) > 0

def test_get_book_by_id():
    response = requests.get(f"{BASE_URL}/Books/1")
    assert response.status_code == 200
    book = response.json()
    assert book["id"] == 1
    assert "title" in book
    assert "description" in book
    assert "pageCount" in book

@pytest.mark.parametrize("book_id", [1, 2, 3, 10, 50])
def test_get_books(book_id):
    response = requests.get(f"{BASE_URL}/Books/{book_id}")
    assert response.status_code == 200
    assert response.json()["id"] == book_id

def test_get_invalid_book():
    response = requests.get(f"{BASE_URL}/Books/999999")
    assert response.status_code == 404


# =============================
# POST
# =============================

def test_create_book():
    # arrange
    payload = {
        "id": 201,
        "title": "Pytest Automation",
        "description": "Book created from pytest",
        "pageCount": 250,
        "excerpt": "Testing REST API",
        "publishDate": "2026-07-08T00:00:00Z"
    }
    #act
    response = requests.post(
        f"{BASE_URL}/Books", 
        json=payload
    )
    #assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["title"] == payload["title"]
    assert response_data["description"] == payload["description"]
    assert response_data["pageCount"] == payload["pageCount"]
    

# =============================
# PUT
# =============================

def test_update_book():
    # arrange
    book_id = 1
    payload = {
        "id": book_id,
        "title": "Updated Title",
        "description": "Updated description",
        "pageCount": 250,
        "excerpt": "Updated excerpt",
        "publishDate": "2026-07-08T00:00:00Z"
    }
    #act
    response = requests.put(
        f"{BASE_URL}/Books/{book_id}", 
        json=payload
    )
    #assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["title"] == payload["title"]
    assert response_data["description"] == payload["description"]
    assert response_data["pageCount"] == payload["pageCount"]
    assert response_data["excerpt"] == payload["excerpt"]
    assert response_data["publishDate"] == payload["publishDate"]
    
def test_update_wrong_date_format():
    book_id = 1
    payload = {
        "id": book_id,
        "title": "Updated",
        "description": "Updated",
        "pageCount": 100,
        "excerpt": "Updated",
        "publishDate": "08/07/2026" #wrong date format
    }
    response = requests.put(
        f"{BASE_URL}/Books/{book_id}",
        json=payload
    )
    print(response.status_code)
    print(response.json())
    assert response.status_code == 400


# =============================
# DELETE
# =============================

def test_delete_book():
    book_id = 1
    response = requests.delete(f"{BASE_URL}/Books/{book_id}")
    assert response.status_code == 200    

@pytest.mark.xfail(reason="FakeRestAPI does not validate resource existence")
def test_delete_non_existing_book():
    book_id = 999999
    response = requests.delete(f"{BASE_URL}/Books/{book_id}")
    assert response.status_code == 404