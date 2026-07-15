import mysql.connector
from config.db_config import HOST, USER, PASSWORD, DATABASE


def get_connection():
    """
    Creates and returns a MySQL database connection.
    """

    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        return connection

    except mysql.connector.Error as err:
        print(f"\n❌ Database Connection Error: {err}")
        return None


if __name__ == "__main__":

    connection = get_connection()

    if connection:
        print("✅ Connected Successfully!")
        connection.close()
        print("Connection Closed.")