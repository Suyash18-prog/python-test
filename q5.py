#list ka 2nd largest

numbers=[1,3,5,3,6,86,75,21]

for num in numbers:
    print(num,end=" ")

max_num = max(numbers)
numbers.remove(max_num)

print(max(numbers))