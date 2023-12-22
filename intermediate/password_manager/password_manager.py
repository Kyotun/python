from tkinter import *
from tkinter import messagebox
import random
from password_generator import generate_new_password
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    generated_password = generate_new_password()
    password_entry.insert(0, generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_username_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    
    if len(email) or len(website) or len(website) <=1:
        messagebox.showwarning(title="Missing Information!", message="Length of any kind of information cannot be shorter than 2 characters.")
    else:
        answer = messagebox.askokcancel(title="Information!", message=f"""Details entered:
                            \nEmail: {email} 
                            \nPassword: {password} 
                            \nWebsite: {website}""")
        if answer:
            with open("intermediate/password_manager/data.txt", mode="a") as file:
                file.write(f"{website_entry.get()} -- {email_username_entry.get()} -- {password_entry.get()}\n")
                website_entry.delete(0,END)
                email_username_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()
                messagebox.showinfo(title="Confirmation", message="Informations are saved!")
                file.close()
        else:
            messagebox.showinfo(title="Acknowledgement", message="Informations are not saved.")
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
website_entry.focus()
website_entry.insert(END, "Amazon")
website_entry.grid(row=1, column=1, columnspan=2)
email_username_entry = Entry(width=35, highlightthickness=0)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "example@gmail.com")
password_entry = Entry(width=20, highlightthickness=0)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=11, highlightbackground="white", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33, highlightbackground="white", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()