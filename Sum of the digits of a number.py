#Find the sum of the digits of a number
a = int(input("Enter a number: "))
result = sum(int(digit) for digit in str(a))
print("The sum of the digits of the number is:", result)