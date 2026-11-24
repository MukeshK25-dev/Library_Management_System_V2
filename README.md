# 📚 Library Management System (Version 2)

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8-4479A1?logo=mysql&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-Layered-2EC4B6)
![License](https://img.shields.io/badge/License-MIT-green)

A command-line **Library Management System** built with **Python**, **MySQL** and **Object-Oriented Programming**, organized into layers. This version rebuilds [Version 1](https://github.com/MukeshK25-dev/Library_Management_System_V1) with modular design, a reusable service layer, input validation and a cleaner project structure.

> See it in 3D: the [portfolio site](https://mukeshk25-dev.github.io/Mukesh-Portfolio/) has an interactive model of these layers.

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
* Parameterized SQL queries
* MySQL database integration
* Object-Oriented Programming (OOP)
* Layered project architecture

---

## 🛠️ Technologies Used

* Python 3
* MySQL 8
* mysql-connector-python

---

## 🏗️ Project Architecture

Each layer has one job:

```mermaid
flowchart LR
    U([User]) --> M[main.py]
    M --> S["services<br/>BookService"]
    S --> V["utils<br/>validator.py"]
    S --> B["models<br/>Book"]
    S --> D["database<br/>connection.py"]
    C["config<br/>db_config.py"] -. reads .env .-> D
    D --> DB[(MySQL)]
```

| Layer | Files | Responsibility |
|---|---|---|
| `config/` | `db_config.py` | Reads database settings from environment variables |
| `database/` | `connection.py`, `create_database.py`, `create_tables.py` | Connects to MySQL and creates the database and table |
| `models/` | `book.py` | The `Book` class |
| `services/` | `book_service.py` | `BookService`: add, view, search, update quantity, delete |
| `utils/` | `validator.py` | Validates every input before it is saved |

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
├── .env.example
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/MukeshK25-dev/Library_Management_System_V2.git
cd Library_Management_System_V2
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL credentials

```bash
cp .env.example .env
```

Then edit `.env` and set `DB_PASSWORD` (and `DB_HOST` / `DB_USER` / `DB_DATABASE`
if your setup differs from the defaults). `config/db_config.py` reads these
values at import time, so you don't edit that file directly.

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
* Environment-based configuration (no hardcoded credentials)

---

## 🧪 Testing

`test.py` and `test_update.py` are manual scripts used during development to exercise `BookService` methods directly (add/view/search/update/delete) against a live database connection. They are **not** an automated test suite: there are no assertions and they are not run via `pytest`. Automated tests with `pytest` are a planned improvement.

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

## 📝 License
MIT. See [LICENSE](./LICENSE).

## 👨‍💻 Author

**Mukesh K**, B.Tech Information Technology · [Portfolio](https://mukeshk25-dev.github.io/Mukesh-Portfolio/) · [LinkedIn](https://www.linkedin.com/in/mukesh-kalyanasundaram-1480863b1/)
