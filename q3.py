try:
    a=int(input("Enter your monthly salary: "))
    if a>50000:
        print("Classifyed as High Earner")
    else:
        if a>20000:
            print("Classifyed as Mid Earner")
        else:
            print("Classfied as Low Earner")
except ValueError:
    print("Invalid input")