# Importing libraries
import random

guess = input("Enter your Guess...(Heads or Tails)")
guess = guess.lower()
options = ['Heads', 'Tails']

# choosing a ramdom index.
guess_int = random.randint(0, 1)

# Display the computer choosen side.
print(f"Flipped side is {options[guess_int]}")

if options[guess_int] == guess:
    print("you Won")
else:
    print("You Lose")
