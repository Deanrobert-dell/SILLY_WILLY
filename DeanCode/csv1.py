import csv
from datetime import datetime
from ElijahCode.expense_management import *


"""Csv
Take income from Elijah's list and append it to a csv file
Take expenses and import them, keep them in categories
For this have a 3rd row called expenses , and call that to sort by expenses
FOR each item IN expense_items:
    rows.APPEND({
      date: item.date,
      type: "expense",
      description: item. *blank*,
      category: item.category ,
Match each income and expense with date
csv: expenses.csv, profiles.csv, income.csv etc.
categories (user input, list)
"""



with open('expenses.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    #write categories from the elijah expense managment code
    writer.writerow(['user', 'category', 'amount', 'date'])

