#Find a number:
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number: "))
i = 0
while i < len(nums):
  if (nums[i] == x):
    print("Number Found")
    break
  i += 1
else:
  print("Number not found")