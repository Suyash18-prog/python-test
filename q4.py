def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
    
#Iteration


num = int(input("Enter a number to find factorial"))
fact = 1
for n in range(num):
    fact = fact*n
print(f"Factorial of {num} is : {fact}")