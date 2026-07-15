from database.connection import get_connection


def create_tables():
    """
    Creates all required tables for the Library Management System.
    """

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    create_books_table = """
    CREATE TABLE IF NOT EXISTS books(
        book_id INT PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        author VARCHAR(100) NOT NULL,
        category VARCHAR(50) NOT NULL,
        quantity INT NOT NULL
    )
    """

    cursor.execute(create_books_table)

    connection.commit()

    print("✅ Books table is ready.")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    create_tables()