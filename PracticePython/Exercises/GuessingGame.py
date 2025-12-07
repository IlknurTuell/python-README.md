#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

while True:
    number = random.randint(1,9)

    guess=None
    guess_number = 1
    
    while True:
        guess = int(input("Your guess: "))
        if guess > number:
            print("Your guess is to high! Guess again.")
            guess_number += 1
        if guess < number:
            print("Your guess is to low! Guess again.")
            guess_number += 1
        if guess==number:
            print(f"You've guessed number!")
            break
    if input("Do you want play again?(Y/N): ")== "N":
        break