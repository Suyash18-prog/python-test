# Write a program to count the frequency of each character in a string using a dictionary.

string = "How are you suyash??!"

char_count={}
for char in string:
    if char not in char_count.keys():
        count=string.count(char)
        char_count[char]=count

print(char_count)