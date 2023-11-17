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

choices = [rock, paper, scissors]
chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(choices[chose])

cpu_choice = random.randint(0, 2)
print("\nComputer's choice")
if cpu_choice == 0:
    print(rock)
elif cpu_choice == 1:
    print(paper)
else:
    print(scissors)

if cpu_choice == chose:
    print("It's a draw!")
elif cpu_choice == 0 and chose == 1:
    print("You won!")
elif cpu_choice == 0 and chose == 2:
    print("You lost!")
elif cpu_choice == 1 and chose == 0:
    print("You lost!")
elif cpu_choice == 1 and chose == 2:
    print("You won!")
elif cpu_choice == 2 and chose == 0:
    print("You won!")
elif cpu_choice == 2 and chose == 1:
    print("You lost!")
  