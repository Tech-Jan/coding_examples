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
window.minsize(width=500, height=100)
window.config(padx=20,pady=20)

# Label
mylabel = Label(text="My First Label", font=("Arial", 22))
# pack puts the label on screen
mylabel.grid(column=0,row=0)
mylabel.config(padx=10)


def buttonclick():
    myinputtext = myinput.get()
    mylabel.config(text=myinputtext)

    print(myinputtext)
    print("ABBVC")


# Button
mybutton = Button(width=10, height=2, text="My Button", command=buttonclick)
# mybutton.pack(side="top")
mybutton.grid(column=1,row=1)

mybutton2= Button(text="enwbutton")
mybutton2.grid(column=2,row=0)

# Entry field
myinput = Entry(width=22)
myinput.insert(index=END, string="Was geht")
# myinput.pack()
myinput.grid(column=3,row=2)

window.mainloop()