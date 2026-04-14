import csv
from datetime import datetime
from ElijahCode.expense_management import *

def initialize_expenses_csv():
    """Create the expenses.csv file with headers if it doesn't exist."""
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            # Check if file has headers
            first_row = next(reader, None)
            if not first_row or first_row[0] != 'user':
                raise FileNotFoundError
    except FileNotFoundError:
        with open('expenses.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['user', 'category', 'amount', 'date'])

def add_expense(user_id, category, amount, date=None):
    """Add an expense entry to the CSV file."""
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')
    
    try:
        with open('expenses.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_id, category, amount, date])
        print(f"Expense added: {category} - ${amount} on {date}")
        return True
    except Exception as e:
        print(f"Error writing to expenses.csv: {e}")
        return False

def read_expenses(user_id=None):
    """Read all expenses from CSV, optionally filtered by user_id."""
    expenses = []
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row and row.get('user'):  # Skip empty rows
                    if user_id is None or row['user'] == user_id:
                        expenses.append({
                            'user': row['user'],
                            'category': row['category'],
                            'amount': float(row['amount']),
                            'date': row['date']
                        })
    except FileNotFoundError:
        print("expenses.csv not found. Please initialize it first.")
    except Exception as e:
        print(f"Error reading expenses.csv: {e}")
    
    return expenses

def import_expenses_from_input():
    """Interactive function to add expenses from user input."""
    print("\n=== Add New Expense ===")
    user_id = input("Enter user ID: ")
    category = input("Enter category (food, entertainment, gas, rent, etc.): ")
    
    while True:
        try:
            amount = float(input("Enter amount (without $): "))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date_input:
        date_input = datetime.now().strftime('%Y-%m-%d')
    
    add_expense(user_id, category, amount, date_input)

if __name__ == "__main__":
    initialize_expenses_csv()