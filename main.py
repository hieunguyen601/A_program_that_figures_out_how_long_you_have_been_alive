from art import logo
print(logo)

winner = ""
bids = {}

name = input("What is your name? ")
price = int(input("What is the price? "))
bids[name] = price
more_user = input("Are there any users? Type 'yes' or 'no': ")
should_continue = True

while should_continue: