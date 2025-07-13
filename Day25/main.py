import pandas as pd
from turtle import Screen
from timmy import State

screen = Screen()
screen.setup(width=500, height=386)
screen.bgpic("states_map.gif")
screen.title("US States Quiz Game")
data = pd.read_csv("50_states.csv")
states = list(data['state'])
guessed_states = []

while len(guessed_states) < len(states):
    guess = screen.textinput(f"{len(guessed_states)}/50 States Correct", "Enter state name (or 'quit' to exit): ")
    if not guess:
        continue
    guess = guess.title()
    if guess == "Quit":
        break
    if guess in states and guess not in guessed_states:
        pos = data[data['state'] == guess]
        x = int(pos.x)
        y = int(pos.y)
        State(guess, x, y)
        guessed_states.append(guess)
    else:
        screen.textinput("Incorrect", f"{guess} is not a valid state or already guessed. Press Enter to continue.")

missed_states = [state for state in states if state not in guessed_states]
if missed_states:
    pd.DataFrame(missed_states, columns=["Missed States"]).to_csv("missed_states.csv", index=False)

screen.exitonclick()