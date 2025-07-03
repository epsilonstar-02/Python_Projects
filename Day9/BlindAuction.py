import os
auction = {}
flag = 'y'
while flag == 'y':
    name = input("What's your name? ")
    auction[name] = int(input("Enter bid amount: $"))
    flag = input("Are there other bidders too?(Y/N): ").lower()
    os.system('cls')

os.system('cls')
winner = max(auction, key=auction.get)
print(f"The winner is {winner}. Bid amount: ${max(auction.values())}")