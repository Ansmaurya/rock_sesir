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

#Write your code below this line 👇
game_images=[rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice>=3 or user_choice<0:
  print("this is a inviled number")
else:
  print(game_images[user_choice])
computer_choice=random.randint(0, 2)
print(f"computer choose {computer_choice} !")
print(game_images[computer_choice])
if computer_choice==0 and user_choice==2:
  print("you Win!")
# if computer_choice==2 and user_choice==0:
#   print("you Win!")
elif computer_choice > user_choice:
  print("You loss!")
elif computer_choice < user_choice:
  print("You win!")
elif computer_choice==user_choice:
  print("it's a draw!")
