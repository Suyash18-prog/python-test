# Create a custom module named calculator.py with add, subtract, multiply, and divide functions.
# Import and use it in another script.

from calculator import addition,substract,multiply,divide

num_1=int(input("Enter a number"))
num_2=int(input("Enter another number"))

addition(num_1,num_2)
substract(num_1,num_2)
multiply(num_1,num_2)
divide(num_1,num_2)


