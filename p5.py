# Write a python program to create the background code for calculator
# This code is by using while loop
# we can create this program by creating functions for each arithmetic operation
def Calculator():
    while True:
        print("Addition : 1")
        print("Subtraction : 2")
        print("Multiplication : 3")
        print("Division : 4")

        user_input = input("Enter your choice :")

        if user_input == "quite":
            break
        elif user_input in ["1" , "2" , "3" , "4"]:
            a = input("Enter first number:")
            b = input("Enter second number:")

            if user_input == "1":
                output = float(a) + float(b)
                print(output)
            elif user_input =="2":
                output = float(a) - float(b)
                print(output)
            elif user_input == "3":
                output = float(a) * float(b)
                print(output)
            elif user_input == "4":
                output = float(a) / float(b)
                print(output)
        else:
            print("Invalid Input")
Calculator()

        