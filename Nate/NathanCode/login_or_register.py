#import csv
import csv

class FinancialCalculator:

    # Make the register function!
    def login(self):
                while True:
                    print("Welcome back!")
                    user_id = input("Please enter your username: ").strip()
    
                    #Logic to check user_registrations.csv for username
                    if self.check_credentials(user_id, mode="user"):
                        print("Verified!")
                        password = input("Now enter password: ")
                        # Logic to check password match in CSV
                        if self.check_credentials(user_id, password, mode="password"):
                            print("Perfect! You're good to go!")
                            self.main_menu()
                            break
                        else:
                            print("Incorrect password. Try again.")
                    else:
                        print("Invalid username. Try again.")
    
    def register(self):
        print("Hello and welcome new user!")
        new_user = input("Please enter your new username: ")
        new_pass = input("Please enter your new password: ")

        # Logic to append new user info to the CSV
        with open('user_registrations.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_user, new_pass])
        #Show that the user was registered!
        print("Registration successful!")
        self.login()

    # Helper function for CSV validation logic
    def check_credentials(self, username, password=None, mode="user"):
        # READ user_registrations.csv
        # IF mode is "user": return True if username exists
        # IF mode is "password": return True if password matches username row
        try:
            with open('user_registrations.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == username:
                        if mode == "user":
                            return True
                        elif mode == "password" and len(row) > 1 and row[1] == password:
                            return True
            return False
        except FileNotFoundError:
            return False
 