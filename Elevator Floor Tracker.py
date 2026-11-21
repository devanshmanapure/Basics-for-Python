# Elevator Floor Tracker
floor = 0
while True:
    movement = input("Enter movement (+/- floors) or 'stop': ")
    if movement == "stop":
        break
    floor += int(movement)
    print("Current floor:", floor)
print("Final floor:", floor)