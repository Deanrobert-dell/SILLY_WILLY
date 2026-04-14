import tkinter as tk
from tkinter import messagebox, simpledialog
from BriggsCode.briggs import create_savings_goal, check_budget_limit, add_budget_limit
from ElijahCode.expense_management import FinanceManager
from DeanCode.csv1 import excsv, import1, read_expenses
from DeanCode.line_graph import tspmo
from DeanCode.pichart import plot1
from Nate.NathanCode.login_or_register import FinancialCalculator

user_id = "abc123"
categories = ["food", "entertainment", "gas", "rent"]

def main_menu_gui():
    
    """Main GUI window with all financial calculator features."""
    root = tk.Tk()
    root.title("NH, BH, EH, DP Financial Calculator")
    root.geometry("500x600")

    root.configure(padx=20, pady=20)
    root.configure(bg='#f0f0f0')

    # Header
    header = tk.Label(root, text="FINANCIAL CALCULATOR", font=("Arial", 18, "bold"), bg='#f0f0f0')
    header.pack(pady=(0, 10))
    
    welcome = tk.Label(root, text=f"Welcome, {user_id}!", font=("Arial", 12), bg='#f0f0f0')
    welcome.pack(pady=(0, 20))

    # Button functions
    def handle_add_expense():
        import1()

    def handle_view_trends():
        tspmo(user_id=user_id)

    def handle_view_pie():
        plot1(user_id=user_id)

    def handle_savings():
        create_savings_goal(user_id)

    def handle_check_budget():
        expenses = read_expenses(user_id)
        check_budget_limit(user_id, categories, expenses)

    def handle_add_budget():
        add_budget_limit(user_id, categories)

    def handle_income():
        user_finance = FinanceManager()
        user_finance.get_currency()


    # Styling
    btn_style = {"width": 30, "pady": 12, "font": ("Arial", 11), "bg": "#2E86AB", "fg": "white"}
    btn_style_danger = {"width": 30, "pady": 12, "font": ("Arial", 11), "bg": "#E74C3C", "fg": "white"}

    # Buttons
    tk.Label(root, text="Expense Management", font=("Arial", 11, "bold"), bg='#f0f0f0').pack(pady=(10, 5))
    tk.Button(root, text="1. Add Expense", command=handle_add_expense, **btn_style).pack(pady=5)
    tk.Button(root, text="2. View Expense Trends (Line Graph)", command=handle_view_trends, **btn_style).pack(pady=5)
    tk.Button(root, text="3. View Category Breakdown (Pie Chart)", command=handle_view_pie, **btn_style).pack(pady=5)

    tk.Label(root, text="Budget & Savings", font=("Arial", 12, "bold"), bg='#f0f0f0').pack(pady=(15, 8))
    tk.Button(root, text="4. Create Savings Goal", command=handle_savings, **btn_style).pack(pady=5)
    tk.Button(root, text="5. Check Budget Limit", command=handle_check_budget, **btn_style).pack(pady=5)
    tk.Button(root, text="6. Add Budget Limit", command=handle_add_budget, **btn_style).pack(pady=5)

    tk.Label(root, text="Income", font=("Arial", 12, "bold"), bg='#f0f0f0').pack(pady=(15, 5))
    tk.Button(root, text="7. Manage Income", command=handle_income, **btn_style).pack(pady=5)

    tk.Button(root, text="Exit", command=root.quit, **btn_style_danger).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    excsv()
    main_menu_gui()