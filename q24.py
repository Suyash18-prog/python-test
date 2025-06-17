# Create a program that reads a file and prints only the lines that contain a specific keyword
def line_with_keyword(filename,keyword):
    with open(filename,'r')as file:
        lines = file.readlines()

    for line in lines :
        if keyword in line:
            print(f"line conatining keyword '{keyword}' is :")
            print(line)
        

line_with_keyword('file.txt','what')