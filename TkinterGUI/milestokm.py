from tkinter import *

mywindow = Tk()
mywindow.minsize(width=300, height=100)
mywindow.title("Mile to Km Converter")

label1 = Label(text="is equal to")
label1.grid(column=1,row=1)

label2 = Label(text="Km")
label2.grid(column=3,row=1)

label3 = Label(text="0")
label3.grid(column=2,row=1)

myinput = Entry()
myinput.grid(column=2,row=0)

def mybutton_click():
    givenmiles= int(myinput.get())
    calculated_km = round(givenmiles*1.60934,2)
    label3.config(text=calculated_km)

mybutton = Button(text="Calculate", command=mybutton_click)

mybutton.grid(column=2,row=3)

mywindow.mainloop()