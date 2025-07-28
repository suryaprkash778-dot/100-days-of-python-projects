rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("WELCOME TO THE ROCK , PAPER AND SCISSORS GAME")
user_choice=int(input("What do you choose? Type 0 for Rock, "
            "1 for Paper and 2 for Scissors\n"))
import random
computer_choice=random.randint(0,2)

game=[rock,paper,scissors]
if user_choice>=0 and user_choice<=2:
    print(game[user_choice])
print("computer chose :")
print(game[computer_choice])
if user_choice>=3 or user_choice<0:
    print("you typed an invalid number. you lose")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif user_choice==2 and computer_choice==0:
    print("you lose")
elif user_choice < computer_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win")
elif user_choice == computer_choice:
    print("its a draw")
