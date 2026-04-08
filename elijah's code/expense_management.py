#EHCP2 expenses

from currency_conversion import currency_conversion

def expenses():
    try:
        monthly_income = float(input("What is your total monthly income?\n"))
    except ValueError:
        print("That ain't a number")
