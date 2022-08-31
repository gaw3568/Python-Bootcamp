# 가위바위보 게임
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
# 바위 : 0  보 : 1  가위 : 2
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
r_p_s = [rock,paper,scissors]
if choice >= 3 or choice < 0 :
    print("Error")
else:
    print(r_p_s[choice])

    computer_choice = random.randint(0,2)
    print("Computer Choice:")
    print(r_p_s[computer_choice])

    if choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and choice == 2:
        print("You lose")
    elif computer_choice > choice:
        print("You lose")
    elif choice > computer_choice:
        print("you win")
    elif choice == computer_choice:
        print("It is draw")
