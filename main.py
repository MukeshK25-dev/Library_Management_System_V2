from services.book_service import BookService
from models.book import Book


def menu():
    print("\n" + "=" * 45)
    print("      LIBRARY MANAGEMENT SYSTEM V2")
    print("=" * 45)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book Quantity")
    print("5. Delete Book")
    print("6. Exit")


def main():

    service = BookService()

    while True:

        menu()

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":

            try:
                book = Book(
                    int(input("Book ID: ")),
                    input("Title: "),
                    input("Author: "),
                    input("Category: "),
                    int(input("Quantity: "))
                )

                service.add_book(book)

            except ValueError:
                print("❌ Invalid input.")

        elif choice == "2":

            service.view_books()

        elif choice == "3":

            try:
                book_id = int(input("Enter Book ID: "))
                service.search_book(book_id)

            except ValueError:
                print("❌ Invalid Book ID.")

        elif choice == "4":

            try:
                book_id = int(input("Book ID: "))
                quantity = int(input("New Quantity: "))
                service.update_book(book_id, quantity)

            except ValueError:
                print("❌ Invalid input.")

        elif choice == "5":

            try:
                book_id = int(input("Book ID: "))
                service.delete_book(book_id)

            except ValueError:
                print("❌ Invalid Book ID.")

        elif choice == "6":

            service.close_connection()
            print("\nThank you for using Library Management System V2.")
            break

        else:

            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()