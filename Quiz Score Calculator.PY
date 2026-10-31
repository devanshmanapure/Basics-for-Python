# Quiz Score Calculator
total = int(input("Total questions: "))
correct = int(input("Correct answers: "))
wrong = total - correct
percentage = (correct / total) * 100
print("Correct:", correct)
print("Wrong:", wrong)
print("Score:", round(percentage, 2), "%")