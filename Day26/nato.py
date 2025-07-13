import pandas as pd

df = pd.read_csv("nato_alphabet.csv")

nato = {phonetic.letter:phonetic.code for letter,phonetic in df.iterrows()}

user = input("Enter your name: ").upper()
name = [phonetic for let,phonetic in nato.items() if let in user]
print(name)
