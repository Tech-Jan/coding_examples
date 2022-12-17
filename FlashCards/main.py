import pandas
from tkinter import *

import random

try:
    dictionary = pandas.read_csv("./data/myunknownwords.csv")
except FileNotFoundError:
    print("no saved status found")
    dictionary = pandas.read_csv("./data/french_words.csv")
else:
    print("found saved data")


RANDOMENTRY = dictionary.sample()
print(dictionary)


def click_button_yes():
    global RANDOMENTRY, flip_timer, dictionary
    window.after_cancel(flip_timer)
    card_front.itemconfig(myimage, image=card_front_image)
    # removes current entry because the word was known (clicked yes)
    dictionary = dictionary[dictionary.French != RANDOMENTRY.iloc[0].tolist()[0]]
    # writes it to a csv
    dictionary.to_csv("./data/myunknownwords.csv", mode=W, index=False)
    # picks a new word from the remaining words in dict
    RANDOMENTRY = dictionary.sample()
    # gigives back the randomentry Values as list
    randomword = RANDOMENTRY.iloc[0].tolist()
    # gives back the randomentry Key (language)
    title = RANDOMENTRY.keys()[0]
    card_front.itemconfig(card_word, text=randomword[0])
    card_front.itemconfig(card_title, text=title)
    flip_timer = window.after(3000, flipcards)


def flipcards():
    global RANDOMENTRY, flip_timer
    randomword = RANDOMENTRY.iloc[0].tolist()
    title = RANDOMENTRY.keys()[1]
    card_front.itemconfig(myimage, image=card_back_image)
    card_front.itemconfig(card_word, text=randomword[1])
    card_front.itemconfig(card_title, text=title)


def click_button_no():
    global RANDOMENTRY, flip_timer
    window.after_cancel(flip_timer)
    card_front.itemconfig(myimage, image=card_front_image)
    RANDOMENTRY = dictionary.sample()
    randomword = RANDOMENTRY.iloc[0].tolist()
    title = RANDOMENTRY.keys()[0]
    card_front.itemconfig(card_word, text=randomword[0])
    card_front.itemconfig(card_title, text=title)
    flip_timer = window.after(3000, flipcards)


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=20)
window.title("Flashcards")
window.minsize(height=760, width=840)

card_front_image = PhotoImage(file="./images/card_front.png")
card_front = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=526)
myimage = card_front.create_image(0, 0, image=card_front_image, anchor=NW)
card_front.grid(column=1, row=1, columnspan=2, pady=30)
card_title = card_front.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = card_front.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

card_back_image = PhotoImage(file="./images/card_back.png")
# card_back = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0,width=800, height=526)
# card_back.create_image(0,0,image = card_back_image, anchor= NW)
# card_back.grid(column=1,row=1, columnspan = 2)


button_no_image = PhotoImage(file="./images/wrong.png")
button_no = Button(image=button_no_image)
button_no.config(image=button_no_image, height=100, width=100, command=click_button_no)
button_no.grid(column=1, row=2)

button_yes_image = PhotoImage(file="./images/right.png")
button_yes = Button()
button_yes.config(image=button_yes_image, height=100, width=100, command=click_button_yes)
button_yes.grid(column=2, row=2)

flip_timer = window.after(3000, flipcards)

click_button_no()
window.mainloop()
