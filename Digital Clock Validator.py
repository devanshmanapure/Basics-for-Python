# Digital Clock Validator
hour = int(input("Enter the hour"))
minute = int(input("Enter the minute"))
if hour >= 0 and hour <= 23 and minute >= 0 and minute <= 59:
    print("Valid time", hour, ":", minute)
    if hour >=5 and hour <=11:
        print("Good Morning")
    elif hour >=12 and hour <=16:
        print("Good Afternoon")
    elif hour >=17 and hour <=20:
        print("Good Evening")
    else:
        print("Night")
else: 
    print("Invalid time")