#Expense Outlier Detector
expenses = []
for i in range(7):
    expenses.append(int(input(f"Enter expense for day {i+1}: ")))
average = sum(expenses) / len(expenses)
print("\nAverage expense:", round(average, 2))
for day, amount in enumerate(expenses, start=1):
    if amount > average:
        print("Above average expense detected!")
        print(f"Day {day}: {amount}")
