from tkinter import *
# Program to convert miles to kilometer


def calculate_km():
    """Take input from user as mile. Multiply it by 1.609 and shows the result in km field.
    """
    mile = float(input.get())
    km = mile * 1.609
    number.config(text=f"{round(km,2)}")
    
# Setup the window 
windows = Tk()
windows.title("Miles/Kilometer Converter")
windows.minsize(width=200, height=100)
windows.config(padx=20, pady=10)

# Label
equal_to = Label(text="is equal to", font=("Arial", 12))
equal_to.grid(row=1, column=0)

number = Label(text="", font=("Arial", 12))
number.grid(row=1, column=1)

km = Label(text="Km", font=("Arial", 12))
km.grid(row=1, column=2)

mile = Label(text="Miles", font=("Arial", 12))
mile.grid(row=0, column=2)


# Button
my_button = Button(text="Calculate", command=calculate_km, width=4)
my_button.grid(row=2, column=1)

# Entry
input = Entry(width=7)
input.grid(row=0, column=1)
windows.mainloop()
