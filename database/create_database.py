import mysql.connector
from config.db_config import HOST, USER, PASSWORD, DATABASE


def create_database():
    """
    Creates the library database if it doesn't already exist.
    """

    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD
        )

        cursor = connection.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

        print(f"✅ Database '{DATABASE}' is ready.")

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")


if __name__ == "__main__":
    create_database()