# NH, BH, EH, DP 2nd Financial Calculator
# Imports for team modules and CSV handling
from DeanCode.pichart import *
from DeanCode.deanline_graph import *
from DeanCode.csv1 import *
from NateCode.nate import *
from BriggsCode.briggs import *
from ElijahCode.currency_conversion import *
from ElijahCode.expense_management import *
import csv
	#   Make the main menu function
def main_menu(self):
    while True:
        print("__________________")
        print("|   MAIN MENU    |")
        print("------------------")
    # welcome user
    #print  each option ex:income budgeting, data visualizer
    # display the options           
    #user input asking which option
    #if statements corresponding to user input, call other functions
        choice = input("Would you like to \n1. Track Savings Goal\n2. Check Budget Limit\n3. Add Budget Limit\n4. Currency Conversion\nE. Exit")
        if choice == "1":
            track_savings_goal()
        elif choice == "2":
            check_budget_limit(categories)
        elif choice == "3":
            add_budget_limit(categories)
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            print("That is not an option. Please try again")
