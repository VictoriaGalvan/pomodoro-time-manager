# Created by Victoria M. Galvan

# ---------------------------- IMPORTS ------------------------------- #
import math
from tkinter import *

# ---------------------------- SETTINGS ------------------------------- #
# Color Settings
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Font Settings
FONT_NAME = "Courier"
FONT_SIZE = 35
FONT_CHARACTER = "bold"
FONT = (FONT_NAME, FONT_SIZE, FONT_CHARACTER)

# Time Settings
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# UI Settings
WIDTH = 200
HEIGHT = 224


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    countdown(5 * 60)


def countdown(time):
    minute = math.floor(time / 60)
    second = time % 60

    if second < 10:
        second = f"0{second}"

    new_time = f"{str(minute)}:{str(second)}"

    canvas.itemconfig(timer_text, text=new_time)

    if time > 0:
        window.after(1000, countdown, time - 1)


# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
window.title("Pomodoro Time Manager")
window.config(padx=100, pady=50, bg=YELLOW)

# develop photo image
tomato_img = PhotoImage(file="tomato.png")

# create canvas
canvas = Canvas(width=WIDTH, height=HEIGHT, bg=YELLOW, highlightthickness=0)
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=tomato_img)
timer_text = canvas.create_text(WIDTH / 2, 130, text="00:00", fill="white", font=FONT)
canvas.grid(row=1, column=1)

# timer text
timer_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 50, FONT_CHARACTER))
timer_label.grid(row=0, column=1)

# create start button
start_button = Button(text="Start", command=start_timer)  # starts the timer when clicked
start_button.grid(row=2, column=0)

# create restart button
restart_button = Button(text="Restart")
restart_button.grid(row=2, column=2)

# add check marks
check_marks = Label(text="✔️", foreground=GREEN, background=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
