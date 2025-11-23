class BudgetManager:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.expenses = []

    def add_income(self, amount):
        self.balance += amount
        print(f"Income of ₹{amount:.2f} added. New balance: ₹{self.balance:.2f}")

    def add_expense(self, category, amount):
        if amount > self.balance:
            print("Insufficient balance to add this expense!")
            return
        self.expenses.append({'category': category, 'amount': amount})
        self.balance -= amount
        print(f"Expense of ₹{amount:.2f} for {category} added. Remaining balance: ₹{self.balance:.2f}")

    def show_summary(self):
        print(f"\nBudget Summary for {self.name}:")
        print(f"Current Balance: ₹{self.balance:.2f}")
        print("Expenses:")
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for e in self.expenses:
                print(f"  {e['category']}: ₹{e['amount']:.2f}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    manager = BudgetManager(name)

    while True:
        print("\n1. Add Income\n2. Add Expense\n3. View Summary\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amt = float(input("Enter income amount: ₹"))
            manager.add_income(amt)
        elif choice == '2':
            cat = input("Enter expense category: ")
            amt = float(input("Enter expense amount: ₹"))
            manager.add_expense(cat, amt)
        elif choice == '3':
            manager.show_summary()
        elif choice == '4':
            print("Exiting Budget Manager. Have a great day!")
            break
        else:
            print("Invalid choice! Please try again.")