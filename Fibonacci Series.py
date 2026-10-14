#Fibonacci Series
terms = int(input("Enter the number of terms: "))
a, b = 0, 1
for i in range(terms):
    print(a, end=' ')
    a, b = b, a + b