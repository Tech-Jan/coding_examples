# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.minsize(height=240, width=240)
window.config(pady=20, padx=20)
window.title("Password Generator")

logo_picture = PhotoImage("logo.png")
logo = Canvas(height=200, width=200,bg="grey")
logo.create_image(100, 100, image=logo_picture)
logo.grid(row=2, column=2)
window.update()
window.mainloop()
