import random
import string
num = list(range(0,10))
letters = list(string.ascii_letters)
symbols = list(string.punctuation)

n = int(input("Enter no of numbers: "))
l = int(input("Enter no of letters: "))
s = int(input("Enter no of symbols: "))

password = []
for i in range(0,n+1):
    password.append(random.choice(num))
for i in range(0,l+1):
    password.append(random.choice(letters))
for i in range(0,s+1):
    password.append(random.choice(symbols))

random.shuffle(password)
print(''.join(map(str, password)))