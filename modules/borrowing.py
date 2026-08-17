"""Borrowing module - issue and return of books."""

LOAN_PERIOD_DAYS = 14

issued = {}


def issue(book_id, username):
    """Issue a book to a member. Returns False if already on loan."""
    if book_id in issued:
        return False
    issued[book_id] = username
    return True


def return_book(book_id):
    return issued.pop(book_id, None)


def is_available(book_id):
    return book_id not in issued
