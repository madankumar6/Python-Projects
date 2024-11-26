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

users_choice= int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"computer chose {computer_choice}")

if users_choice >= 3 or users_choice < 0:
    print("You chose invalid number. You lose!")
elif users_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and users_choice == 2:
    print("You lose!")
elif computer_choice > users_choice:
    print("You lose!")
elif computer_choice < users_choice:
    print("You win!")
elif computer_choice == users_choice:
    print("Its a draw!")
