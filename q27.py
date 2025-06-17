# Create a custom module named calculator.py with add, subtract, multiply, and divide functions.
# Import and use it in another script.

from calculator import add,substraction,multiply,divide

num_1=int(input("Enter a number :"))
num_2=int(input("Enter another number :"))

print(add.addition(num_1,num_2))
print(substraction.substract(num_1,num_2))
print(multiply.multiply(num_1,num_2))
print(divide.divide(num_1,num_2))


