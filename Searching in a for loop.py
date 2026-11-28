#Searching in a for loop
tup = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x = int(input("Enter a value: "))
for i in tup:
  if (i == x):
    print("Number found")
    break
else:
  print("Number not found")