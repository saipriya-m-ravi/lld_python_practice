# Lesson 3.1 - REST API Design for the Library System

Fill in the table below. For each row, decide: HTTP method, URL path, and which
status code(s) it should return (success case, and at least one failure case).

Think about:
- Which things are resources (nouns)? - Book, Member
- Which of these are plain CRUD vs. an "action" that needs a sub-resource-style endpoint? Checkput, Return are sub-resource style endpoint. Rest are plain CRUD.
- What's the right status code when the thing doesn't exist? When there's a conflict 
  (e.g. checking out an already-checked-out book)?  Not existing resource - 404, state conflict - 409

| # | Action | Method | Path | Success status | Failure status |
|---|---|---|---|---|---|
| 1 | List all books | get | /books | 200 | 400/500  |
| 2 | Get a single book by isbn | get | /books/123 | 200 | 400/500 |
| 3 | Add a new book | post | /books | 201 | 400/500 |
| 4 | Update a book's details (e.g. price) | patch | /books/123 | 200 | 400/404/500 |
| 5 | Delete a book | delete | /books/123 | 200/204 | 400/404/500 |
| 6 | Checkout a book | post | /books/123/checkout | 200/201 | 400/404/409/500 |
| 7 | Return a book | post | /books/123/return | 200/201 | 400/404/409/500 |
| 8 | List all members | get | /members | 200 | 400/500 |
| 9 | Get a single member by id | get | /members/123 | 200 | 400/500 |
| 10 | Register a new member | post | /members | 201 | 400/500 |
| 11 | Get the overdue report | get | /books/members?status=overdue | 200 | 400/500 |

## Follow-up questions (short answers)

1. For row 6 (checkout) -- why might `POST /books/{isbn}/checkout` be a better design
   than `PUT /books/{isbn}` with a body like `{"is_checked_out": true}`? checkput is not an update. Its an action on a resource. to map it to REST nun based model we keep it as a post methos.

2. For row 6 -- if the book is ALREADY checked out, which status code fits best:
   `400`, `404`, or `409`? Why? 409. Its a state conflict

3. For row 3 (add a new book) -- if the client sends a request missing a required
   field (e.g. no `title`), which status code should that be? 400 - malformed input
