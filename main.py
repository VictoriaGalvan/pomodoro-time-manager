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
reps = 0
timer = None

# UI Settings
WIDTH = 600
HEIGHT = 224


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    # stop timer and reset time to 00:00
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")

    # update label text
    timer_label.config(text="Timer", foreground=GREEN)

    # reset check marks
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    long_break_seconds = LONG_BREAK_MIN * 60
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", foreground=RED)
        countdown(long_break_seconds)

    elif reps % 2 == 0:
        timer_label.config(text="Short Break", foreground=PINK)
        countdown(short_break_seconds)

    else:
        timer_label.config(text="Time to Work!", foreground=GREEN)
        countdown(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(time):
    # get minute and second values
    minute = math.floor(time / 60)
    second = time % 60

    # edge case: (time < 10)
    if second < 10:
        second = f"0{second}"

    # format the time into ##:## format
    new_time = f"{str(minute)}:{str(second)}"

    canvas.itemconfig(timer_text, text=new_time)

    if time > 0:
        global timer
        timer = window.after(1000, countdown, time - 1)

    # go to the next section once the timer hits 0
    else:
        start_timer()

        # update check marks when the user completes
        # another round of work
        marks = ""

        work_sessions = math.floor(reps / 2)

        for _ in range(work_sessions):
            marks += "✔"

        check_marks.config(text=marks)


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

# check marks
check_marks = Label(foreground=GREEN, background=YELLOW)
check_marks.grid(row=2, column=2)

# create start button
start_button = Button(text="Start", command=start_timer)  # starts the timer when clicked
start_button.grid(row=2, column=0)

# create restart button
restart_button = Button(text="Restart", command=reset_timer)
restart_button.grid(row=2, column=2)

window.mainloop()
