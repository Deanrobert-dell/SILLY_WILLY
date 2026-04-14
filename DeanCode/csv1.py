import csv
from datetime import datetime
from ElijahCode.expense_management import *

def excsv():
    #add headers
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
    #expenses
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
   #filters with user
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
        print("not found")
    except Exception as e:
        print(f"Error reading expenses.csv: {e}")
    
    return expenses

def import1():
    #add expenses from user input
    print("\n=== Add New Expense ===")
    user_id = input("Enter user ID: ")
    category = input("Enter category (food, entertainment, gas, rent, etc.): ")
    
    while True:
        try:
            amount = float(input("Enter amount (without $): ")) #simply tbh
            if amount < 0:
                print("no nega tibve")
                continue
            break
        except ValueError:
            print("number freakbob")
    
    date_input = input("use yyyy mmmdd ")
    if not date_input:
        date_input = datetime.now().strftime('%Y-%m-%d')
    
    add_expense(user_id, category, amount, date_input)

if __name__ == "__main__": #basically runsfile direct omly

    excsv()