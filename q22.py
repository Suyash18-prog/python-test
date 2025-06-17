#  Create a file and write a list of names into it, then read and print those names in reverse order.

names = ["Suyash","Prakhar","Gourav","Utsav"]

with open("name.txt" ,'w') as file:
    for name in names:
        file.write(str(name))
        file.write(" ")
with open("name.txt" ,'r') as file:
     content = file.read()

print(content[::-1])
