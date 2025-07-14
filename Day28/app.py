from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_state = "work"
window = Tk()
window.config(padx=20, pady=20, bg=YELLOW)
window.title("Pomodoro")

label = Label(text="Pomodoro Timer", font=(FONT_NAME, 48, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

canvas = Canvas(width=640, height=640, background=YELLOW)
img = PhotoImage(file="tomato.png")
canvas.create_image(320,320, image=img)
canvas.grid(row=1, column=1)
start_button = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 16, "bold"), command=lambda: start_timer())
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 16, "bold"), command=lambda: reset_timer())
reset_button.grid(row=2, column=2)

tick_label = Label(text="", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)

reps = 0

def update_timer_label(text, color):
    label.config(text=text, fg=color)

def update_timer_text(minutes, seconds):
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

def update_tick_label(ticks):
    tick_label.config(text=ticks)

def reset_ui():
    update_timer_text(0, 0)
    update_timer_label("Pomodoro Timer", GREEN)
    update_tick_label("")

def reset_timer():
    if hasattr(window, "after_id"):
        window.after_cancel(window.after_id)
    reset_ui()
    global reps
    reps = 0
    global timer_state
    timer_state = "work"

def start_next_timer():
    global timer_state
    if timer_state == "work":
        timer_state = "short_break"
        update_timer_label("Short Break", PINK)
        countdown(SHORT_BREAK_MIN * 60)
    elif timer_state == "short_break":
        timer_state = "work"
        update_timer_label("Work", GREEN)
        countdown(WORK_MIN * 60)
    elif timer_state == "long_break":
        timer_state = "work"
        update_timer_label("Work", GREEN)
        countdown(WORK_MIN * 60)

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count = LONG_BREAK_MIN * 60
        update_timer_label("Long Break", RED)
        global timer_state
        timer_state = "long_break"
    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN * 60
        update_timer_label("Short Break", PINK)
        timer_state = "short_break"
    else:
        count = WORK_MIN * 60
        update_timer_label("Work", GREEN)
        timer_state = "work"
    countdown(count)

def countdown(count):
    minutes = count // 60
    seconds = count % 60
    update_timer_text(minutes, seconds)
    if count > 0:
        window.after_id = window.after(1000, countdown, count - 1)
    else:
        if timer_state == "work":
            marks = "✔" * (reps // 2)
            update_tick_label(marks)
        start_timer()

timer_text = canvas.create_text(320, 350, text="00:00", font=(FONT_NAME, 48, "bold"), fill="White")
window.mainloop()