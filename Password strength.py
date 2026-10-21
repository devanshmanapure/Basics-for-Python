#Password strength
password = input("Enter your password:")
if len(password) <= 4:
    print("Your password is weak. Consider using a stronger password.")
elif len(password) <= 7:
    print("Your password is moderate. You can improve it for better security.")
else:
    print("Your password is strong. Good job!")
    