import json
import os
from datetime import datetime

File_path = 'expenses.json'

def load_expenses():
    if not os.path.exists(File_path):
        return []
    with open(File_path,'r') as f:
        return json.load(f)
    
def save_expenses(expenses):
    with open(File_path,'w') as f:
        json.dump(expenses,f,indent =4)

def add_expenses():
    date = input("Enter date (YYYY-MM-DD): ")
    category= input("Enter category: ")
    description = input("Enter a description: ")
    amount = float(input("Enter the amount: Rs"))
    expenses = load_expenses()
    expenses.append({
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    })
    save_expenses(expenses)
    print(f"Expenses of Rs{amount} for {description} aded successfully.")

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





