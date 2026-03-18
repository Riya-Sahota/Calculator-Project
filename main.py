try:
    a = int(input("Enter the value of a : "))

    b = int(input("Enter the value of b : "))

    print("What kind of operation do u want to perform.\n + for addition \n - for subtraction \n * for multiplication \n / for division")

    o = input("Enter the operation : ")

    match o:
        case "+":
            print(f"The result is {a+b}")
        case "-":
            print(f"The result is {a-b}")
        case "*":
            print(f"The result is {a*b}")
        case "/":
            print(f"The result is {a/b}")

except Exception as e:
    print("Enter valid value of a and b")    

