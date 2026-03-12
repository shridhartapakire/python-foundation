# number_guessing_game.py
# Mini Project: Number Guessing Game

import random

# Generate a random number
secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("Correct! You guessed the number.")
        print("Total attempts:", attempts)
        break

    elif guess < secret_number:
        print("Too low! Try a higher number.")

    else:
        print("Too high! Try a lower number.")
