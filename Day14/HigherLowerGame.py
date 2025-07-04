from data import data
import os

print("Welcome to the Higher Lower Game!!!")
n = len(data)
SCORE = 0
for i in range(1,n):
    A = data[i-1]
    B = data[i]
    if A['follower_count'] > B['follower_count']:
        gr = 'A'
    else:
        gr = 'B'
    print(f"Your Score: {SCORE}")
    print("Who has more followers on Instagram?")
    print(f"A: {A['name']}, {A['description']}, {A['country']}")
    print("VS")
    print(f"B: {B['name']}, {B['description']}, {B['country']}")
    
    guess = input("Your guess(A or B): ").upper()
    if guess == gr:
        SCORE += 1
        print("Correct!!!")
        os.system('cls')
    else:
        print("Wrong!!")
        print("GAME OVER!!!")
        print(f"Your score: {SCORE}")
        break