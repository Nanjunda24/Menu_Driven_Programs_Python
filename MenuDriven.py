def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    print("-----Simple calculator-----")
    print("1. Addition ")
    print("2. Substraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. Exit ")

    choice = int(input("Enter your choice (1 - 5): "))

    if (choice == 1):
        num1 = int(input("Enter a number 1: "))
        num2 = int(input("Enter a number 2: "))
        result=add(num1,num2)
        print("Result: ",result)

    elif (choice == 2):
        num1 = int(input("Enter a number 1: "))
        num2 = int(input("Enter a number 2: "))
        result=sub(num1,num2)
        print("Result: ",result)

    elif (choice == 3):
        num1 = int(input("Enter a number 1: "))
        num2 = int(input("Enter a number 2: "))
        result=mul(num1,num2)
        print("Result: ",result)

    elif (choice == 4):
        num1 = int(input("Enter a number 1: "))
        num2 = int(input("Enter a number 2: "))
        result=div(num1,num2)
        print("Result: ",result)

    elif choice == 5:
        print("Exit successfully!!!!")
        break

