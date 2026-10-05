#Print Alternating Numbers
a = int(input("Enter a number:"))
for i in range(1, a + 1):
    if i % 2 == 0:
        print(-i)
    else:
        print(i)