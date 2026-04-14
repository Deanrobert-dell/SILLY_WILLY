import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from collections import defaultdict
from DeanCode.csv1 import read_expenses

def parse_date(date_string):
    """Parse date string to datetime object."""
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        return None

def aggregate_expenses_by_date(expenses):
    """Aggregate expenses by date, returning average amount per date."""
    date_amounts = defaultdict(list)
    
    for expense in expenses:
        date_obj = parse_date(expense['date'])
        if date_obj:
            date_amounts[date_obj].append(expense['amount'])
    
    # Calculate average for each date
    result = []
    for date in sorted(date_amounts.keys()):
        avg_amount = sum(date_amounts[date]) / len(date_amounts[date])
        result.append({
            'date': date,
            'date_str': date.strftime('%Y-%m-%d'),
            'average_amount': avg_amount
        })
    
    return result

def plot_expense_trends(user_id=None, start_date=None, end_date=None):
    """
    Create a line graph of expense trends over time.
    
    Args:
        user_id: Optional filter by user
        start_date: Optional start date filter (YYYY-MM-DD)
        end_date: Optional end date filter (YYYY-MM-DD)
    """
    # Read expenses
    expenses = read_expenses(user_id)
    
    if not expenses:
        print("No expenses found to plot.")
        return
    
    # Filter by date range if provided
    if start_date or end_date:
        start = parse_date(start_date) if start_date else datetime.min
        end = parse_date(end_date) if end_date else datetime.max
        expenses = [e for e in expenses if start <= parse_date(e['date']) <= end]
    
    if not expenses:
        print("No expenses in the specified date range.")
        return
    
    # Aggregate by date
    aggregated = aggregate_expenses_by_date(expenses)
    
    if not aggregated:
        print("Could not process expense data.")
        return
    
    # Extract data for plotting
    dates = [item['date_str'] for item in aggregated]
    amounts = [item['average_amount'] for item in aggregated]
    
    # Calculate average line
    avg_expense = np.mean(amounts)
    avg_line = [avg_expense] * len(dates)
    
    # Create plot
    plt.figure(figsize=(12, 6))
    plt.plot(dates, amounts, marker='o', linewidth=2, label='Daily Average Expenses', color='#2E86AB')
    plt.plot(dates, avg_line, linestyle='--', linewidth=2, label=f'Overall Average (${avg_expense:.2f})', color='red')
    
    # Customize plot
    plt.title('Expense Trends Over Time', fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Amount ($)', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Show plot
    plt.show()

if __name__ == "__main__":
    # Example usage
    plot_expense_trends(user_id="abc123")