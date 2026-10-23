#Email Masker
email = input("Enter your email")
name, domain = email.split("@")
masked = name[0] + "*" * (len(name) - 1)
print("masked email:", masked + "@" + domain)