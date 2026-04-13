# NH, BH, EH, DP 2nd Financial Calculator
# Imports for team modules and CSV handling
from DeanCode import *
from BriggsCode.briggs import *
from ElijahCode.expense_management import income
import csv
	#   Make the main menu function

def main_menu():
    while True:
        print("__________________")
        print("|   MAIN MENU    |")
        print("------------------")
main_menu()
    # welcome user
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
main_menu()