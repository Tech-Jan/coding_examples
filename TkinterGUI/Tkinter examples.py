from tkinter import *
import time


# *args and **kwargs
def add(*args):
    sum = 0
    for number in args:
        sum += number
        print(sum)
    print(sorted(set(args)))


add(1, 3, 65, 6, 3, 2, 3, 23)


def test(n, **kw):
    print(kw)
    n += kw["number"]
    print(n)


test(2, non="aka", number=45)

# Window
window = Tk()
window.title("my first Tinka app")
window.minsize(width=500, height=300)

# Label
mylabel = Label(text="My First Label", font=("Arial", 22))
# pack puts the label on screen
mylabel.pack(anchor="center")


def buttonclick():
    myinputtext = myinput.get()
    mylabel.config(text=myinputtext)

    print(myinputtext)
    print("ABBVC")


# Button
mybutton = Button(width=10, height=2, text="My Button", command=buttonclick)
mybutton.pack(side="top")

# Entry field
myinput = Entry(width=22)
myinput.insert(index=END, string="Was geht")
myinput.pack()

# more examples


# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

window.mainloop()
