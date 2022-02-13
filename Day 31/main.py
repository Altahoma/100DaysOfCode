from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def next_card():
    global current_card
    global flip_timer
    global words_dict
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(words_dict)
    except IndexError:
        reset_data = pandas.read_csv('data/french_words.csv')
        words_dict = reset_data.to_dict(orient="records")
        current_card = random.choice(words_dict)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(language_canvas, text='French', fill='black')
    canvas.itemconfig(word_canvas, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language_canvas, text='English', fill='white')
    canvas.itemconfig(word_canvas, text=current_card['English'], fill='white')


def is_known():
    words_dict.remove(current_card)
    words_to_learn = pandas.DataFrame(words_dict)
    words_to_learn.to_csv('data/words_to_learn.csv', index=False)
    next_card()


try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    words_dict = original_data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")


# UI Setup
window = Tk()
window.title('Flashy')
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Images
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front_img)
language_canvas = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'), fill='black')
word_canvas = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'), fill='black')
canvas.grid(column=0, row=0, columnspan=2)

# Labels

# Buttons
right_button = Button(image=right_img, command=is_known, highlightbackground=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, command=next_card, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()
