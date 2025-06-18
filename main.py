from user_auth import register, login
from diary_module import read_notes, add_notes, clear_notes
from contact_book import add_contact, view_contact, update_contact, delete_contact
from todo_list import add_tasks, view_tasks, done_tasks, clear_tasks
from expense_tracker import add_expenses, view_expenses, generate_report, total_expenses
from utility_tools import calculator, unit_convertor, random_password_generator

# Login/Register loop
while True:
    print("Welcome to Your Personal Management System!")
    print("1 - Register account\n2 - Login to your account")
    choice = input("Choose one: ")

    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(username, password):
            break
        else:
            print("Login failed. Try again.\n")
    else:
        print("Invalid choice.\n")

# Main feature menu
while True:
    print("\nChoose the field you want to explore!")
    print("1 - Diary Module\n2 - Contact Book\n3 - Expense Tracker\n4 - To-do List\n5 - Utility Tools\n6 - Exit Program")
    n = input("Enter your choice: ").strip()

    if n == "1":
        print("1 - Add notes\n2 - View notes\n3 - Delete notes") 
        option = input("Enter your choice: ").strip()
        if option == "1":
            add_notes()
        elif option == "2":
            read_notes()
        elif option == "3":
            clear_notes()
        else:
            print("Invalid Choice")
            continue

    elif n == "2":
        print("1 - Add contact\n2 - View contacts\n3 - Edit contacts\n4 - Delete contact")     
        select = input("Enter your choice: ").strip()
        if select == "1":
            name = input("Enter name of contact: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif select == "2":
            name = input("Enter name of contact: ")
            view_contact(name)
        elif select == "3":
            name = input("Enter name of contact: ")
            print("Enter field or leave blank if you don't want to update it.")
            phone = input("Enter phone: ") or None
            email = input("Enter email: ") or None
            address = input("Enter address: ") or None
            update_contact(name, phone, email, address)
        elif select == "4":
            name = input("Enter name of contact: ")
            delete_contact(name)
        else:
            print("Invalid Choice")
            continue

    elif n == "3":
        print("1 - Add expenses\n2 - View Expenses\n3 - Generate Report\n4 - Total Expenses")
        expense_choice = input("Enter your choice: ").strip()
        if expense_choice == "1":
            add_expenses()
        elif expense_choice == "2":
            view_expenses()
        elif expense_choice == "3":
            generate_report()
        elif expense_choice == "4":
            total_expenses()
        else:
            print("Invalid Choice!")
            continue

    elif n == "4":
        print("1 - Add tasks\n2 - View To-do list\n3 - Mark tasks complete\n4 - Delete tasks")
        todo_choice = input("Enter your choice: ").strip()
        if todo_choice == "1":
            add_tasks()
        elif todo_choice == "2":
            view_tasks()
        elif todo_choice == "3":
            done_tasks()
        elif todo_choice == "4":
            clear_tasks()
        else:
            print("Invalid Choice....")
            continue

    elif n == "5":
        print("1 - Calculator\n2 - Unit Convertor\n3 - Random Password Generator")
        utility_choice = input("Enter your choice: ").strip()
        if utility_choice == "1":
            calculator()
        elif utility_choice == "2":
            unit_convertor()
        elif utility_choice == "3":
            random_password_generator()
        else:
            print("Invalid Choice...")
            continue

    elif n == "6":
        print("Exiting the program...")
        break

    else:
        print("Invalid Choice!")
        continue
