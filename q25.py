# Write a program to update a specific line in a file.

def update_line(filename,line_number,content_to_be_written):
    with open(filename , 'r') as file:
        lines = file.readlines()

        lines[line_number-1] = content_to_be_written
    with open(filename , 'w') as file:
        for line in lines:
            file.write(line)

update_line("file.txt",3,"Where are you from")