import random

def hit(you, dealer):
    yourcard = random.choice(cards)
    you.append(yourcard)
    if yourcard == 11 and sum(you) > 21:
        you[-1] = 1
    print(f"You drew: {yourcard}")
    print(f"Your hand: {you} (Total: {sum(you)})")
    if sum(you) > 21:
        print("You busted! Your total is over 21.")
        return False
    else:
        return True

def blackjack(you, dealer):
    yourhand = sum(you)
    dealerhand = sum(dealer)
    print(f"Dealer reveals hand: {dealer} (Total: {dealerhand})")
    while dealerhand < 17:
        print(f"Dealer's hand: {dealer} (Total: {dealerhand}). Dealer picks another card...")
        card = random.choice(cards)
        if card == 11 and sum(dealer) + 11 > 21:
            card = 1
        dealer.append(card)
        dealerhand = sum(dealer)
        print(f"Dealer drew: {card}")
    print(f"Dealer's final hand: {dealer} (Total: {dealerhand})")
    if dealerhand > 21:
        print("Dealer busted! Dealer's total is over 21.")
        return True
    elif dealerhand > yourhand:
        print("Dealer wins with a higher hand!")
        return False
    elif dealerhand == yourhand:
        print("It's a draw!")
        return None
    else:
        print("You win with a higher hand!")
        return True


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
you = []
dealer = []
print("\n==============================")
print("  Welcome to the BlackJack Game!!!  ")
print("==============================\n")
you.append(random.choice(cards))
you.append(random.choice(cards))
dealer.append(random.choice(cards))
dealer.append(random.choice(cards))
print(f"Your hand: {you} (Total: {sum(you)})")
print(f"Dealer's visible card: {dealer[0]}")

busted = False
while True:
    choice = input("Do you want to hit or stand? (h/s): ").lower()
    if choice == 'h':
        if not hit(you, dealer):
            print(f"Dealer's hand: {dealer} (Total: {sum(dealer)})")
            print("You LOSE!")
            busted = True
            break
    elif choice == 's':
        break
    else:
        print("Invalid input. Please enter 'h' to hit or 's' to stand.")

if not busted:
    result = blackjack(you, dealer)
    print(f"\nYour final hand: {you} (Total: {sum(you)})")
    print(f"Dealer's final hand: {dealer} (Total: {sum(dealer)})")
    if result is True:
        print("You WIN!")
    elif result is False:
        print("You LOSE!")
    else:
        print("It's a DRAW!")