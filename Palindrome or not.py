#WAP to check if the invup character is a palindrome or not
list1 = [1, 2, 1]
list2 = [1, 2, 3]
copy_list1 = list1.copy()
copy_list2 = list2.copy()
copy_list1.reverse()
copy_list2.reverse()
if (list1 == copy_list1):
  print("List 1 is a palindrome")
else:
  print("List 1 is not a palindrome")
if (list2 == copy_list2):
  print("List 2 is a palindrome")
else:
  print("List 2 is not a palindrome")
