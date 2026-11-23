#Parking fees calculator
entry = int(input("Enter entry hour: "))
exit = int(input("Enter exit hour: "))
hours = exit - entry
fee = 30 + (hours - 1) * 20
print("Parking duration:", hours, "hours")
print("Total parking fee: ₹", fee)
