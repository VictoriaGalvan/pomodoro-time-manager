# Created by Victoria M. Galvan

# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WIDTH = 200
HEIGHT = 224

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Time Manager")

# develop photo image
tomato_img = PhotoImage(file="tomato.png")

# create canvas
canvas = Canvas(width=WIDTH, height=HEIGHT)
canvas.create_image(WIDTH/2, HEIGHT/2, image=tomato_img)
canvas.pack()

window.mainloop()