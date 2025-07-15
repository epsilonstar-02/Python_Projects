import pandas as pd

df = pd.read_csv("nato_alphabet.csv")

nato = {phonetic.letter:phonetic.code for letter,phonetic in df.iterrows()}

on = True
while on:
    try:
        user = input("Enter your name: ").upper()
        name = [nato[let] for let in user]
    except KeyError:
        print("Enter a valid name.")
        continue
    else:
        on = False


print(name)
