# Monthly expenses
expenses = [2200, 2350, 2600, 2130, 2190]

# 1. Calculate extra expense in Feb compared to Jan
extra_expense_feb = expenses[1] - expenses[0]
print(f"Extra expense in February compared to January: {extra_expense_feb}")

# 2. Calculate total expense in first quarter (first three months)
total_expense_first_quarter = sum(expenses[:3])
print(f"Total expense in the first quarter: {total_expense_first_quarter}")

# 3. Check if you spent exactly 2000 dollars in any month
spent_2000 = 2000 in expenses
print(f"Did you spend exactly 2000 dollars in any month? {spent_2000}")

# 4. Add June's expense to the list
expenses.append(1980)
print("Monthly expenses after adding June's expense:", expenses)

# 5. Correct April's expense due to refund
refund_amount = 200
expenses[3] -= refund_amount
print("Monthly expenses after correcting April's refund:", expenses)
