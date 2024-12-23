print("Welcome to the Wizarding World")
a = input("Do you want to study 'spells' or 'potions'?: ").lower()

if a == "spells":
    b = input("Do you want to 'practice magic' or 'compete in duels'?: ").lower()
    if b == "practice magic":
        print("You mastered a powerful spell. You Win!")
    elif b == "compete in duels":
        print("You lost to a rival wizard. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif a == "potions":
    b = input("Do you want to 'brew an elixir' or 'create poison'?: ").lower()
    if b == "brew an elixir":
        print("You healed a village. You Win!")
    elif b == "create poison":
        print("Your potion backfired. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")
