import random
from Hangman_Picture import logo, stages
import Hangman_Words

print(logo)

chosen_word = random.choice(Hangman_Words.word_list)
lives = len(stages) - 1

display = []
chosen_word_len = len(chosen_word)

for index in range(chosen_word_len):
    display.append("_")

isCorrect = False

while not isCorrect:
    guess = input("Guess a letter : ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for index in range(chosen_word_len):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = letter
    print(f"{' '.join(display)}")
            
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives <= 0:
            isCorrect = True
            print("You lose.")

    if not "_" in display:
        isCorrect = True
        print("You win")

    print(stages[lives])
