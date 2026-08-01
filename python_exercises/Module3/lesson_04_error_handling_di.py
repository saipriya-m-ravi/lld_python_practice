"""
Lesson 3.4 - Error handling & Dependency Injection (Depends)

Run with:
    uvicorn lesson_04_error_handling_di:app --reload
(from inside python_exercises/Module3/)

The point of this lesson: eliminate the repeated
    if isbn not in books_db: raise HTTPException(404, ...)
check that used to be copy-pasted into every endpoint in Lesson 3.2.
"""

from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()

books_db: dict[str, dict] = {}


class BookCreate(BaseModel):
    isbn: str = Field(min_length=3, max_length=13, pattern=r"^[0-9]+$")
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    price: float = Field(gt=0)


class BookUpdate(BaseModel):
    price: float = Field(gt=0)


# ------------------------------------------------------------------
# Domain exceptions -- plain Python, no HTTP concepts involved
# ------------------------------------------------------------------

class BookNotFoundError(Exception):
    pass


class BookAlreadyExistsError(Exception):
    pass


class BookAlreadyCheckedOutError(Exception):
    pass


# ------------------------------------------------------------------
# Global exception handlers -- the ONLY place that maps domain
# exceptions to HTTP status codes. Add one for each exception above.
# ------------------------------------------------------------------

@app.exception_handler(BookNotFoundError)
def handle_not_found(request: Request, exc: BookNotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})


# TODO: @app.exception_handler(BookAlreadyExistsError) -> 400
# TODO: @app.exception_handler(BookAlreadyCheckedOutError) -> 409
@app.exception_handler(BookAlreadyExistsError)
def handle_already_exists(request: Request, exc: BookAlreadyExistsError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})

@app.exception_handler(BookAlreadyCheckedOutError)
def handle_already_checkedout(request: Request, exc: BookAlreadyCheckedOutError):
    return JSONResponse(status_code=409, content={"detail": str(exc)})


# ------------------------------------------------------------------
# Dependency -- reusable "find this book or fail" logic
# ------------------------------------------------------------------

def get_book_or_404(isbn: str) -> dict:
    if isbn not in books_db:
        raise BookNotFoundError(f"Book '{isbn}' not found")
    return books_db[isbn]


# ------------------------------------------------------------------
# WORKED EXAMPLE -- notice: no manual 404 check anywhere in here
# ------------------------------------------------------------------

@app.get("/books/{isbn}")
def get_book(book: dict = Depends(get_book_or_404)):
    return book


# ------------------------------------------------------------------
# TODO: refactor these four using Depends(get_book_or_404), same shape
# as get_book above. None of them should contain a manual
# "if isbn not in books_db" check anymore.
# ------------------------------------------------------------------

@app.post("/books", status_code=201)
def add_book(book: BookCreate):
    if book.isbn in books_db:
        raise BookAlreadyExistsError(f"Book '{book.isbn}' already exists")
    books_db[book.isbn] = book.model_dump()
    books_db[book.isbn]["is_checked_out"] = False
    return books_db[book.isbn]


# TODO: PATCH /books/{isbn}
# - use Depends(get_book_or_404) to get `book: dict`
# - also take `update: BookUpdate`
# - update book["price"] = update.price and return book
# (since dicts are mutable and get_book_or_404 returns the SAME dict
#  object stored in books_db, mutating `book` here mutates the "database" too)
@app.patch("/books/{isbn}", status_code=200)
def update_book(update: BookUpdate, book: dict = Depends(get_book_or_404)):
    book["price"] = update.price
    return book
    

# TODO: DELETE /books/{isbn}, status_code=204
# - use Depends(get_book_or_404) to get `book: dict`
# - del books_db[book["isbn"]]
# - return None
@app.delete("/books/{isbn}", status_code=204)
def delete_book(book: dict = Depends(get_book_or_404)):
    del books_db[book["isbn"]]
    return None


# TODO: POST /books/{isbn}/checkout
# - use Depends(get_book_or_404) to get `book: dict`
# - if book["is_checked_out"]: raise BookAlreadyCheckedOutError(...)
# - else set book["is_checked_out"] = True, return book
@app.post("/books/{isbn}/checkout", status_code=201)
def checkout(book: dict = Depends(get_book_or_404)):
    if book["is_checked_out"]:
        raise BookAlreadyCheckedOutError(f"Book {book['isbn']} is already checked out")
    book["is_checked_out"] = True
    return book

# TODO: POST /books/{isbn}/return
# - use Depends(get_book_or_404) to get `book: dict`
# - set book["is_checked_out"] = False, return book
@app.post("/books/{isbn}/return", status_code=201)
def return_book(book: dict = Depends(get_book_or_404)):
    book["is_checked_out"] = False
    return book