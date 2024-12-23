print("Welcome to the Haunted Castle")
a = input("Do you want to 'enter the castle' or 'run away'?: ").lower()

if a == "enter the castle":
    b = input("Choose a door: 'red', 'green', or 'black': ").lower()
    if b == "red":
        print("You entered a room full of flames. Game Over.")
    elif b == "green":
        print("You found the treasure. You Win!")
    elif b == "black":
        print("You were captured by ghosts. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif a == "run away":
    print("You escaped safely.")
else:
    print("Invalid choice. Game Over.")
