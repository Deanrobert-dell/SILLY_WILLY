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
    root.geometry("400x450")
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

    # --- UI Buttons ---
    btn_style = {"width": 25, "pady": 10, "font": ("Arial", 10)}

    tk.Button(root, text="1. Create Savings Goal", command=handle_savings, **btn_style).pack(pady=5)
    tk.Button(root, text="2. Check Budget Limit", command=handle_check_budget, **btn_style).pack(pady=5)
    tk.Button(root, text="3. Add Budget Limit", command=handle_add_budget, **btn_style).pack(pady=5)
    tk.Button(root, text="4. Expense Management", command=handle_expense_mgmt, **btn_style).pack(pady=5)

    tk.Button(root, text="Exit", command=root.quit, fg="red", width=15).pack(pady=20)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main_menu_gui()