# Python code to find entered number is even or odd

def oddEven():
    num = int(input("Enter the number:"))
    if num > 0 and num % 2 == 0 : 
        print("Number is Even")
    else:
        print("Number is Odd")
oddEven()
