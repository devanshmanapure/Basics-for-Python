#Sentence Join
words = []
for i in range(3):
    word = input("Enter your word")
    words.append(word)
result = " ".join(words)
print("combined sentence:", result)