import matplotlib.pyplot as plt
from collections import defaultdict
from DeanCode.csv1 import read_expenses

def calculate_category_totals(expenses):
    """Calculate total expenses by category."""
    category_totals = defaultdict(float)
    
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        category_totals[category] += amount
    
    return dict(category_totals)

def plot_expense_pie_chart(user_id=None):
    """
    Create a pie chart showing expense breakdown by category.
    
    Args:
        user_id: Optional filter by user
    """
    # Read expenses
    expenses = read_expenses(user_id)
    
    if not expenses:
        print("No expenses found to plot.")
        return
    
    # Calculate category totals
    category_totals = calculate_category_totals(expenses)
    
    if not category_totals:
        print("Could not process expense data.")
        return
    
    # Prepare data for pie chart
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())
    
    # Create color palette
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2']
    colors = colors[:len(categories)]
    
    # Create pie chart
    fig, ax = plt.subplots(figsize=(10, 8))
    
    wedges, texts, autotexts = ax.pie(
        amounts,
        labels=categories,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        textprops={'fontsize': 11}
    )
    
    # Enhance text appearance
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    # Add title
    total_expenses = sum(amounts)
    ax.set_title(
        f'Expense Breakdown by Category\nTotal: ${total_expenses:.2f}',
        fontsize=14,
        fontweight='bold',
        pad=20
    )
    
    # Add legend with amounts
    legend_labels = [f'{cat}: ${amount:.2f}' for cat, amount in category_totals.items()]
    ax.legend(legend_labels, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example usage
    plot_expense_pie_chart(user_id="abc123")