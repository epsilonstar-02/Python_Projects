from tkinter import *

def con():
    km.config(text=round(float(miles.get())*1.609, 2))

screen = Tk()
screen.title("Miles to Kilometer Converter")
screen.config(padx=10, pady=10)

label = Label(text="is equals to: ")
label.grid(row=1,column=0)

miles = Entry(width=10)
miles.grid(row=0,column=1)

km = Label(text="0")
km.grid(row=1,column=1)

text1 = Label(text="Miles: ")
text1.grid(row=0,column=2)

text2 = Label(text="Kilometres: ")
text2.grid(row=1,column=2)

button = Button(text="Convert", command=con)
button.grid(row=2,column=1)

screen.mainloop()