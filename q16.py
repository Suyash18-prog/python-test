# Write a function to merge two sorted lists into a single sorted list.

def merge_list(list_1,list_2):
    merge_list = list_1 + list_2
    return sorted(merge_list)
    

numbers = [1, 2, 6, 4, 3, 2, 9]
number2 = [7, 8, 10]  

merged =merge_list(numbers, number2)
print(merged)
