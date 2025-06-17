# Write a Python program to read a text file and count the number of lines and words.

with open("file.txt",'r') as file:
    content = file.readlines()

    total_lines = len(content)
    total_words =sum([len(line.split()) for line in content])

print(f" total lines = {total_lines}")
print(f" total words = {total_words}")