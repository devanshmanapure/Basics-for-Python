#Screenshot generator
date = input("Enter the date in YYYY-MM-DD format: ")
description = input("Enter a description for the screenshot: ")
day, month, year = date.split("-")
name = description.lower().replace(" ", "_")
filename = year + "_" + month + "_" + day + "_" + name + ".png"
print("The filename for the screenshot is:", filename)