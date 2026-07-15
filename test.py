from services.book_service import BookService
from models.book import Book

service = BookService()

# ---------------- ADD ----------------
# service.add_book(
#     Book(
#         105,
#         "Operating System",
#         "Galvin",
#         "OS",
#         10
#     )
# )

# ---------------- VIEW ----------------
# service.view_books()

# ---------------- SEARCH ----------------
# service.search_book(101)

# ---------------- UPDATE ----------------
# service.update_book(101, 25)

# ---------------- DELETE ----------------
service.delete_book(999)

service.close_connection()