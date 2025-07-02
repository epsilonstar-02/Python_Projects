import random


choice = int(input("Enter your choice(0 for Rock, 1 for Paper, 2 for Scissors): "))
comp = random.randint(0,2)
print(f"Computer chooses: {comp}")

if choice == comp:
    print("Draw!")
elif (choice == 0 and comp == 2) or (choice == 1 and comp == 0) or (choice == 2 and comp == 1):
    print("You win!")
else:
    print("Comp wins!")