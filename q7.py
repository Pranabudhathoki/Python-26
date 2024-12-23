print("Welcome to the Forest Adventure")
a = input("Choose a path: 'left' or 'right': ").lower()

if a == "left":
    b = input("Do you want to 'explore' or 'rest'?: ").lower()
    if b == "explore":
        print("You found treasure!")
    elif b == "rest":
        print("You were attacked by wild animals. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif a == "right":
    print("You fell into a trap. Game Over.")
else:
    print("Invalid choice. Game Over.")
