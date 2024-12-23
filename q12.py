print("Welcome to the Pirate Ship Adventure")
a = input("Do you want to 'search for treasure' or 'battle enemy ships'?: ").lower()

if a == "search for treasure":
    b = input("Do you want to 'dig on the island' or 'explore the cave'?: ").lower()
    if b == "dig on the island":
        print("You found a hidden treasure chest. You Win!")
    elif b == "explore the cave":
        print("You were trapped inside. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif a == "battle enemy ships":
    b = input("Do you want to 'attack' or 'defend'?: ").lower()
    if b == "attack":
        print("You won the battle. You Win!")
    elif b == "defend":
        print("You were outnumbered. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")
