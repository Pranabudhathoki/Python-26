a=int(input("Enter a number: "))
if a%2==0:
    if a%5==0:
        print(f"{a}  is divisible by both 2 and 5")
    else:
        print(f"{a} is divisible by 2 only")
else:
    print(f"{a} is not divisible by 2")