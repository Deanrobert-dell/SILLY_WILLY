#BH 2nd Ortho
import csv
from datetime import datetime

present_time = datetime.now()
current_month = present_time.month
current_year = present_time.year

def create_savings_goal(user_id):
	matching_user_profile = None
	try:
		with open('csvfiles/user_profiles.csv', mode='r') as f:
			user_profiles = csv.DictReader(f)
			for row in user_profiles:
				if row["user"] == user_id:
					matching_user_profile = row
					matching_user_profile["balance"] = float(matching_user_profile["balance"])
					break
	except:
		print("There was an error reading the user profiles. Please check the file and try again.")
		return
	if matching_user_profile is None:
		print(f"The user {user_id} does not exist.")
		return
	necessary_money = input("How much money would you like to save up to (please do not add the dollar sign in your amount)?\n")
	necessary_money = validate_float_input(necessary_money)
	savings_time = input("How long are you going to save for (in months)?\n")
	savings_time = validate_float_input(savings_time)
	while savings_time == int(savings_time) <= 0:
		savings_time = input("Invalid input. Please enter a positive number for the number of months you will save for.\n")
	total = round((necessary_money - matching_user_profile["balance"]) / savings_time, 2)
	print(f"You will need to save ${total} each month to reach a total savings of ${necessary_money} in {savings_time} months.")
# expenses is a list of dictionaries with keys "user", "category", "amount", and "date". The "date" value needs to be a datetime instance.
def check_budget_limit(user_id, categories, expenses):
	if categories == []:
		print("Add a category first.")
		return
	selected_category = select_from_list(categories, "Which of the above categories would you like to check your budget for?\n")
	budgets = read_budgets()
	if budgets is None:
		return
	matching_budget = None
	for budget in budgets:
		if budget["user"] == user_id and budget["category"] == selected_category:
			matching_budget = budget
			matching_budget["limit"] = float(matching_budget["limit"])
			break
	if matching_budget is None:
		print("No budget has been set for that category.")
		return
	this_month_expenses = 0
	for expense in expenses:
		if expense["user"] == user_id and expense["category"] == selected_category:
			parse_date_result = parse_date(expense["date"])
			if parse_date_result is None:
				print(f"Invalid date format for expense: {expense}. Skipping this expense.")
				continue
			if parse_date_result.month == current_month and parse_date_result.year == current_year:
				this_month_expenses += expense["amount"]

	print(f"You have spent ${this_month_expenses} out of your ${matching_budget['limit']} budget for {selected_category} this month.")	
# categories is a list of categories as strings
def add_budget_limit(user_id, categories):
	if categories == []:
		print("Add a category first.")
		return
	selected_category = select_from_list(categories, "Which of the above categories would you like to add a budget for (please do not add the dollar sign in your amount)?\n")
	budgets = read_budgets()
	if budgets is None:
		return
	for budget in budgets:
		if budget["user"] == user_id and budget["category"] == selected_category:
			print("A budget already exists for that category.")
			return
	limit = input("What's the monthly budget limit you want for this category (please do not add the dollar sign in your amount)?\n")
	limit = validate_float_input(limit)
	append_budget(user_id, selected_category, limit)
	print(f"A budget of ${limit} has been set for {selected_category}.")
def read_budgets():
	try:
		with open('csvfiles/budgets.csv', mode='r') as file:
			budgets = csv.DictReader(file)
			return list(budgets)
	except:
		print("There was an error reading the budgets file. Please check the file and try again.")
		return None
def append_budget(user_id, selected_category, limit):
	try:
		with open('csvfiles/budgets.csv', mode='a', newline='') as file:
			writer = csv.DictWriter(file, fieldnames=['user', 'category', 'limit'])
			writer.writerow({'user': user_id, 'category': selected_category, 'limit': limit})
	except:
		print("There was an error writing to the budgets file. Please check the file and try again.")
def select_from_list(items, prompt):
    while True:
        print_numbered_list(items)
        selected_item_input = input(prompt)
        if selected_item_input.isdigit() and int(selected_item_input) > 0 and int(selected_item_input) <= len(items):
            return items[int(selected_item_input)-1]
        else:
            print("Invalid input.")
#pretty prints items in a numbered list
def print_numbered_list(items):
	for i, item in enumerate(items):
		print(f"{i+1}: {item}")
def validate_float_input(num):
	while True:
		try:
			return int(num)
		except:
			try:
				return float(num)
			except ValueError:
				num = input("Invalid input. Please enter a number.\n")
#parsing function for datetime
def parse_date(date_string):
    #use datetime
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        return None