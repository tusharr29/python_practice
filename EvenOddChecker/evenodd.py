# Check whether the given number is even or odd

# Using If and else :
number = int(input("Enter a number to check whether it is even or odd:"))

def using_if_else(number):
    if number % 2 == 0 :
        print(f"The given number {number} is Even.")
    else:
        print(f"The given number {number} is Odd.")

# Using Match Case :
def using_match_case(number):
    match number:
        case _ if number % 2 == 0 :
            print(f"The given number {number} is Even.")
        case _ :
            print(f"The given number {number} is Odd.")

method = input("Choose method = 'if_else' or 'match_case':")

if method == 'if_else':
    using_if_else(number)

else:
    using_match_case(number)
    
