from mimetypes import guess_extension
import random
from Guess_the_number_Art import logo

def func_1():
    return
def func_2():
    return
def func_3():
    return


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

guess_number = random.randint(1,100)
print(f"guess number : {guess_number}")

if level == 'easy':
    chance = 10
elif level == 'hard':
    chance = 5

isGameEnd = False

while not isGameEnd:
    print(f"You have {chance} attempts remaining to guess the number")
    number = int(input("Make a guess: "))

    if number == guess_number:
        print("It is correct")
        isGameEnd = True
    elif number > guess_number:
        print("Too high.")
        print("Guess Again.")
        chance -= 1
    elif number < guess_number:
        print("Too low.")
        print("Guess Again.")
        chance -= 1
    
    if chance == 0:
        print("You lose")
        isGameEnd = True