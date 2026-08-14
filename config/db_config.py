import os
from dotenv import load_dotenv

load_dotenv()

# Database Configuration — loaded from environment, never hardcoded
HOST = os.getenv("DB_HOST", "localhost")
USER = os.getenv("DB_USER", "root")
PASSWORD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DB_DATABASE", "library_db")

if not PASSWORD:
    raise RuntimeError(
        "DB_PASSWORD is not set. Create a .env file with DB_PASSWORD=<your-password> "
        "(see .env.example)."
    )
