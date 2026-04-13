#NH Main for Finance manager
import tkinter as tk
from tkinter import messagebox

# --- The existing logic and imports ---
# (Keep your imports and data lists at the top as they were)
user_id = "abc123"
categories = ["food", "entertainment", "gas", "rent"]
expenses = []

# Placeholder functions (replace with actual implementations)
def create_savings_goal(user_id):
    messagebox.showinfo("Savings Goal", f"Creating savings goal for {user_id}")

def check_budget_limit(user_id, categories, expenses):
    messagebox.showinfo("Budget Check", f"Checking budget for {user_id}")

def add_budget_limit(user_id, categories):
    messagebox.showinfo("Add Budget", f"Adding budget limit for {user_id}")

def income():
    messagebox.showinfo("Expense Management", "Opening expense management")

def main_menu_gui():
    # Create the main window
    root = tk.Tk()
    root.title("NH, BH, EH, DP Financial Calculator")
    root.geometry("400x550")
    root.configure(padx=20, pady=20)

    # Header Label
    header = tk.Label(root, text="FINANCIAL CALCULATOR", font=("Arial", 16, "bold"))
    header.pack(pady=(0, 10))
    
    welcome = tk.Label(root, text=f"Welcome, {user_id}!", font=("Arial", 10))
    welcome.pack(pady=(0, 20))

    # --- Button Functions (Linking to your team modules) ---
    def handle_savings():
        # Calls your existing function from Nate/Briggs
        create_savings_goal(user_id)

    def handle_check_budget():
        # Calls your existing check function
        check_budget_limit(user_id, categories, expenses)

    def handle_add_budget():
        add_budget_limit(user_id, categories)

    def handle_expense_mgmt():
        # Calls Elijah's income function
        income()

    # --- Button Frame ---
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    button_savings = tk.Button(button_frame, text="Create Savings Goal", command=handle_savings, width=25, pady=10)
    button_savings.pack(pady=5)

    button_check = tk.Button(button_frame, text="Check Budget Limit", command=handle_check_budget, width=25, pady=10)
    button_check.pack(pady=5)

    button_add = tk.Button(button_frame, text="Add Budget Limit", command=handle_add_budget, width=25, pady=10)
    button_add.pack(pady=5)

    button_expense = tk.Button(button_frame, text="Expense Management", command=handle_expense_mgmt, width=25, pady=10)
    button_expense.pack(pady=5)

    button_exit = tk.Button(button_frame, text="Exit", command=root.quit, width=25, pady=10, bg="red", fg="white")
    button_exit.pack(pady=5)

    # --- Create Menu Bar ---
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # File Menu
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=root.quit)

    # Operations Menu
    ops_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Operations", menu=ops_menu)
    ops_menu.add_command(label="Create Savings Goal", command=handle_savings)
    ops_menu.add_command(label="Check Budget Limit", command=handle_check_budget)
    ops_menu.add_command(label="Add Budget Limit", command=handle_add_budget)
    ops_menu.add_command(label="Expense Management", command=handle_expense_mgmt)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main_menu_gui()