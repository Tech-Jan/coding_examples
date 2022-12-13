from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(TIMER)
    label_timer.config(text="Resedd", fg="grey")
    canvas.itemconfig(timer_text, text="00:00")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    if REPS % 2 == 1:
        count_down(work_sec)
        label_timer.config(text="WorkWork", fg=GREEN)

    elif REPS % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="LongBreak", fg="red")
        text_checkmark = REPS // 2 * "✓"
        label_checkmark.config(text=text_checkmark)
    else:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg="pink")
        text_checkmark = REPS // 2 * "✓"
        label_checkmark.config(text=text_checkmark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()
    window.update()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PomOdOro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=201, height=225, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 105, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 33, "bold"), fill="white")
canvas.grid(row=2, column=2)

label_timer = Label(text="Timer", font=(FONT_NAME, 33, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(row=1, column=2)

button_start = Button(text="Start", bg=YELLOW, command=start_timer)
button_start.grid(row=3, column=1)

button_reset = Button(text="Reset", bg=YELLOW, command=reset_timer)
button_reset.grid(row=3, column=3)

label_checkmark = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
label_checkmark.grid(row=4, column=2)
window.update()

window.mainloop()
