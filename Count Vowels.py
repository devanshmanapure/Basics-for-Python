#Count Vowels
Sentence = input("Enter a Sentence:")
Sentence = Sentence.lower()

count = 0

for i in Sentence:
    if i in "aeiou":
        count += 1

print("Number of vowels:", count)