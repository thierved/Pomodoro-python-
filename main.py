from email.mime import image
from textwrap import fill
from tkinter import *
from tkinter import font
from turtle import bgcolor, colormode

window = Tk()
window.title("Pomodoro!")
window.config(padx=10, pady=10, bg="#f25")

#Label
timer_label = Label(text="Timer", font=("helvatica", 35, "bold"), fg="green", bg="#f25")
timer_label.grid(column=1, row=0)

#Canvas
canvas = Canvas(width=200, height=300, bg="#f25", highlightthickness=0)
canvas.create_text(100, 150, text="00:00", fill="white", font=("courier", 38, "bold"))
canvas.grid(column=1, row=1)

#Buttons
start_btn = Button(text="Start", highlightthickness=0)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="reset", highlightthickness=0)
reset_btn.grid(column=2, row=2)




window.mainloop()
