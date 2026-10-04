# Count Character Frequency
word = input("Enter any word")
char = input("Enter a charechter")
count = 0
for i in word:
    if i == char:
        count += 1
print("Charechter appears", count, "times")