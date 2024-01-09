from logo import logo



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']


print(logo)
direction = input("Type 'Incode' or 'Decode'\n").lower()
text = input("Enter your text here:\n").lower()
shift = int(input("Enter the swift you want:\n"))


def caesar(given_text, told_shift, cipher):
    new_text = ""
    for letter in given_text:
        if letter not in alphabet:
            new_text += letter
            continue
        elif cipher == "incode":
            index = alphabet.index(letter) + told_shift
            if index > 25:
                index -= 26
        else:
            index = alphabet.index(letter) - told_shift
            if index < 0:
                index += 25
        new_text += alphabet[index]
    print(f"Here is the {cipher} result: {new_text}")


caesar(text, shift, direction)
