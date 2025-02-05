"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jiri Mastny
email: mastnyj@seznam.cz
"""

import random
import time

# vygeneruje náhodné čtyřmístné číslo s unikátními číslicemi, které nezačíná nulou.
def generate_secret_number():
    digits = list("0123456789")
    while True:
        random.shuffle(digits)
        if digits[0] != '0':
            return "".join(digits[:4])

# ověří, zda jde o validní výběr čísla
def is_valid_guess(guess):
    if len(guess) != 4 or not guess.isdigit():
        return False
    if guess[0] == '0':
        return False
    return len(set(guess)) == 4

# vyhodnotí zvolené číslo
def evaluate_guess(guess, secret):
    bulls = sum(1 for g, s in zip(guess, secret) if g == s)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def main():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret = generate_secret_number()
    print (secret)
    # pro testovací účely "print (secret)""
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number: ")
        if not is_valid_guess(guess):
            print("Invalid input. Please enter a 4-digit number with unique digits that doesn't start with 0.")
            continue

# připočte jeden pokus
        attempts += 1
        bulls, cows = evaluate_guess(guess, secret)

        if bulls == 4:
            end_time = time.time()
            duration = end_time - start_time
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(f"It took you {duration:.2f} seconds.")
            print("-----------------------------------------------")
            print("That's amazing!")
            break
        else:
            print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
            print("-----------------------------------------------")

if __name__ == "__main__":
    main()
