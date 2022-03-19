from cgitb import text
from email.mime import image
import math
from textwrap import fill
from tkinter import *
from tkinter import font

TIMER_DURATION = 25
timer = None

window = Tk()
window.title("Pomodoro!")
window.config(padx=20, pady=20, bg="#f25")

#Label
timer_label = Label(text="Timer", font=("helvatica", 35, "bold"), fg="green", bg="#f25")
timer_label.grid(column=1, row=0)

#Canvas
canvas = Canvas(width=200, height=300, bg="#f25", highlightthickness=0)
timer_digits = canvas.create_text(100, 150, text="00:00", fill="white", font=("courier", 38, "bold"))
canvas.grid(column=1, row=1)

#Buttons
def start_timer():
    timer_counter(TIMER_DURATION*60)

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_digits, text="00:00")


start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

#Functionality
def timer_counter(n):
    minutes = math.floor(n / 60)
    seconds = n % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"
    
    canvas.itemconfig(timer_digits, text=f"{minutes}:{seconds}")
    if n > 0:
        global timer
        timer = window.after(1000, timer_counter, n - 1)



window.mainloop()
