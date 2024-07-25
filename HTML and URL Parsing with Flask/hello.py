from flask import Flask
import random

app = Flask(__name__)

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)

@app.route('/')
def home():
    return '''
        <h1 style="color: purple; text-align: center;">Guess a number between 0 and 9</h1>
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Thinking gif" style="display: block; margin: auto;">
    '''

@app.route('/<int:guess>')
def check_guess(guess):
    if guess < random_number:
        return '''
            <h1 style="color: blue; text-align: center;">''' + str(guess) + ''' is too low!</h1>
            <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Too low gif" style="display: block; margin: auto;">
        '''
    elif guess > random_number:
        return '''
            <h1 style="color: red; text-align: center;">''' + str(guess) + ''' is too high!</h1>
            <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Too high gif" style="display: block; margin: auto;">
        '''
    else:
        return '''
            <h1 style="color: green; text-align: center;">''' + str(guess) + ''' is correct!</h1>
            <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Correct guess gif" style="display: block; margin: auto;">
        '''

if __name__ == "__main__":
    app.run(debug=True)