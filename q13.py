# Write a program to reverse a list without using [::-1] or reverse() method.

numbers = [1,2,3,4,5,6,7,9]
reversed_list=[]

for num in numbers:
    reversed_list.insert(0,num)
print(reversed_list)