#Traffic lights
light = input("Enter traffic light (Red, Yellow or Green):")
if (light == "green"):
  print("go")
elif (light == "yellow"):
  print("be ready")
elif (light == "red"):
  print("stop")
else:
  print("Invalid signal")