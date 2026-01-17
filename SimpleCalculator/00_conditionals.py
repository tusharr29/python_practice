# Calculator using match case

num1= int(input("Enter a number 1:"))

num2 = int(input("Enter a number 2 :"))

operation = input("Enter an operation (+ , -, *, / :")

# if num % 2 == 0:
#     print("The number is even.")

# else:
#     print("The number is odd.")

match operation:
    case "+" :
        num = num1 + num2
        print(f"The addition of {num1} and {num2} is {num}")
    case "-" :
        num = num1 - num2
        print(f"The subtraction of {num1} and {num2} is {num}")
    case "*" :
        num = num1 * num2
        print(f"The multiplication of {num1} and {num2} is {num}")
    case "/" :
        num = num1 / num2
        print(f"The division of {num1} and {num2} is {num}")

    case _:
        print("Invalid input")
  