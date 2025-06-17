# Write a program that copies the content of one file to another

with open("name.txt",'r') as file:
    content = file.read()

with open("copy.txt",'w') as file:
    file.write(content)
    