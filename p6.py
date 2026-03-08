# Python code to find whether the number is Armstrong or not
# We are doing with pow() function and for loop

num = input("enter the number:")
n = len(num)
digit = 0
for i in num:
    digit += pow(int(i), n)
if digit == int(num):
    print("It is Armstrong Number")
else:
    print("It is not Armstrong Number")