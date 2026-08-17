"""Authentication module - member login and role checks."""

USERS = {
    "admin": "librarian",
    "student01": "member",
}


def login(username):
    """Return the user's role, or None if the user is unknown."""
    return USERS.get(username)


def is_librarian(username):
    return login(username) == "librarian"
