class Book:
    """
    Represents a book in the Library Management System.
    """

    def __init__(self, book_id, title, author, category, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.quantity = quantity

    def __str__(self):
        return (
            f"\nBook ID   : {self.book_id}\n"
            f"Title     : {self.title}\n"
            f"Author    : {self.author}\n"
            f"Category  : {self.category}\n"
            f"Quantity  : {self.quantity}"
        )


if __name__ == "__main__":

    book = Book(
        101,
        "Python Programming",
        "Guido van Rossum",
        "Programming",
        10
    )

    print(book)