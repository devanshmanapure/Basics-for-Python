#A class Student has been defined to calculate the result of a student
Name = str(input("Enter your Name"))
Roll_No = int(input("Enter your Roll no."))
Marks_1 = float(input("Enter Marks of Subject 1"))
Marks_2 = float(input("Enter Marks of Subject 2"))
Marks_3 = float(input("Enter Marks of Subject 3"))
Percentage = float(Marks_1 + Marks_2 + Marks_3)/300*100
print("Name", Name)
print("Roll_No", Roll_No)
print("Percentage", Percentage, "%")
