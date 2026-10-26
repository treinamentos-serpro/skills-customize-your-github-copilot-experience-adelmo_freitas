from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel
import pytest

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str
    publication_year: int


class Book(BookCreate):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    return list(books.values())


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    book = books.get(book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate) -> Book:
    global next_book_id

    book = Book(id=next_book_id, **book_data.model_dump())
    books[next_book_id] = book
    next_book_id += 1
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate) -> Book:
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    book = Book(id=book_id, **book_data.model_dump())
    books[book_id] = book
    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    del books[book_id]


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_books() -> None:
    global next_book_id

    books.clear()
    books[1] = Book(id=1, title="Kindred", author="Octavia E. Butler", publication_year=1979)
    next_book_id = 2


def test_list_books_returns_collection() -> None:
    response = client.get("/books")

    # TODO: Check the status code and the list of books in the JSON response.
    assert response.status_code == 200


def test_get_book_returns_requested_book() -> None:
    response = client.get("/books/1")

    # TODO: Check the returned book's ID, title, author, and publication year.
    assert response.status_code == 200


def test_get_missing_book_returns_404() -> None:
    response = client.get("/books/999")

    # TODO: Check the error response body.
    assert response.status_code == 404


def test_create_book_returns_created_book() -> None:
    response = client.post(
        "/books",
        json={"title": "Parable of the Sower", "author": "Octavia E. Butler", "publication_year": 1993},
    )

    # TODO: Check the created book's fields and generated ID.
    assert response.status_code == 201


def test_create_book_rejects_missing_author() -> None:
    response = client.post("/books", json={"title": "Parable of the Sower", "publication_year": 1993})

    # TODO: Check the validation error response.
    assert response.status_code == 422


def test_update_book_replaces_book_data() -> None:
    response = client.put(
        "/books/1",
        json={"title": "Parable of the Sower", "author": "Octavia E. Butler", "publication_year": 1993},
    )

    # TODO: Check the updated values in the response.
    assert response.status_code == 200


def test_update_missing_book_returns_404() -> None:
    response = client.put(
        "/books/999",
        json={"title": "Parable of the Sower", "author": "Octavia E. Butler", "publication_year": 1993},
    )

    assert response.status_code == 404


def test_delete_book_removes_book() -> None:
    response = client.delete("/books/1")

    assert response.status_code == 204
    assert client.get("/books/1").status_code == 404


def test_delete_missing_book_returns_404() -> None:
    response = client.delete("/books/999")

    assert response.status_code == 404