from database.connection import get_connection
from utils.validator import (
    validate_book_id,
    validate_title,
    validate_author,
    validate_category,
    validate_quantity,
)
from models.book import Book


class BookService:
    """
    Handles all book-related database operations.
    """

    def __init__(self):
        self.connection = get_connection()

    def close_connection(self):
        if self.connection:
            self.connection.close()