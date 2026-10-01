#Ticket Price Calculator
a = int(input("Enter the age"))
if a<=5:
    print("Entry is Free")
elif a>=6 and a<18:
    print("Entry ticket is 5rs")
elif a>=18 and a<30:
    print("Entry ticket is 20rs")
elif a>=30 and a<50:
    print("Entry ticket is 30rs")
elif a>=50:
    print("Entry ticket is 40rs")
else:
    print("Not Applicable")
