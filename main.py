# Created by Victoria M. Galvan

# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
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

# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
window.title("Pomodoro Time Manager")
window.config(padx=100, pady=50)

# develop photo image
tomato_img = PhotoImage(file="tomato.png")

# create canvas
canvas = Canvas(width=WIDTH, height=HEIGHT)
canvas.create_image(WIDTH/2 + 3, HEIGHT/2, image=tomato_img)
canvas.create_text(WIDTH/2 + 3, 130, text="00:00", fill="white", font=FONT)
canvas.pack()

window.mainloop()
