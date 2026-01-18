#Rock Paper Scissor Game

print("Welcome to Rock Paper Scissor Game!")

user_input = int(input("Enter a choice: 0 for Rock, 1 for Paper, 2 for Scissor:"))

import random

computer_choice = random.randint(0,2)

if user_input == computer_choice:
    print("It's a Tie!")
elif (user_input == 0 and computer_choice == 2) or (user_input == 1 and computer_choice == 0) or (user_input == 2 and computer_choice == 1):
    print("You Win!")
else:
    print("Computer Wins!")

#Using match case

match computer_choice:
    case 0:
        if user_input == 0:
            print("It's a Tie!")
        elif user_input == 1:
            print("You Win!")
        else:
            print("Computer Wins!")
    case 1:
        if user_input == 0:
            print("Computer Wins!")
        elif user_input == 1:
            print("It's a Tie!")
        else:
            print("You Win!")
    case 2:
        if user_input == 0: 
            print("You Win!")      
        elif user_input == 1:
            print("Computer Wins!")
        else:
            print("It's a Tie!")

user_choice_str = input("Enter your choice as Rock, Paper or Scissor:").lower()

if user_choice_str == "rock":
    user_input1 = 0
elif user_choice_str == "paper":
    user_input2= 1
else:
    user_input3 = 2

computer_choice = random.randint(0,2)

if user_input1 == computer_choice or user_input2 == computer_choice or user_input3 == computer_choice:
    print("It's a Tie!")
elif (user_input1 == 0 and computer_choice == 2) or (user_input2 == 1 and computer_choice == 0) or (user_input3 == 2 and computer_choice == 1):
    print("You Win!")
else:
    print("Computer Wins!")
