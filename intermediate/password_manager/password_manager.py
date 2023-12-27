from tkinter import *
from tkinter import messagebox
import random
import json
from password_generator import generate_new_password
# ---------------------------- SEARCH ------------------------------------------- #
def search_info():
    """Searches the json data for given website entry. If website can be found, prints the informations
    of target website.
    If website cannot be found, shows a error in screen.
    """
    website = website_entry.get()
    try:
        with open("/Users/kyotun/Desktop/python/intermediate/password_manager/data.json", mode="r") as file:
            # Load the existed json data.
            loaded_json_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="File Error", message="No Data File Found")
    else:
        if website in loaded_json_data:
            password = loaded_json_data[website]["password"]
            email = loaded_json_data[website]["email"]
            messagebox.showinfo(title=f"Requested Informations",
                                message=f"Website: {website} \nEmail: {email} \nPassword: {password}")
        else:
            messagebox.showerror(title="Key Error", message=f"There is no key such '{website}'")
            
                    
                    
    
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Delete the characters in password field.
    Generate password and put the generated password in password field.
    """
    password_entry.delete(0,END)
    generated_password = generate_new_password()
    password_entry.insert(0, generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Gets the input email, password and website. Convert them into dict format.
    Controls the length of given inputs, if lengths are not bigger than 1, shows warning in screen.
    If there is nothing against rules, saves the given input password, email and website to json data.
    Deletes the characters from the fields.
    At the end, focuses the cursor to website field.
    """
    email = email_username_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    
    new_data_to_dump = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(email) <= 1 or len(website) <= 1 or len(password) <=1:
        messagebox.showwarning(title="Missing Information!", message="Length of any kind of information cannot be shorter than 2 characters.")
    else:
        answer = messagebox.askokcancel(title="Information!", message=f"""Details entered:
                            \nEmail: {email} 
                            \nPassword: {password} 
                            \nWebsite: {website}""")
        if answer:
            try:
                with open("/Users/kyotun/Desktop/python/intermediate/password_manager/data.json", mode="r") as file:
                    # Load the existed json data.
                    loaded_json_data = json.load(file) # Loading a json file. (It will be loaded as dict)
            except FileNotFoundError:
                with open("/Users/kyotun/Desktop/python/intermediate/password_manager/data.json", mode="w") as file:
                    # Dump the updated data to the same/different json data.
                    json.dump(new_data_to_dump, file, indent=4)
                    file.close()
            else:
                # Update the json data with the given inputs from the user.
                loaded_json_data.update(new_data_to_dump)
                file.close()
                
                # Open the json data with write mode and dump the updated data.
                with open("/Users/kyotun/Desktop/python/intermediate/password_manager/data.json", mode="w") as file:
                    json.dump(loaded_json_data, file, indent=4)
                    file.close()
            finally:
                website_entry.delete(0,END)
                email_username_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()
                messagebox.showinfo(title="Confirmation", message="Informations are saved!")
        else:
            messagebox.showinfo(title="Acknowledgement", message="Informations are not saved.")
# ---------------------------- UI SETUP ------------------------------- #
# Create the windows and setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# Create canvas for photo of lock
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="/Users/kyotun/Desktop/python/intermediate/password_manager/logo.png")
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
website_entry = Entry(width=20, highlightthickness=0)
website_entry.focus()
website_entry.insert(END, "Amazon")
website_entry.grid(row=1, column=1)
email_username_entry = Entry(width=35, highlightthickness=0)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "example@gmail.com")
password_entry = Entry(width=20, highlightthickness=0)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=11, highlightbackground="white", command=search_info)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", width=11, highlightbackground="white", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33, highlightbackground="white", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()