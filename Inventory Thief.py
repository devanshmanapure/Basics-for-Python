#Inventory Thief
items = ["sword","helmet", "shield"]
choice = input("What item would you like to steal?")
if choice in items:
    items.remove(choice)
    print(f"You have stolen the {choice}!")
else:
    print("Item not found in inventory.")