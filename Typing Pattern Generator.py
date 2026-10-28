# Typing Pattern Generator
word = input("Enter word: ")
rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    print(word * i)