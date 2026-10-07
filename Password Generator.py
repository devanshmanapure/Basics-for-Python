#Password Generator
import random
charecters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
n = int(input("Enter the length of password: "))
password = ""
for i in range(n):
    password += random.choice(charecters)
print(f"Generated password: {password}")