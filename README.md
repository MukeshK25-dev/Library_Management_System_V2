# 📚 Library Management System (Version 2)

A professional command-line **Library Management System** built using **Python**, **MySQL**, and **Object-Oriented Programming (OOP)** with a layered architecture. This version improves upon Version 1 by introducing modular design, reusable services, validation, and a cleaner project structure.

---

## 🚀 Features

* Add a new book
* View all books
* Search books by Book ID
* Update book quantity
* Delete books
* Menu-driven interface
* Input validation
* Duplicate Book ID detection
* MySQL database integration
* Object-Oriented Programming (OOP)
* Layered project architecture

---

## 🛠️ Technologies Used

* Python 3
* MySQL 8
* mysql-connector-python

---

## 📂 Project Structure

```text
Library_Management_System_V2/
│
├── config/
│   └── db_config.py
│
├── database/
│   ├── connection.py
│   ├── create_database.py
│   └── create_tables.py
│
├── models/
│   └── book.py
│
├── services/
│   └── book_service.py
│
├── utils/
│   └── validator.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🏗️ Project Architecture

```text
User
   │
   ▼
main.py
   │
   ▼
BookService
   │
   ├────────► Validator
   │
   ▼
Book Model
   │
   ▼
Database Connection
   │
   ▼
MySQL Database
```

---

## ⚙️ Installation

### 1. Clone the repository

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL

Update the database credentials inside:

```text
config/db_config.py
```

### 4. Create the database

```bash
python -m database.create_database
```

### 5. Create the tables

```bash
python -m database.create_tables
```

### 6. Run the application

```bash
python main.py
```

---

## 💡 Concepts Demonstrated

* Object-Oriented Programming (OOP)
* Layered Architecture
* CRUD Operations
* MySQL Database Connectivity
* Input Validation
* Exception Handling
* Modular Programming
* Reusable Service Layer

---

## 🧪 Testing

`test.py` and `test_update.py` are manual scripts used during development to exercise `BookService` methods directly (add/view/search/update/delete) against a live database connection. They are **not** an automated test suite — there are no assertions and they are not run via `pytest`. Automated tests with `pytest` are a planned improvement.

---

## 📝 Notes

A couple of small housekeeping items are known and left as-is in this documentation pass:

* `services/book_services.py` is an early, unused stub from refactoring — the application entry point (`main.py`) uses `services/book_service.py`.
* `database/create_databse.py` is a duplicate of `create_database.py` (naming typo from an earlier commit).

Both are safe to remove in a future cleanup pass.

---

## 🔮 Future Improvements

* Automated tests with `pytest`
* User Authentication
* Book Issue & Return Module
* Student Management
* Fine Calculation
* Dashboard
* Logging
* REST API
* Flask Web Version
* GUI Version

---

## 👨‍💻 Author

Mukesh K

B.Tech Information Technology

Python & MySQL Learning Project
