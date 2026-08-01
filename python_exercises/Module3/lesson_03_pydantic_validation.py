"""
Lesson 3.3 - Pydantic request/response validation

Run with:
    uvicorn lesson_03_pydantic_validation:app --reload
(from inside python_exercises/Module3/)

Try these at http://127.0.0.1:8000/docs and confirm each is rejected with 422:
    - POST /books with price = -5
    - POST /books with isbn = "abc" (letters, not digits)
    - POST /books with title = "   " (whitespace only)
And confirm a successful POST /books response body does NOT include cost_price,
even though it's a required field you must send in the request.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

books_db: dict[str, dict] = {}


# ------------------------------------------------------------------
# TODO: BookCreate -- the INPUT model for creating a book.
# Fields:
#   isbn: str        -- Field(min_length=3, max_length=13, pattern=r"^[0-9]+$")
#   title: str        -- Field(min_length=1)
#   author: str       -- Field(min_length=1)
#   price: float      -- Field(gt=0)         (what a member pays / late fee is based on)
#   cost_price: float -- Field(gt=0)         (what the LIBRARY paid -- internal only)
#
# Also add a @field_validator("title") that rejects a title that is only
# whitespace (v.strip() == "") even though it passed min_length=1
# (e.g. a single space "  " has length > 0 but is still garbage).

class BookCreate(BaseModel):
    isbn: str = Field(min_length=3, max_length=13, pattern=r"^[0-9]+$")
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    price: float = Field(gt=0)         
    cost_price: float = Field(gt=0)
    
    @field_validator("title")
    @classmethod
    def name_not_blank(cls, v):
        if not v.strip():
            raise ValueError("name cannot be blank")
        return v

# ------------------------------------------------------------------


# ------------------------------------------------------------------
# TODO: BookPublic -- the OUTPUT model, used as response_model.
# Fields: isbn, title, author, price, is_checked_out
# Deliberately does NOT include cost_price.
# ------------------------------------------------------------------
class BookPublic(BaseModel):
    isbn: str 
    title: str 
    author: str
    price: float
    is_checked_out: bool
# ------------------------------------------------------------------
# WORKED EXAMPLE
# ------------------------------------------------------------------

@app.get("/books/{isbn}")
def get_book(isbn: str):
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[isbn]


# ------------------------------------------------------------------
# TODO: GET /books, response_model=list[BookPublic]
# - return list(books_db.values())
# ------------------------------------------------------------------
@app.get("/books", response_model=list[BookPublic], status_code=200)
def get_books():
    return books_db.values()
    

# ------------------------------------------------------------------
# TODO: POST /books, response_model=BookPublic, status_code=201
# - takes `book: BookCreate`
# - 400 if book.isbn already in books_db
# - otherwise store book.model_dump() (this includes cost_price) in books_db,
#   also set is_checked_out=False on the stored dict, then return it
#   (response_model will strip cost_price from what's actually sent back)
# ------------------------------------------------------------------
@app.post("/books", response_model=BookPublic, status_code=201)
def add_book(book: BookCreate):
    if book.isbn in books_db.keys():
        raise HTTPException(status_code=400, detail="Book already exists")
    books_db[book.isbn] = book.model_dump()
    books_db[book.isbn]["is_checked_out"] = False
    return books_db[book.isbn]


    