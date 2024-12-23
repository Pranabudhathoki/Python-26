print("Welcome to the Jungle Survival Challenge")
a  = input("Do you want to 'search for food' or 'build a shelter'?: ").lower()

if a == "search for food":
    choice = input("Do you want to 'hunt' or 'gather'?: ").lower()
    if choice == "hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif choice == "gather":
        print("You found enough food. You Win!")
    else:
        print("Invalid choice. Game Over.")
elif a == "build a shelter":
    print("Your shelter collapsed in the rain. Game Over.")
else:
    print("Invalid choice. Game Over.")
