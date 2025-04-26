from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#---------------PASSWORD GENERATOR---------------------#
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list  = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

#------------------------------------------------------

#---------------------SAVE PASSWORD -------------------
def check_empty(website_data, username_data, password_data):
    if website_data == "":
        messagebox.showinfo(title="Notification", message="You have not entered website!")
        return True
    elif username_data == "":
        messagebox.showinfo(title="Notification", message="You have not entered username/email!") 
        return True 
    elif password_data == "":
        messagebox.showinfo(title="Notification", message="You have not entered password!") 
        return True
    else:
        return False

def save():
    website_data = website_entry.get()
    username_data = username_entry.get()
    password_data = password_entry.get()

    check_empty_flag = check_empty(website_data, username_data, password_data)

    if check_empty_flag == False:
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered:\nEmail: {username_data}"
                                                                    f"\nPassword: {password_data} \nIs it ok to save?")
        if is_ok:
            new_data = f"{website_data} | {username_data} | {password_data}"

            with open('data.txt') as file:
                saved_data = file.readlines()

            if new_data + "\n" not in saved_data:
                messagebox.showinfo(title="Notification", message="Data is saved!")
                with open("data.txt", mode="a") as file:
                    file.write(new_data + '\n')
            
            website_entry.delete(0, END)
            # username_entry.delete(0, END)
            password_entry.delete(0, END)

            website_entry.focus()

#------------------------------------------------------#

#---------------------UI SET-UP--===-------------------#
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
# Change type to PhotoImage because create_image requires a PhotoImage object.
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky='snew')
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky='snew')
username_entry.insert(0, "thieu.le569@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='snew')

# Buttons
save_button = Button(text="Add", command=save,width=36, highlightthickness=0)
save_button.grid(row=4, column=1, columnspan=2, sticky='snew')

generate_password_button = Button(text="Generate Password", command=generate_password,width=14, highlightthickness=0)
generate_password_button.grid(row=3, column=2, sticky='snew' )

#------------------------------------------------------#

window.mainloop()