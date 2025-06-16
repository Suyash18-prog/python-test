palindrome_check = input("Enter a string")

palindrome_check=palindrome_check.lower().replace(" ","")
if palindrome_check == palindrome_check[::-1]:
    print("enterred string is a palindrome")