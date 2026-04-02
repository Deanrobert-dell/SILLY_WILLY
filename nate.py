#Create class for finance calc
class FinancialCalculator:
#make the login function
def login(self):
        while True:
        print("Welcome back!")
        username = input("Please enter your username: ").strip()
        
        #Logic to check user_registrations.csv for username
        if self.check_credentials(username, mode="user"):
            print("Verified!")
            password = input("Now enter password: ")
            
            # Logic to check password match in CSV
            if self.check_credentials(username, password, mode="password"):
                print("Perfect! You’re good to go!")
                self.main_menu()
                break
            else:
                print("Incorrect password. Try again.")
        else:
            print("Invalid username. Try again.")
#Make the register function!
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
    pass

# Entry Point
if __name__ == "__main__":
program= FinancialCalculator()
# Choose to start with app.register() or app.login()
program.login()
#start the program!
