#Battery Backup Calculator
battery = float(input("Enter battery capacity (mAh): "))
usage = float(input("Enter device consumption (mA): "))
hours = battery / usage
print("Battery Backup:", round(hours, 2), "hours")