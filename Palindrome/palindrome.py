#To check the givem string is palindrome or not

string = input("Enter a string to check whether it is palindrome or not:")

reversed_string = string[::-1]

if string == reversed_string:
    print(f"The given string '{string}' is a Palindrome.")
else:
    print(f"The given string '{string}' is not a Palindrome.")