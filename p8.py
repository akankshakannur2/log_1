# Python code to print Fibonacci series 
# Fibonacci series using for loop

def Fibonacci_1():
    n = int(input("Enter the number:"))
    fibo = [0,1]
    if n > 2:
        for i in range(2,n):
            num = fibo[i-1] + fibo[i-2]
            fibo.append(num)
        print(fibo)
Fibonacci_1()

