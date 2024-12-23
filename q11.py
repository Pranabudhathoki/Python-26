print("Welcome to the Underwater World")
a = input("Do you want to 'dive deeper' or 'surface'?: ").lower()

if a == "dive deeper":
    b = input("Do you want to 'search for pearls' or 'chase the fish'?: ").lower()
    if b == "search for pearls":
        print("You found a rare pearl. You Win!")
    elif b == "chase the fish":
        print("You got lost underwater. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif a == "surface":
    print("You returned safely.")
else:
    print("Invalid choice. Game Over.")
