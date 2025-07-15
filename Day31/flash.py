from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

if os.path.exists("./data/words_to_learn.csv"):
    DATA = pd.read_csv("./data/words_to_learn.csv")
else:
    DATA = pd.read_csv("./data/french_words.csv")
learn = DATA.to_dict(orient="records")
current_card = {}
flip_timer = None

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = random.choice(learn)
    canvas.itemconfig("title", text="French", fill="black")
    canvas.itemconfig("word", text=current_card["French"], fill="black")
    canvas.itemconfig(card_img, image=front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig("title", text="English", fill="white")
    canvas.itemconfig("word", text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=back)

def remove_known_word():
    global learn
    learn.remove(current_card)
    pd.DataFrame(learn).to_csv("./data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(400, 526/2, image=front)
canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black", tags="title")
canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black", tags="word")
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=remove_known_word)
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=next_card)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

def save_progress():
    pd.DataFrame(learn).to_csv("./data/words_to_learn.csv", index=False)
    window.destroy()
window.protocol("WM_DELETE_WINDOW", save_progress)

next_card()

window.mainloop()