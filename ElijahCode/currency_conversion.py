#EHCP2 currency conversion
from forex_python.converter import CurrencyRates

def currency_conversion(income):
    c = CurrencyRates()
    choice = input("Would you like to convert your money to another currency?\nEuros\nPounds\nand a few more\ny or n\n")
    while True:
        if choice == "y":
            try: 
                user_currency = input("What is your current currency? (e.g. USD, EUR)\n").upper()
                new_currency = input("What currency would you like to convert to? (e.g, USD or EUR)\n").upper()
            except TypeError:
                print("Not a currency!")

            rate = c.get_rate(user_currency, new_currency)

            new_amount = income * rate

            print(f"Your new currency amount in {new_currency} is {new_amount:.2f}")
            return new_amount

        elif choice == "n":
            break