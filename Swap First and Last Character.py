#Swap First and Last Character
word = input("Enter a word")
new_word = word[-1] + word[1:-1] + word[0]
print("The new word is:", new_word)