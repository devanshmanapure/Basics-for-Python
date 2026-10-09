# Smart Study Timer
minute = int(input("Enter study minutes:"))
if minute < 0:
    print("Invalid Input.")
else:
    if minute < 25:
        print("Study time is too short.")
    elif minute < 50:
        print("Good Focus.")
    elif minute < 75:
        print("Great Focus.")
    else:
        print("Take a break.")

    remaining_minutes = 120 - minute

    if remaining_minutes > 0:
        print("Minutes left to reach 2 hours.", remaining_minutes)
    else:
        print("You have completed 2 hours of study.")
