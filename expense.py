import os
import csv


class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def delete_expense(self, expense):
        self.expenses.remove(expense)

    def get_expenses(self):
        return self.expenses

    def save_expenses_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])
            for expense in self.expenses:
                writer.writerow([expense.date, expense.category, expense.description, expense.amount])

    def load_expenses_from_file(self, filename):
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    date, category, description, amount = row
                    expense = Expense(date, category, description, amount)
                    self.add_expense(expense)


def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    # for i, expense in enumerate(expenses, start=1):
    #     print(f"Expense #{i}")
    #     print(f"Date: {expense.date}")
    #     print(f"Category: {expense.category}")
    #     print(f"Description: {expense.description}")
    #     print(f"Amount: {expense.amount}")
    #     print()

    for i in range(len(expenses)):
        expense = expenses[i]
        print(f"Expense #{i + 1}")
        print(f"Date: {expense.date}")
        print(f"Category: {expense.category}")
        print(f"Description: {expense.description}")
        print(f"Amount: {expense.amount}")
        print()


def create_expense():
    print("Creating a new expense.")
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    amount = input("Enter the amount: ")
    expense = Expense(date, category, description, amount)
    return expense


def main_menu():
    print("Expense Management System")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Save Expenses")
    print("5. Load Expenses")
    print("0. Exit")


def save_expenses(manager):
    filename = input("Enter the filename to save expenses: ")
    manager.save_expenses_to_file(filename)
    print("Expenses saved successfully.")


def load_expenses(manager):
    filename = input("Enter the filename to load expenses: ")
    manager.load_expenses_from_file(filename)
    print("Expenses loaded successfully.")


def main():
    manager = ExpenseManager()

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            expense = create_expense()
            manager.add_expense(expense)
            print("Expense added successfully.")
        elif choice == "2":
            expenses = manager.get_expenses()
            display_expenses(expenses)
        elif choice == "3":
            expenses = manager.get_expenses()
            display_expenses(expenses)
            index = int(input("Enter the index of the expense to delete: ")) - 1
            if 0 <= index < len(expenses):
                expense = expenses[index]
                manager.delete_expense(expense)
                print("Expense deleted successfully.")
            else:
                print("Invalid index.")
        elif choice == "4":
            save_expenses(manager)
        elif choice == "5":
            load_expenses(manager)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
