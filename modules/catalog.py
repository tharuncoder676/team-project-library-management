"""Catalog module - book records and search."""

BOOKS = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "Hunt & Thomas"},
]


def search(keyword):
    """Return every book whose title contains the keyword."""
    keyword = keyword.lower()
    return [b for b in BOOKS if keyword in b["title"].lower()]


def get_book(book_id):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return None
