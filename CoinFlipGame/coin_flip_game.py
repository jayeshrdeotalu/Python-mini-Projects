import random
guess = input("Enter your Guess")
guess_int = random.randint(0, 1)
options = ['Heads', 'Tails']
print(f"Flipped side is {options[guess_int]}")
if options[guess_int] == guess:
    print("you Won")
else:
    print("You Lose")
