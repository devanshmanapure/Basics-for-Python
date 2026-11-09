# Check whether a number is a three-digit number
number = int(input("Enter a number: "))
if (number >= 100 and number <= 999) or (number <= -100 and number >= -999):
    print("Three-digit number")
else:
    print("Not a three-digit number")