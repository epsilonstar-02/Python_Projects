from tkinter import *
from tkinter import messagebox
import random
import string

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"

# ---------------------------- GENERATE PASSWORD ------------------------------- #

def generate():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    specials = string.punctuation

    let = random.randint(8,10)
    dig = random.randint(2,4)
    sp = random.randint(2,4)

    pass_let = [random.choice(upper + lower) for i in range(let)]
    pass_dig = [random.choice(numbers) for i in range(dig)]
    pass_special = [random.choice(specials) for i in range(sp)]

    pasword = pass_let + pass_dig + pass_special
    random.shuffle(pasword)

    password = "".join(pasword)
    pas1.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = web1.get()
    email = email1.get()
    password = pas1.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            with open("password.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            web1.delete(0, END)
            pas1.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = web1.get()
    if not website:
        messagebox.showinfo(title="Error", message="Please enter the website to search.")
        return
    try:
        with open("password.txt", "r") as file:
            for line in file:
                data = line.strip().split(" | ")
                if data[0].lower() == website.lower():
                    messagebox.showinfo(title=website, message=f"Email: {data[1]}\nPassword: {data[2]}")
                    return
            messagebox.showinfo(title="Not found", message=f"No details for '{website}' exist.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=YELLOW)

img = PhotoImage(file="password.png")
canvas = Canvas(width=512, height=512, bg=YELLOW, highlightthickness=0)
canvas.create_image(256, 256, image=img)
canvas.grid(row=0, column=0, columnspan=3, pady=(0, 20))

# Labels
web = Label(text="Website:", font=(FONT_NAME, 14), bg=YELLOW)
web.grid(row=1, column=0, sticky="e", pady=5)
email = Label(text="Email/Username:", font=(FONT_NAME, 14), bg=YELLOW)
email.grid(row=2, column=0, sticky="e", pady=5)
pas = Label(text="Password:", font=(FONT_NAME, 14), bg=YELLOW)
pas.grid(row=3, column=0, sticky="e", pady=5)

# Entries
web1 = Entry(width=40, font=(FONT_NAME, 13))
web1.grid(row=1, column=1, sticky="w", pady=5, padx=(0, 10))
web1.focus()
search_btn = Button(text="Search", width=14, command=find_password, bg=RED, font=(FONT_NAME, 11))
search_btn.grid(row=1, column=2, sticky="w", padx=(0, 30))
email1 = Entry(width=40, font=(FONT_NAME, 13))
email1.grid(row=2, column=1, columnspan=2, sticky="w", pady=5, padx=(0, 30))
email1.insert(0, "user@email.com")
pas1 = Entry(width=24, font=(FONT_NAME, 13))
pas1.grid(row=3, column=1, sticky="w", pady=5, padx=(0, 10))

# Buttons
gen_btn = Button(text="Generate Password",command=generate, bg=GREEN, font=(FONT_NAME, 11), width=18)
gen_btn.grid(row=3, column=2, sticky="w", pady=5, padx=(0, 30))
save_btn = Button(text="Add", width=44, command=save_password, bg=PINK, font=(FONT_NAME, 13))
save_btn.grid(row=4, column=0, columnspan=3, pady=(18, 0))

window.mainloop()