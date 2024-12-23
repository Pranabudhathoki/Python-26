try:
    a = float(input("Enter price of the product: "))
    if a >= 1000:
        discount = a - a * (10 / 100)
        print(f"Your total cost is {discount}")
    elif a >= 500 and a < 1000:
        discount = a - a * (5 / 100)
        print(f"Your total cost is {discount}")
    else:
        print("No discount applied")
        print(f"Your total cost is {a}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

