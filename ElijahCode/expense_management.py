#EHCP2 expenses

from ElijahCode.currency_conversion import *  # Add folder prefix

import time as t

def income():
    while True:
        try:
            monthly_income = float(input("What is your total monthly income?\nDon't enter a dollar sign\n"))
            if monthly_income <= 0:
                print("Bro we all know you have an income")
                #i'll connect it to the main menu soonish
                return
            else:
                new_amount = currency_conversion(monthly_income)
                expenses(new_amount)
        except ValueError:
            print("That ain't a number")

def expenses(income):
    time_entered = t.ctime()
    while True:
        try:
            transportation = float(input("What is your monthly cost for transportation?\n"))
            food = float(input("What is your monthly cost for food?\n"))
            housing = float(input("What is the cost of your housing per month?\ne.g. property taxes or rent\n"))
            extra_stuff = float(input("What is the cost of your frivolous stuff?\n"))
            total_expense = transportation + food + housing + extra_stuff
            if total_expense > income:
                print(f"You have exceeded your monthly income (${income}) with these expenses")
                print("You must re_calculate your expenses")
                continue
            elif total_expense == income:
                print("You have exactly matched your income! Great calculation!")
                print(f"You entered this on {time_entered}")
            else:
                print("You still have some money left to spend!\nEither you got a big income, or a big brain!")
                print(f"You entered this on {time_entered}")
        except ValueError:
            print("That ain't a number bro")
if __name__ == "__main__":
    income()