# NH, BH, EH, DP 2nd Financial Calculator
# Imports for team modules and CSV handling
from DeanCode.pichart import *
from DeanCode.csv1 import *
from DeanCode import *
from Nate import *
from BriggsCode.briggs import *
from ElijahCode.expense_management import income
from Nate import *
import csv
	#   Make the main menu function

user_id = "abc123"
categories = ["food", "entertainment", "gas", "rent"]
expenses = [
    {"user": "abc123", "category": "food", "amount": 15.50, "date": "2026-03-01"},
    {"user": "abc123", "category": "entertainment", "amount": 40.00, "date": "2026-03-06"},
    {"user": "def456", "category": "food", "amount": 20.00, "date": "2026-03-01"},
    {"user": "def456", "category": "entertainment", "amount": 50.00, "date": "2026-03-02"},
    {"user": "abc123", "category": "gas", "amount": 30.00, "date": "2026-04-03"},
    {"user": "abc123", "category": "rent", "amount": 1200.00, "date": "2026-04-04"},
    {"user": "def456", "category": "gas", "amount": 25.00, "date": "2026-04-03"}
]
def main_menu():
    while True:
        print("__________________")
        print("|   MAIN MENU    |")
        print("------------------")
main_menu()
    # welcome user
print("Welcome user!")
while True:
    #print  each option ex:income budgeting, data visualizer
    # display the options           
    #user input asking which option
    #if statements corresponding to user input, call other functions
        choice = input("What would you like to do? \n1. Create Savings Goal\n2. Check Budget Limit\n3. Add Budget Limit\n4. Expense Management\nE. Exit\n").strip()
        if choice == "1":
            create_savings_goal(user_id)
        elif choice == "2":
            check_budget_limit(user_id,categories, expenses)
        elif choice == "3":
            add_budget_limit(user_id, categories)
        elif choice == "4":
            income()
        elif choice == "E":
            break
        else:
            print("That is not an option. Please try again.")