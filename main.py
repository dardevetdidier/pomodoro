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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=16, highlightthickness=0)
start_button.config(padx=15)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=16, highlightthickness=0)
start_button.config(padx=15)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔", fg=GREEN, bg=YELLOW, font=("Arial", 20, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()