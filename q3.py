#1,1,2,3,5,8....

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

for num in range(1,8):
    print(fib(num),end=" ")