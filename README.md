# Smart Personal Management System

A modular, console-based personal productivity application written in Python. The system bundles five distinct tools — a diary, contact book, expense tracker, to-do list, and a set of utility functions — behind a single authenticated entry point. All data is persisted locally to plain text and JSON files with no external database dependency.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Module Reference](#module-reference)
- [Data Storage](#data-storage)
- [Security](#security)
- [Dependencies](#dependencies)
- [Author](#author)
- [License](#license)

---

## Overview

This project was built as a first end-to-end Python application with an emphasis on clean modular design. Each feature is implemented in its own file and imported into a central `main.py` that handles navigation and session management. The authentication layer ensures that personal data is protected behind a hashed password before any module is accessible.

---

## Features

- User registration and login with SHA-256 password hashing
- Timestamped diary with add, view, and clear operations
- Contact book with full CRUD support (create, read, update, delete)
- Expense tracker with per-category reporting and running totals
- To-do list with task completion tracking
- Built-in calculator, unit converter, and random password generator
- Graceful handling of `KeyboardInterrupt` and unexpected runtime errors

---

## Project Structure

```
Smart-Personal-Management-System/
│
├── main.py                 # Entry point; main menu and sub-menu routing
├── user_auth.py            # Registration, login, and password hashing
├── diary_module.py         # Diary: add, read, and clear timestamped entries
├── contact_book.py         # Contacts: add, view, update, delete (JSON-backed)
├── expense_tracker.py      # Expenses: log, view, categorize, total (JSON-backed)
├── todo_list.py            # Tasks: add, view, mark done, clear
├── utility_tools.py        # Calculator, unit converter, password generator
│
├── users.txt               # Stored usernames and hashed passwords
├── diary.txt               # Persistent diary entries
├── contacts.json           # Contact records
├── expenses.json           # Expense records
├── todo.txt                # Task list with completion status
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Getting Started

**Prerequisites:** Python 3.7 or higher. No third-party packages are required.

```bash
git clone https://github.com/KA6-p/Smart-Personal-Management-System.git
cd Smart-Personal-Management-System
python main.py
```

The data files (`users.txt`, `diary.txt`, `contacts.json`, `expenses.json`, `todo.txt`) are created automatically on first run if they do not already exist.

---

## Usage

On launch, the application presents an authentication screen:

```
=== Welcome to Your Personal Management System! ===
1 - Register account
2 - Login to your account
3 - Exit
```

After a successful login, the main menu provides access to all modules:

```
--- Main Menu ---
1 - Diary Module
2 - Contact Book
3 - Expense Tracker
4 - To-do List
5 - Utility Tools
6 - Logout
```

Each module opens a dedicated sub-menu. Input is read from the terminal and all output is printed to the console.

---

## Module Reference

### user_auth.py

Handles account creation and session validation. Passwords are never stored in plain text — only their SHA-256 digest is written to `users.txt`. Login recomputes the digest of the entered password and compares it against the stored value.

### diary_module.py

Writes journal entries to `diary.txt` with an automatic timestamp. Supports viewing the full entry history and wiping all entries with a confirmation step.

### contact_book.py

Stores contacts as JSON objects in `contacts.json`. Each record holds a name, phone number, email address, and physical address. The update function accepts partial input — fields left blank are preserved from the existing record.

### expense_tracker.py

Appends expense entries to `expenses.json` with fields for amount, category, and a short description. Includes a view-all function, a category-grouped report, and a total expenditure calculation.

### todo_list.py

Maintains a flat list of tasks in `todo.txt`. Each task carries a pending or completed status. Tasks can be marked done individually and the full list can be cleared in one operation.

### utility_tools.py

Three independent utilities accessible from a single sub-menu:

- **Calculator** — evaluates basic arithmetic expressions (add, subtract, multiply, divide)
- **Unit Converter** — converts between common measurement units (length, weight, temperature)
- **Password Generator** — produces a random alphanumeric password of a user-specified length using Python's `secrets` or `random` and `string` modules

---

## Data Storage

All persistence is file-based. No database engine is required.

| File | Format | Contents |
|------|--------|----------|
| `users.txt` | Plain text | Username and SHA-256 password hash, one pair per line |
| `diary.txt` | Plain text | Timestamped diary entries, appended sequentially |
| `contacts.json` | JSON | Array of contact objects |
| `expenses.json` | JSON | Array of expense objects with amount, category, and description |
| `todo.txt` | Plain text | Task entries with inline completion markers |

---

## Security

Passwords are hashed with SHA-256 via Python's built-in `hashlib` module before being written to disk. The plain-text password is never stored or logged. For a personal local application this provides a reasonable level of protection, though production systems would warrant salted hashing (e.g. `bcrypt` or `argon2`).

---

## Dependencies

This project uses only the Python standard library. No `pip install` step is needed.

| Module | Purpose |
|--------|---------|
| `hashlib` | SHA-256 password hashing |
| `json` | Reading and writing structured data files |
| `datetime` | Timestamping diary entries |
| `os` | File existence checks and path handling |
| `random`, `string` | Password generation |

---

## Author

**KA6-p** — [github.com/KA6-p](https://github.com/KA6-p)

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
