income = {"Bubblegum": 202, "Toffee":118, "Ice cream": 2250,
        "Milk chocolate": 1680, "Doughnut": 1075, "Pancake": 80}
expenses = {}
print("Earned amount:")
for item, amount_earned in income.items():
     print(f"{item}: ${str(amount_earned)}")

print("\n")
print(f"Income: ${float(sum(income.values()))}")
expenses["Staff expenses"] = float(input("Staff expenses: \n"))
expenses["Other expenses"] = float(input("Other expenses: \n"))
net_income = float((sum(income.values())) - sum(expenses.values()))
print(f"Net income: ${net_income}")
