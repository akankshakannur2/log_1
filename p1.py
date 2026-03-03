# Write a python code to perform all Arithmetic Operations on two numbers
a=input("Enter First number:")
b=input("Enter Second number:")

sum = float(a) + float(b)
sub = float(a) - float(b)
mul = float(a) * float(b)
div = float(a) / float(b)
fdiv = float(a) // float(b)
exp = float(a) ** float(b)
mod = float(a) % float(b)

print("Sum:", sum)
print("SUbtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
print("Floor Division:", fdiv)
print("Exponential:", exp)
print("Modulus:", mod)