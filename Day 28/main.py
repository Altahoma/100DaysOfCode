from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
resp = 0
mark = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global resp
    window.after_cancel(timer)
    title_label.config(text='Timer')
    check_marks_label.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    resp = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global resp
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    resp += 1

    if resp % 8 == 0:
        title_label.config(text='Break', bg=YELLOW, fg=PINK, font=(FONT_NAME, 50))
        count_down(long_break_sec)
    elif resp % 2 == 0:
        title_label.config(text='Break', bg=YELLOW, fg=RED, font=(FONT_NAME, 50))
        count_down(short_break_sec)
    else:
        title_label.config(text='Work', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    global mark
    count_min = int(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text='{:02}:{:02}'.format(count_min, count_sec))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if resp % 2 == 0:
            mark += '☑'
            check_marks_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
check_marks_label = Label(text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
check_marks_label.grid(column=1, row=3)

start_button = Button(text='Start', command=start_timer, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)
reset_button = Button(text='Reset', command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

window.mainloop()
