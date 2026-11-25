#Print multiplication table
n = int(input("Enter a number "))
i = 1
print("Multiplication table is: ")
while i <= 10:
  product = n*i
  print(f"{n} x {i} = {n*i}")
  i += 1