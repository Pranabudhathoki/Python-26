a = int(input("Enter a number: "))

if a % 2 == 0 and a % 7 == 0:
    print("Double Seven")
elif a % 2 == 0:
    print("Even")
elif a % 7 == 0:
    print("Lucky Seven")
else:
    print(a)
