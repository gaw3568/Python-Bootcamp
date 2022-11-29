from flask import Flask
import random

RANDOM_NUMBER = random.randint(0,9)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess number 0 ~ 9</h1>'\
            '<img src="https://media.giphy.com/media/grDFHLDd6Bl9vDCr4Z/giphy.gif"/>'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess < RANDOM_NUMBER:
        return '<h1>Too low, try again!</h1>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
    elif guess > RANDOM_NUMBER:
        return '<h1>Too high, try again!</h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    else:
        return '<h1>You found me</h1>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'


if __name__ == "__main__":
    app.run()