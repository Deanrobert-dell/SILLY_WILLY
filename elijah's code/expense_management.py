#EHCP2 expenses
from currency_conversion import currency_conversion
from currex import *

def inputs():
    while True:
        try:
            budget = Currency('USD', float(input("What is your total monthly income?\n")))
            if budget <= 0:
                pass
            if budget > 0:
                currency_conversion(budget)
                return budget
        except ValueError:
            print("That ain't a budget!")

def expenses():
    