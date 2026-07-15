def validate_book_id(book_id):
    """
    Validate Book ID.
    """
    if book_id <= 0:
        raise ValueError("Book ID must be greater than 0.")


def validate_title(title):
    """
    Validate Book Title.
    """
    if not title.strip():
        raise ValueError("Title cannot be empty.")


def validate_author(author):
    """
    Validate Author Name.
    """
    if not author.strip():
        raise ValueError("Author name cannot be empty.")


def validate_category(category):
    """
    Validate Category.
    """
    if not category.strip():
        raise ValueError("Category cannot be empty.")


def validate_quantity(quantity):
    """
    Validate Quantity.
    """
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
if __name__ == "__main__":
    
    try:
        validate_book_id(101)
        validate_title("Python")
        validate_author("Guido")
        validate_category("Programming")
        validate_quantity(10)

        print("✅ All validations passed!")

    except ValueError as err:
        print(err)