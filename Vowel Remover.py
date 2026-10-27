# Vowel Remover
sentence = input("Enter a sentence: ")
for vowel in "aeiouAEIOU":
    sentence = sentence.replace(vowel, "")
print("Output:", sentence)
