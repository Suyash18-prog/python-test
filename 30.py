#  Write a script using os module to list all files in a directory and count how many are .txt files.

import os 

files_list = os.listdir()
print (f"list of all files in directory is :{files_list} ")
count = 0
for file in files_list:
    if file.endswith('.txt'):
        count+=1

print(f"Number of .txt files is {count}")