"""
Lesson 3.5 - Pagination (offset-based and cursor-based)

Run with:
    uvicorn lesson_05_pagination:app --reload
(from inside python_exercises/Module3/)

Try at http://127.0.0.1:8000/docs:
    GET /books?skip=0&limit=5    -> first 5 books, offset-based
    GET /books?skip=5&limit=5    -> next 5 books
    GET /books/cursor?limit=5              -> first page, cursor-based
    GET /books/cursor?limit=5&cursor=1005  -> next page after isbn "1005"
"""

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

books_db: dict[str, dict] = {}

# Seed 20 books upfront so pagination is actually visible.
# isbns are "1001".."1020" -- fixed-width digit strings, so plain string
# comparison ("1005" < "1006") sorts them correctly, same as numeric order.
for i in range(1, 21):
    isbn = f"10{i:02d}"
    books_db[isbn] = {
        "isbn": isbn,
        "title": f"Book {i}",
        "author": f"Author {i}",
        "price": 10.0 + i,
        "is_checked_out": False,
    }


class BookPublic(BaseModel):
    isbn: str
    title: str
    author: str
    price: float
    is_checked_out: bool


# ------------------------------------------------------------------
# WORKED EXAMPLE -- offset/limit pagination
# ------------------------------------------------------------------

class PaginatedBooksOffset(BaseModel):
    items: list[BookPublic]
    total: int
    skip: int
    limit: int


@app.get("/books", response_model=PaginatedBooksOffset)
def list_books(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0, le=100)):
    all_books = sorted(books_db.values(), key=lambda b: b["isbn"])
    page = all_books[skip: skip + limit]
    return PaginatedBooksOffset(items=page, total=len(all_books), skip=skip, limit=limit)


# ------------------------------------------------------------------
# TODO: cursor-based pagination
#
# 1. Define PaginatedBooksCursor(BaseModel):
#      items: list[BookPublic]
#      next_cursor: str | None
#      limit: int
class PaginatedBooksCursor(BaseModel):
    items: list[BookPublic]
    next_cursor: str | None
    limit: int
#
# 2. @app.get("/books/cursor", response_model=PaginatedBooksCursor)
#    def list_books_cursor(cursor: str | None = None, limit: int = Query(10, gt=0, le=100)):
#        - get all_books sorted by isbn (same as the worked example)
#        - if cursor is None: start from the beginning
#          else: only keep books with isbn > cursor
#          (hint: [b for b in all_books if cursor is None or b["isbn"] > cursor])
#        - take the first `limit` of those as `page`
#        - next_cursor = page[-1]["isbn"] if there are MORE books after this
#          page, else None (hint: compare len(page) and whether any books
#          remain beyond it)
#        - return PaginatedBooksCursor(items=page, next_cursor=next_cursor, limit=limit)
@app.get("/books/cursor", response_model=PaginatedBooksCursor)
def list_books_cursor(cursor: str | None = None, limit: int = Query(10, gt=0, le=100)):
    all_books = sorted(books_db.values(), key=lambda b: b["isbn"])
    result = [b for b in all_books if cursor is None or b["isbn"] > cursor]
    page = result[:limit]
    next_cursor = None if len(page)<limit else page[-1]["isbn"]
    return PaginatedBooksCursor(items=page, next_cursor=next_cursor, limit=limit)

# ------------------------------------------------------------------
