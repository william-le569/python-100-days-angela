from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
# window.minsize(width=250, height=100)

#Labels
label_0 = Label(text="")
label_0.grid(row=0, column=0)
label_0.config(padx=50, pady=0)

#Entries
entry = Entry(width=10)
entry.grid(row=0, column=1)


#Labels
label_1 = Label(text="This is old text")
label_1.config(text="Miles")
label_1.grid(row=0, column=2)

#Labels
label_2 = Label(text="This is old text")
label_2.config(text="is equal to ")
label_2.grid(row=1, column=0)

#Labels
label_3 = Label(text="This is old text")
label_3.config(text="0")
label_3.grid(row=1, column=1)

#Labels
label_4 = Label(text="This is old text")
label_4.config(text=" Km")
label_4.grid(row=1, column=2)

#Buttons
def calculate():
    input_miles = float(entry.get())
    CONVERT_CONST = 1.609344
    output_convert_km = input_miles * CONVERT_CONST
    label_3.config(text=str(output_convert_km))


#calls action() when pressed
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()

