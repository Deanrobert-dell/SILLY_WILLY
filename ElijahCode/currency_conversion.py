#EHCP2 currency conversion
while True:
    try:
        from forex_python.converter import CurrencyRates, RatesNotAvailableError
        break
    except ImportError:
        print("Cannot import the module forex_python, you need to do 'pip install forex_python'")
        break

def convert(income, new_currency):
    c = CurrencyRates()
    choice = input("Would you like to convert your money to another currency?\nEuros\nPounds\nand a few more\ny or n\n")
    while True:
        if choice == "y":
            try: 
                user_currency = input("What is your current (not prefered) currency? (e.g. USD, EUR)\n").upper()
            except RatesNotAvailableError:
                print("Not a currency!")

            rate = c.get_rate(user_currency, new_currency)

            new_amount = income * rate

            print(f"Your new currency amount in {new_currency} is {new_amount:.2f}")
            return new_amount

        else:
            break