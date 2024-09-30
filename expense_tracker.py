from expense import Expense
from datetime import  datetime
import calendar

def main():
    print("Running Expense Tracker")
    expense_file_path = 'expenses.csv'
    budget = 2000

    # Get user input for Expense
    expense = get_user_expense()
    print(expense)
    # Write their expense to a file
    save_expense_to_file(expense, expense_file_path)
    # Read file and summarize expense
    summerize_expenses(expense_file_path, budget)
    pass


def get_user_expense():
    print("Getting user Expenses")
    expense_name = input("Enter Expense name: ")
    expense_amount = float(input("Enter Expense amount: "))

    expense_categories = [
        "Food",
        "Rent",
        "Entertainment",
        "Fees"
        "Miscellaneous"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        if selected_index in range(len(expense_categories)):
            new_Expense = Expense(name=expense_name,category=expense_categories[selected_index],amount=expense_amount)

            return new_Expense
        else:
            print("Invalid category, Please try again")



def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summerize_expenses(expense_file_path, budget):
    print("Summerizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.rstrip().split(",")
            line_expense = Expense(name=expense_name,amount=float(expense_amount),category=expense_category)
            print(line_expense)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses by Category: ")
    for key, amount in amount_by_category.items():
        print(f"    {key}: {amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"Total amount spent: {total_spent}")

    remaining_budget = budget - total_spent
    print(f"Budget Remaining: {remaining_budget}")

    now = datetime.now()
    days_in_month = calendar.monthrange(now.year,now.month)[1]
    remaining_days = days_in_month - now.day
    print(f"Remaining days in current month: {remaining_days}")

    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
        print(f"Budget per day: Rs.{daily_budget:.2f}")
    else:
        print("End of the month. No days remaining to calculate the daily budget.")
if __name__ == '__main__':
    main()
