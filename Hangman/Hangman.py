# Importing libraries and art file
import random
from art import stages

failed = 6   # Number of chances ... Must be equal to the stages in art file 
wordlist = ['apple', 'banana', 'cucumber']   # Words to guess

# Using random module to choose a word for wordlist
chosen_word = wordlist[random.randint(0, 2)]

display = []
for i in range(0, len(chosen_word)):
    display += "_"    # To create empty spaces 
    
print(display)

# end_of_game = False

while "_" in display:
    guess = input("Enter your guess:").lower()
    for letter in range(0, len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess

    if guess not in display:
        print(stages[failed])
        if failed == 0:
            break
        failed -= 1
    print(display)

if "_" in display:
    print("You Lose!")
else:
    print("You Won!!!")
