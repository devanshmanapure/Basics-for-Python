#Download Time Calculator
size = float(input("Enter file size (MB): "))
speed = float(input("Enter internet speed (Mbps): "))
time = (size * 8) / speed
print("Download Time:", round(time, 2), "seconds")