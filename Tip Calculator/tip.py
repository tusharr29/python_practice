#To calculate and divide tip among people

print("Welcome to the Tip Calculator!")

bill_amount = float(input("Enter the total bill amount: $"))

tip = float(input("Enter the amounnt of tip you would like to give: $ "))

num_people = int(input("Enter the number of people to split the bill: "))

total_bill = tip + bill_amount

final_Split = total_bill / num_people

print(f"Each person should pay : ${final_Split}")

print("Thank you for using the Tip Calculator!")