# Program to censor a particular word in a sentence

sentence = input("Enter a sentence: ")
word = input("Enter the word to censor: ")

result = sentence.replace(word, "****")

print("Censored sentence:", result)