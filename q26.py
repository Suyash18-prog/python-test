# Use the math module to calculate the square root, sin, and factorial of a number.

from math import sqrt,sin,factorial

num_1 = int(input("Enter number to find square root : "))
num_2 = int(input("Enter number to find sine : "))
num_3 = int(input("Enter number to find factorial : "))

print(f'Square root of {num_1} = {sqrt(num_1)}')
print(f"Sine of {num_2} = {sin(num_2)}")
print(f"Facotrial of {num_3} = {factorial(num_3)}")

