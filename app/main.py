from fastapi import FastAPI, HTTPException
from .db import books

app = FastAPI()


@app.get("/books")
async def get_books(offset: int = 0, limit: int = 10):
    return books[offset : offset + limit]


@app.get("/books/{id}")
async def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
