from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ========== RANDOM PASSWORD ========== #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_letters = [choice(letters) for char in range(randint(8, 10))]
    rand_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    rand_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = rand_letters + rand_symbols + rand_numbers
    shuffle(password_list)

    random_password = "".join(password_list)

    password_field.delete(0, END)
    password_field.insert(0, random_password)
    pyperclip.copy(random_password)


# ========== SAVE DATA ========== #

def write_data():
    website_name = website_field.get().title()
    email_username = email_user_field.get()
    site_password = password_field.get()
    new_data = {
        website_name: {
            "email": email_username,
            "password": site_password
        }
    }

    if len(website_name) == 0 or len(site_password) == 0:
        messagebox.showinfo(title="Error", message="Please fill in the fields before saving!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_field.delete(0, END)
            password_field.delete(0, END)


# ========== SEARCH DATA ========== #

def search():
    query = website_field.get().title()
    if len(query) == 0:
        messagebox.showinfo(title="Field Empty", message="Please fill in the field before searching!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found.")
        else:
            if query in data:
                messagebox.showinfo(title=query, message=f"Email/Username: {data[query]["email"]}\n"
                                                         f"Password: {data[query]["password"]}")
            else:
                messagebox.showinfo(title="Error", message="No credentials found.\n\nPlease check spelling or type the "
                                                           "full entry name if this is a mistake.")


# ========== UI SETUP ========== #

# Window
window = Tk()
window.title("MyPass")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1, sticky=E)

email_user = Label(text="Email/Username:")
email_user.grid(column=0, row=2, sticky=E)

password = Label(text="Password:")
password.grid(column=0, row=3, sticky=E)

# Entry Fields
website_field = Entry(width=24)
website_field.grid(column=1, row=1, columnspan=2, sticky=W)
website_field.focus()

email_user_field = Entry(width=41)
email_user_field.grid(column=1, row=2, columnspan=2, sticky=W)
email_user_field.insert(END, "placeholder text")

password_field = Entry(width=24)
password_field.grid(column=1, row=3, sticky=W)

# Buttons
search_button = Button(text="Search", width=13, command=search)
search_button.grid(column=2, row=1)

password_button = Button(text="Generate Password", width=13, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=write_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
