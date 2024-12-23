print("Welcome to the Cybersecurity Mission")
a = input("Do you want to 'trace the hacker' or 'secure the system'?: ").lower()

if a == "trace the hacker":
    b = input("Do you want to 'track their IP' or 'decode their message'?: ").lower()
    if b == "track their IP":
        print("You caught the hacker. You Win!")
    elif b == "decode their message":
        print("The message was a trap. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif a == "secure the system":
    b = input("Do you want to 'shut down the server' or 'upgrade the firewall'?: ").lower()
    if b == "shut down the server":
        print("The attack was stopped. You Win!")
    elif b == "upgrade the firewall":
        print("The hacker bypassed it. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")
