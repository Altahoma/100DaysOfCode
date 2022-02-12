from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# PASSWORD GENERATOR
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_number
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# SAVE PASSWORD
def save_log_pass():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please don\'t leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\n'
                                                              f'Email: {email}\n'
                                                              f'Password: {password}\n'
                                                              f'Is it ok to save?')
        if is_ok:
            with open('data.txt', 'a') as file:
                new_line = f'{website} / {email} / {password}\n'
                file.write(new_line)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# UI Setup
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'example@mail.com')
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text='Generate', command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text='Add', command=save_log_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
