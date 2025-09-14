import json
import os
from datetime import datetime

EXPENSES_FILE = 'expenses.json'

def get_valid_date():
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid Date Format. Please use YYYY-MM-DD")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter the amount: Rs"))
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0")
        except ValueError:
            print("Please enter a valid number")

def load_expenses():
    try:
        if not os.path.exists(EXPENSES_FILE):
            return []
        with open(EXPENSES_FILE,'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error reading expenses file. Starting fresh.")
        return []
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return []
    
    
def save_expenses(expenses):
    with open(EXPENSES_FILE,'w') as f:
        json.dump(expenses,f,indent =4)

def add_expenses():
    date = get_valid_date()
    category= input("Enter category: ")
    description = input("Enter a description: ")
    amount = get_valid_amount()
    expenses = load_expenses()
    expenses.append({
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    })
    save_expenses(expenses)
    print(f"Expenses of Rs{amount} for {description} added successfully.")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nDate | Category | Description | Amount")
    print("------------------------------------------")
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | {exp['description']} | Rs{exp['amount']}")

def generate_report():
    search_date = input("Enter the date to search for (YYYY-MM-DD): ")
    expenses = load_expenses()
    found = False
    print("\nDate | Category | Description | Amount")
    print("------------------------------------------")
    for exp in expenses:
        if exp['date'] == search_date:
            print(f"{exp['date']} | {exp['category']} | {exp['description']} | Rs{exp['amount']}")
            found = True
    if not found:
        print("No expenses found for that date")

def total_expenses():
     expenses = load_expenses()
     total = sum(exp['amount'] for exp in expenses)
     print(f"\nTotal expenses: Rs{total}")





