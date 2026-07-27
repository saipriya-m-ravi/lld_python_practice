"""
Lesson 3.2 - Building a CRUD API with FastAPI

Run this with:
    uvicorn lesson_02_fastapi_crud:app --reload
(run that command from inside python_exercises/Module3/)

Then open http://127.0.0.1:8000/docs to try every endpoint interactively.

Endpoints to build (per your Lesson 3.1 design):
    GET    /books                  -> list all books
    GET    /books/{isbn}           -> get one book
    POST   /books                  -> create a book            (201)
    PATCH  /books/{isbn}           -> update a book's price     (200)
    DELETE /books/{isbn}           -> delete a book             (204)
    POST   /books/{isbn}/checkout  -> checkout a book           (200 / 409 if already out)
    POST   /books/{isbn}/return    -> return a book             (200)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# in-memory "database" -- isbn -> book dict
books_db: dict[str, dict] = {}


class Book(BaseModel):
    isbn: str
    title: str
    author: str
    price: float
    is_checked_out: bool = False


class BookUpdate(BaseModel):
    price: float


# ------------------------------------------------------------------
# WORKED EXAMPLES -- study these before writing the rest yourself
# ------------------------------------------------------------------

@app.get("/books")
def list_books():
    return list(books_db.values())


@app.get("/books/{isbn}")
def get_book(isbn: str):
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[isbn]


# ------------------------------------------------------------------
# TODO: implement the rest
# ------------------------------------------------------------------

# TODO: POST /books, status_code=201
# - takes a `book: Book` request body
# - if book.isbn already exists in books_db, raise HTTPException(400, "Book already exists")
# - otherwise store it (books_db[book.isbn] = book.model_dump()) and return it

@app.post("/books", status_code=201)
def add_book(book: Book):
    if book.isbn in books_db:
        raise HTTPException(status_code=400, detail="Book already exists")
    books_db[book.isbn] = book.model_dump()
    return books_db[book.isbn]


# TODO: PATCH /books/{isbn}
# - takes `isbn: str` path param AND `update: BookUpdate` request body
# - 404 if isbn not found
# - otherwise update books_db[isbn]["price"] and return the updated book
@app.patch("/books/{isbn}")
def update_book(isbn: str, update: BookUpdate):
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[isbn]['price'] = update.price
    return books_db[isbn]


# TODO: DELETE /books/{isbn}, status_code=204
# - 404 if isbn not found
# - otherwise delete it from books_db
# - a 204 response should return None (no body)
@app.delete("/books/{isbn}", status_code=204)
def delete_book(isbn: str):
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    del books_db[isbn]
    return None
    

# TODO: POST /books/{isbn}/checkout
# - 404 if isbn not found
# - 409 (HTTPException(status_code=409, detail=...)) if already checked out
# - otherwise set is_checked_out = True and return the updated book

@app.post("/books/{isbn}/checkout")
def checkout(isbn: str):
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    if books_db[isbn]["is_checked_out"]:
        raise HTTPException(status_code=409, detail="Book already checked out")
    books_db[isbn]["is_checked_out"] = True
    return books_db[isbn]

# TODO: POST /books/{isbn}/return
# - 404 if isbn not found
# - otherwise set is_checked_out = False and return the updated book
@app.post("/books/{isbn}/return")
def return_book(isbn: str):
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[isbn]["is_checked_out"] = False
    return books_db[isbn]
