class ContactExistsError(Exception):
    """Raised when contact already exists."""
    pass


class ValidationError(Exception):
    """Raised when phone format is invalid."""
    pass


class NotFoundError(Exception):
    """Raised when the value is not found."""
    pass