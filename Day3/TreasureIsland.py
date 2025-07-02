print("Welcome to Treasure Island!")
print("Your mission is to find the treasure")
dec = input("Do you want to go left or right? ")
if dec.lower() == "right":
    print("Game Over!")
else:
    dec = input("Do you want to swim or wait? ")
    if dec.lower() == "swim":
        print("Game Over")
    else:
        dec = input("Which door do you want to choose?(Red, Blue, or Yellow) ")
        if dec.lower() == "yellow":
            print("You win!")
        else:
            print("Game Over!")