#Username cleaner
sentence = input("Enter your sentence")
result = " ".join(sentence.strip().split())
print("Cleaner sentence is:", result)