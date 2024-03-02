class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def show_summary(self):
        print("Expense Summary:")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")

# Example usage
tracker = ExpenseTracker()

# User input
tracker.add_expense("Groceries", 50)
tracker.add_expense("Dining out", 30)
tracker.add_expense("Groceries", 20)

# Display summary
tracker.show_summary()
