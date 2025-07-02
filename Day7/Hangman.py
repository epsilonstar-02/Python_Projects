import random
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

words = ["Mouse", "Horse", "Baboon", "Giraffe", "Cheetah"]

word = random.choice(words).lower()
lives = len(hangman_stages) - 1
blanks = len(word)
wrd = list("_" * blanks)

print("Welcome to Hangman!")
print(hangman_stages[0])

while blanks > 0 and lives > 0:
    print(' '.join(wrd))
    guess = input("Guess a letter: ").lower()
    if guess in word:
        print("Right Guess!")
        occurrences = 0
        for i in range(len(word)):
            if word[i] == guess:
                wrd[i] = guess
                occurrences += 1
        blanks -= occurrences
    else:
        print("Wrong Guess!")
        lives -= 1
        print(hangman_stages[len(hangman_stages) - lives - 1])

if lives == 0:
    print("You lose!")
    print(f"The word was: {word}")
else:
    print("You win!")
    print(f"The word was: {word}")