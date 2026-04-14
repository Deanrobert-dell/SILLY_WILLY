#EHCP2 expenses
import time as t

from .currency_conversion import currency_conversion

class FinanceManager:
    def __init__(self):
        self.monthly_income = 0
        self.time_entered = None
        self.currency = "USD"

    def get_currency(self):
        self.currency = input("Enter your preferred currency (e.g., USD, EUR, GBP): ").upper()
        self.get_income()

    def get_income(self):
        while True:
            try:
                amount = float(input(f"What is your total monthly income in {self.currency}?\n(No symbols like $): "))
                if amount <= 0:
                    print("Bro, we all know you have an income.")
                    continue
                self.monthly_income = amount
                self.get_expenses()
                break
            except ValueError:
                print("That ain't a number.")

    def get_expenses(self):
        while True:
            try:
                trans = float(input("Monthly cost for transportation?: "))
                food = float(input("Monthly cost for food?: "))
                housing = float(input("Monthly cost for housing?: "))
                extra = float(input("Monthly cost for frivolous stuff?: "))
                
                self.time_entered = t.ctime()
                total_expense = trans + food + housing + extra
                self.calculate_balance(total_expense)
                break
            except ValueError:
                print("That ain't a number. Try again.")

    def calculate_balance(self, total_expense):
        income = self.monthly_income
        remainder = income - total_expense
        
        print("Now it'll ask you to enter your currency you want to convert to 3 times, if you don't want to convert just say 'n'")
        conv_income = convert(income, self.currency)
        conv_expense = convert(total_expense, self.currency)
        conv_diff = convert(abs(remainder), self.currency)

        if not conv_diff:
            conv_diff = (remainder * - 1)

        if not conv_income:
            conv_income = self.monthly_income

        print(f"\n--- Results ({self.currency}) (Recorded: {self.time_entered}) ---")
        
        if total_expense > income:
            print(f"You exceeded your income (${conv_income:.2f}) by ${conv_diff:.2f}")
        elif total_expense == income:
            print("You matched your income exactly! Perfect balance.")
        else:
            print(f"You have ${conv_diff:.2f} left over.")

user_finance = FinanceManager()
user_finance.get_currency()
