#BH 2nd Ortho
categories = [
	{
}
]
def track_savings_goal():
	current_money = #FROM CSV#
	necessary_money = input(“How much money would you like to save up to?”)
	savings_time = input(“How long are you going to save for (in months)?”)
	total = (necessary_money - current_money) / savings_time
	print(“You will need to add ${total} to your savings each day to earn {necessary_money} in {savings_time} months?”)
def check_budget_limit(categories):
	for key in categories:
		print(key)
	category_to_check = input(“Which of the above categories would you like to check?”) 
	If not categories['category_to_check']:
		print(“That category does not exist.”)
		return
	print(f”The budget for that category is {categories['category_to_check']}.”)
def add_budget_limit(categories):
	for key in categories:
		print(key)
	category_needing_budget = input(“Which of the above categories would you like to check?”)
	If not categories['category_needing_budget']:
		print(“That category does not exist.”)
		return
	If categories['category_needing_budget'] != “None”:
		print(“A budget already exists for that category.”)
		return
	limit = input(“What's the budget limit you want for this category (Please do not add the dollar sign in your amount)?”)
	categories['category_needing_budget'] = limit