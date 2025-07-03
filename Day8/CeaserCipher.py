def encrypt(msg, shift):
    cipher = ''
    for i in msg:
        if i.islower():
            cipher += chr(((ord(i) + shift- ord('a'))%26 + ord('a')))
        elif i.isupper():
            cipher += chr(((ord(i) + shift- ord('A'))%26 + ord('A')))
        else:
            cipher += i
    print(f"{cipher}")

def decrypt(msg, shift):
    cipher = ''
    for i in msg:
        if i.islower():
            cipher += chr(((ord(i) - shift- ord('a'))%26 + ord('a')))
        elif i.isupper():
            cipher += chr(((ord(i) - shift- ord('A'))%26 + ord('A')))
        else:
            cipher += i
    print(f"{cipher}")
    
choice = input("Encode or Decode? ").lower()
msg = input("Enter your message: ")
shift = int(input("Enter shift: "))
if choice == "encode":
    encrypt(msg,shift)
elif choice == "decode":
    decrypt(msg,shift)