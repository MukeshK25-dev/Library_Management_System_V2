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

    # ----------------------------
    # Add Book
    # ----------------------------
    def add_book(self, book: Book):

        try:
            validate_book_id(book.book_id)
            validate_title(book.title)
            validate_author(book.author)
            validate_category(book.category)
            validate_quantity(book.quantity)

            cursor = self.connection.cursor()

            cursor.execute(
                "SELECT * FROM books WHERE book_id=%s",
                (book.book_id,)
            )

            if cursor.fetchone():
                print("❌ Book ID already exists.")
                cursor.close()
                return

            cursor.execute(
                """
                INSERT INTO books
                (book_id, title, author, category, quantity)
                VALUES (%s,%s,%s,%s,%s)
                """,
                (
                    book.book_id,
                    book.title,
                    book.author,
                    book.category,
                    book.quantity
                )
            )

            self.connection.commit()
            print("✅ Book added successfully.")

            cursor.close()

        except Exception as err:
            print(f"❌ {err}")

    # ----------------------------
    # View Books
    # ----------------------------
    def view_books(self):

        try:
            cursor = self.connection.cursor()

            cursor.execute("SELECT * FROM books")

            books = cursor.fetchall()

            if not books:
                print("\nNo books available.")
                cursor.close()
                return

            print("\n========== BOOK LIST ==========")

            for row in books:

                book = Book(*row)

                print("-----------------------------------")
                print(book)

            cursor.close()

        except Exception as err:
            print(f"❌ {err}")

    # ----------------------------
    # Search Book
    # ----------------------------
    def search_book(self, book_id):

        try:
            validate_book_id(book_id)

            cursor = self.connection.cursor()

            cursor.execute(
                "SELECT * FROM books WHERE book_id=%s",
                (book_id,)
            )

            row = cursor.fetchone()

            if row:

                book = Book(*row)

                print("\n📖 Book Found")
                print("-----------------------------------")
                print(book)

            else:
                print("❌ Book not found.")

            cursor.close()

        except Exception as err:
            print(f"❌ {err}")

    # ----------------------------
    # Update Book Quantity
    # ----------------------------
    def update_book(self, book_id, new_quantity):

        try:
            validate_book_id(book_id)
            validate_quantity(new_quantity)

            cursor = self.connection.cursor()

            cursor.execute(
                "SELECT * FROM books WHERE book_id=%s",
                (book_id,)
            )

            if not cursor.fetchone():
                print("❌ Book not found.")
                cursor.close()
                return

            cursor.execute(
                """
                UPDATE books
                SET quantity=%s
                WHERE book_id=%s
                """,
                (new_quantity, book_id)
            )

            self.connection.commit()

            print("✅ Book quantity updated successfully.")

            cursor.close()

        except Exception as err:
            print(f"❌ {err}")

    # ----------------------------
    # Delete Book
    # ----------------------------
    def delete_book(self, book_id):

        try:
            validate_book_id(book_id)

            cursor = self.connection.cursor()

            cursor.execute(
                "SELECT * FROM books WHERE book_id=%s",
                (book_id,)
            )

            row = cursor.fetchone()

            if not row:
                print("❌ Book not found.")
                cursor.close()
                return

            book = Book(*row)

            print("\nBook Found")
            print("-----------------------------------")
            print(book)

            cursor.execute(
                "DELETE FROM books WHERE book_id=%s",
                (book_id,)
            )

            self.connection.commit()

            print("\n✅ Book deleted successfully.")

            cursor.close()

        except Exception as err:
            print(f"❌ {err}")