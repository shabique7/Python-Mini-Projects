import random
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
game_image=[rock,paper,scissors]
user_choice=int(input("What will you choose?Type 0 for rock,1 for paper,2 for scissors\n"))
print("You Choose\n")
print(game_image[user_choice])
computer_input=random.randint(0,2)
print("Computer Choose\n")
print(game_image[computer_input])
if user_choice==0 and computer_input==1:
    print("You Lose!!")
elif user_choice==0 and computer_input==2:
    print("You Win!!")
elif user_choice==1 and computer_input==0:
    print("You Win!!")
elif user_choice==1 and computer_input==2:
    print("You Lose!!")
elif user_choice==2 and computer_input==0:
    print("You Lose!!")
elif user_choice==2 and computer_input==1:
    print("You Win!!")
elif user_choice ==  computer_input:
    print("It is a Draw!!")
else:
    print("You printed invalid number")
