import random

def guess():
    n = int(input("Your guess: "))
    if n > NUM:
        print("Too high!")
        return False
    elif n < NUM:
        print("Too Low!")
        return False
    elif n == NUM:
        return True
    else:
        print("Invalid Guess!!")
        return False

print("Welcome to the Guessing Game!!!")
NUM = random.randint(1,100)
print("I'm thinking of a number between 1 and 100. Can you guess the number?")
mode = input("Choose difficulty - Easy or Hard: ").lower()
if mode == 'easy':
    attempts = 10
elif mode == 'hard':
    attempts = 5
else:
    print("Invalid Input!!")

while attempts > 0:
    status = guess()
    if status == True:
        print("You guessed right!!")
        break
    attempts -= 1
    print(f"Attempts Remaining: {attempts}")

if attempts == 0:
    print("You LOSE!!")