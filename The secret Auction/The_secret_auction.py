from replit import clear
import random

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bid_value = {}
print(logo)
print("Welcome to the Secret Auction...")



def protocol():
    in_name = input("What is your name?\n")
    value = int(input("Enter your bid:\n"))
    bid_value[in_name] = value


protocol()
highest = 0
ask = input("Is there any other bidder\n")

while ask == "yes":
    clear()
    protocol()
    ask = input("Is there any other bidder\n")

clear()
print(f"{logo}   {logo}")
for name in bid_value:
    if bid_value[name] >= highest:
        highest = bid_value[name]
for name in bid_value:
    if highest == bid_value[name]:
        print(f"The winner is '{name}' with highest bid of {highest}")
