#Alphabet Position Converter
word = input("Enter a word: ").upper()
for letter in word:
    print(letter, "=", ord(letter) - 64)