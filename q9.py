print("Welcome to the Space Adventure")
a = input("Do you want to 'land on Mars' or 'fly to Jupiter'?: ").lower()

if a == "land on Mars":
    b= input("Do you want to 'explore' or 'build a base'?: ").lower()
    if b == "explore":
        print("You found alien artifacts. You Win!")
    elif b == "build a base":
        print("You ran out of resources. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif a == "fly to Jupiter":
    print("Your spaceship crashed. Game Over.")
else:
    print("Invalid choice. Game Over.")
