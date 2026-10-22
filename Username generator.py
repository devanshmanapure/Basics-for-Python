#Username generator
name = input("Enter your name")
year = input("Enter your birth year")
username = name.lower() + "_" + year[-2:]
print("Your username is: " + username)