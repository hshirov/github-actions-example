from fastapi.testclient import TestClient
from .main import app
from .db import books

client = TestClient(app)


def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == books[:10]


def test_get_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == books[0]


def test_get_book_not_found():
    response = client.get("/books/999999")
    assert response.status_code == 404
