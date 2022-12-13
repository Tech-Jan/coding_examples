# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def create_pw():
    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    print("Welcome to the PyPassword Generator!")


    nr_letters =random.randint(8,10)
    nr_symbols =3
    nr_numbers =2

    pw_letter = []

    abc= [str(letters[random.randint(0, len(letters) - 1)]) for _ in range(random.randint(8,10))]
    # print(list(pw_letter))
    # for pw_counter in range(0,nr_letters):
    #   pw_letter.append(str(letters[random.randint(0,len(letters)-1)]))
    for pw_counter in range(0, nr_numbers):
        pw_letter.append(str(numbers[random.randint(0, len(numbers) - 1)]))
    for pw_counter in range(0, nr_symbols):
        pw_letter.append(str(symbols[random.randint(0, len(symbols) - 1)]))
    pw_letter = pw_letter+abc
    print(list(pw_letter))


    pw_letter_str = ""
    for sign in pw_letter:
        pw_letter_str += sign
    print(pw_letter_str)

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


    pw_letter_str_random = ""
    i = 0
    for i in range(0, len(pw_letter)):
        length_pw_letter = len(pw_letter) - 1
        position = random.randint(0, length_pw_letter)
        pw_letter_str_random += pw_letter[position]
        pw_letter.remove(pw_letter[position])
        i += 1
    print(pw_letter_str_random)
    return pw_letter_str_random

# ---------------------------- SAVE PASSWORD ------------------------------- #

def genpw():
    mypw=create_pw()
    input_password.delete(first=0, last=END)
    input_password.insert(0,mypw)
    pyperclip.copy(mypw)
def add_click():
    website = input_website.get()
    password = input_password.get()
    email = input_email.get()
    mystring = f"{website} | {email} | {password} \n"
    if messagebox.askokcancel(title=website, message="You wanna add these informations to your file?"):
        save(mystring)
        input_website.delete(first=0, last=END)
        input_password.delete(first=0, last=END)
        # input_email.delete(first=0, last=len(email))


def save(mystring):
    with open("password_generator_list", "a") as f:
        f.write(mystring)


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox

window = Tk()
window.minsize(height=240, width=240)
window.config(pady=20, padx=20)
window.title("Password Generator")

logo_picture = PhotoImage(file="logo.png")
logo = Canvas(height=200, width=200)
logo.create_image(100, 100, image=logo_picture)
logo.grid(row=1, column=2)

label_website = Label(text="Website:")
label_website.grid(row=2, column=1)
label_username = Label(text="Email/Username:")
label_username.grid(row=3, column=1)
label_password = Label(text="Password:")
label_password.grid(row=4, column=1)

input_website = Entry(width=36)
input_website.grid(row=2, column=2, columnspan=2)
input_website.focus()
input_email = Entry(width=36)
input_email.grid(row=3, column=2, columnspan=2)
input_email.insert(0, "Email@hotmail.com")
input_password = Entry(width=20)
input_password.grid(row=4, column=2, rowspan=1)

button_generate_pw = Button(height=1, width=14, text="Generate Password",command=genpw)
button_generate_pw.grid(row=4, column=3)
button_add = Button(height=1, width=36, text="Add", command=add_click)
button_add.grid(row=5, column=2, columnspan=2)

logo.update()
window.mainloop()
