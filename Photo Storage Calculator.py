# Photo Storage Calculator

photos = []

a = int(input("Enter photo size: "))
photos.append(a)

b = int(input("Enter photo size: "))
photos.append(b)

c = int(input("Enter photo size: "))
photos.append(c)

total = sum(photos)

print("Photo sizes:", photos)
print("Total storage:", total, "MB")
print("Largest photo:", max(photos), "MB")