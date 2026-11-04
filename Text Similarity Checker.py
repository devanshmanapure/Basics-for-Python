#Text Similarity Checker
a = set(input("Enter first sentence: ").lower().split())
b = set(input("Enter second sentence: ").lower().split())
common = a & b
print("Common Words:", common)
print("Similarity:", round(len(common) / len(a | b) * 100, 2), "%")