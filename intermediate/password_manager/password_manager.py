from tkinter import *
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="intermediate/password_manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="white", fg="black")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:",bg="white", fg="black")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="white", fg="black")
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=35, highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2)
email_username_entry = Entry(width=35, highlightthickness=0)
email_username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=20, highlightthickness=0)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=11, highlightbackground="white")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33, highlightbackground="white")
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()