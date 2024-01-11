import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '$', '%', '&', '*']

print("Welcome to the Password Generator!")
alpha = int(input("Enter the number of alphabets you want:"))
sym = int(input("Enter the number of symbot you want:"))
num = int(input("Enter the number you want:"))

raw_password = []
for i in range(0, alpha):
    raw_password += alphabets[random.randint(0, 51)]
for i in range(0, sym):
    raw_password += symbols[random.randint(0, 5)]
for i in range(0, num):
    raw_password += str(numbers[random.randint(0, 9)])
random.shuffle(raw_password)
password = ""
for char in raw_password:
    password += char
print(password)
