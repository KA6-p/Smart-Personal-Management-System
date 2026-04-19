# 🛠️ Smart Personal Management System

> A modular, console-based personal productivity app built with Python — featuring user authentication, a diary, contact book, expense tracker, to-do list, and utility tools all in one place.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Modules](#modules)
- [Data Storage](#data-storage)
- [Technologies Used](#technologies-used)
- [Author](#author)
- [License](#license)

---

## 🔍 Overview

The **Smart Personal Management System** is a fully functional Python console application that serves as an all-in-one personal organizer. It supports multi-user authentication and gives each user access to a suite of productivity tools — from journaling and contact management to expense tracking and a password generator.

This was built as a first end-to-end Python project, demonstrating modular design, file-based persistence, and clean menu-driven navigation.

---

## ✨ Features

| Module | Capabilities |
|--------|--------------|
| 🔐 **User Auth** | Register & login with SHA-256 hashed passwords |
| 📒 **Diary** | Add, view, and clear timestamped notes |
| 📇 **Contact Book** | Add, view, update, and delete contacts (stored as JSON) |
| 💰 **Expense Tracker** | Log expenses, view records, generate reports, calculate totals |
| ✅ **To-Do List** | Add tasks, view list, mark tasks as done, clear completed |
| 🛠️ **Utility Tools** | Calculator, unit converter, random password generator |

---

## 📁 Project Structure

```
Smart-Personal-Management-System/
│
├── main.py                 # Entry point — main menu & navigation logic
├── user_auth.py            # User registration & login with password hashing
├── diary_module.py         # Diary: add, read, and clear notes
├── contact_book.py         # Contact management (CRUD operations)
├── expense_tracker.py      # Expense logging, reporting & totals
├── todo_list.py            # To-do list management
├── utility_tools.py        # Calculator, unit converter, password generator
│
├── users.txt               # Stores registered user credentials
├── diary.txt               # Persistent diary entries
├── contacts.json           # Contacts stored in JSON format
├── expenses.json           # Expense records stored in JSON format
├── todo.txt                # To-do tasks file
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- No external libraries required — uses the Python standard library only

### Installation

```bash
# Clone the repository
git clone https://github.com/KA6-p/Smart-Personal-Management-System.git

# Navigate into the project folder
cd Smart-Personal-Management-System

# Run the application
python main.py
```

---

## 🖥️ Usage

On launch, you'll be greeted with the welcome screen:

```
=== Welcome to Your Personal Management System! ===
1 - Register account
2 - Login to your account
3 - Exit
```

After logging in, the **Main Menu** gives you access to all modules:

```
--- Main Menu ---
1 - Diary Module
2 - Contact Book
3 - Expense Tracker
4 - To-do List
5 - Utility Tools
6 - Logout
```

Each module has its own sub-menu with numbered options for easy navigation.

---

## 🧩 Modules

### 🔐 User Authentication (`user_auth.py`)
- Register new accounts with a username and password
- Passwords are hashed using **SHA-256** before storage
- Credentials are saved to `users.txt`
- Login validates the hashed input against the stored hash

### 📒 Diary (`diary_module.py`)
- Add timestamped journal entries
- View all past notes
- Clear/delete all diary entries
- Entries are stored persistently in `diary.txt`

### 📇 Contact Book (`contact_book.py`)
- Add contacts with name, phone, email, and address
- Look up a contact by name
- Update specific fields (leave blank to keep existing value)
- Delete contacts
- Data persisted in `contacts.json`

### 💰 Expense Tracker (`expense_tracker.py`)
- Log expenses with amount, category, and description
- View all recorded expenses
- Generate a categorized expense report
- Calculate total spending
- Data persisted in `expenses.json`

### ✅ To-Do List (`todo_list.py`)
- Add new tasks
- View all tasks with their completion status
- Mark tasks as done ✔
- Clear all tasks
- Tasks stored in `todo.txt`

### 🛠️ Utility Tools (`utility_tools.py`)
- **Calculator** — perform basic arithmetic operations
- **Unit Converter** — convert between common measurement units
- **Random Password Generator** — generate strong, random passwords

---

## 💾 Data Storage

All data is stored locally using plain text and JSON files — no database required.

| File | Contents |
|------|----------|
| `users.txt` | Usernames and SHA-256 hashed passwords |
| `diary.txt` | Timestamped diary entries |
| `contacts.json` | Contact records (name, phone, email, address) |
| `expenses.json` | Expense entries with amount, category, and description |
| `todo.txt` | Tasks with completion status |

---

## 🛠️ Technologies Used

- **Python 3** — core language
- `hashlib` — SHA-256 password hashing
- `json` — structured data storage for contacts and expenses
- `os` / `datetime` — file handling and timestamps
- `random` / `string` — secure password generation

---

## 👤 Author

**KA6-p** — [GitHub Profile](https://github.com/KA6-p)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
