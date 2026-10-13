#Zombie Survival
choice = input("zombie approaching, You will run, hide and fight?").lower()
if choice == "run":
    print("You run away from the zombie and find a safe place to hide, you are safe.")
elif choice == "hide":
    print("You hide behind a dumpster and wait for the zombie to pass but the zombie finds you.")    
elif choice == "fight":
    print("You decide to fight the zombie with a nearby weapon, you defeat the zombie.")
else:
    print("Bad Decision. Please choose Run, Hide, or Fight.")