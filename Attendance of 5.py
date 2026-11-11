# WAP to count present and absent students

attendance = []

for i in range(1, 6):
    status = input(f"Enter attendance of student {i}: ")
    attendance.append(status.upper())

print("Attendance:", attendance)
print("Present students:", attendance.count("P"))
print("Absent students:", attendance.count("A"))