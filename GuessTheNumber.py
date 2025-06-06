import random
import time
import inputimeout
from inputimeout import inputimeout
from inputimeout import TimeoutOccurred
# Everything below this is the game. Everything above is the imports and the inputimeout class.
print("Loading the game...")
time.sleep(2)
print("Welcome to the Guess the Number Game made by Me!")
time.sleep(1)
while True:
    print("Guess What Number I'm thinking of.")
    random_number = random.randint(1, 10)
    time.sleep(1)
    try:
        print("You have 10 seconds to guess the number between 1-10!")
        try:
            number = int(inputimeout(prompt="Enter your guess: ", timeout=10)) 
        except TimeoutOccurred:
            print("You ran out of time! Exiting the game.")
            time.sleep(2)
            break
    except ValueError:
        print("Please enter a valid number between 1 and 10.")
        time.sleep(1)
        clear = input("Press Enter to continue...")
        if clear == "":
            print("Continuing...")
        else:
            print("Invalid input, continuing anyway.")
        time.sleep(1)
        continue
    if number == random_number:
        print("Correct! You guessed the number.")
    else:
        print(f"Wrong! The number was {random_number}.")

    time.sleep(2)
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    time.sleep(1)
    if play_again == "yes":
        continue
    else:
        print("Goodbye! Thanks for playing.")
        break
exit