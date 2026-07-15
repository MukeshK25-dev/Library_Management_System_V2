from services.book_service import BookService

service = BookService()

service.update_book(101, 20)

service.close_connection()