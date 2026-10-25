#Word scramber

# Word Scrambler

word = input("Enter a word: ")
result = word[::-1]

final = ""

for i in range(len(result)):
    if i % 2 == 1:
        final += result[i].upper()
    else:
        final += result[i].lower()

print("Scrambled word:", final)
