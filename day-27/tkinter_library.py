# import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack() # this will place the label on the screen and center it.

def button_clicked():
    # print("I got clicked!")s
    text_entry = input.get()
    my_label.config(text = text_entry)

# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry()
input.pack()

window.mainloop()