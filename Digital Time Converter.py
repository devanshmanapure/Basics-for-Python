# Digital Time Converter
seconds = int(input("Enter seconds: "))
minutes = seconds // 60
remaining_seconds = seconds % 60
print(minutes, "minutes and", remaining_seconds, "seconds")