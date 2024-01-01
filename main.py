from tkinter import *
import pandas
from random import choice

tim = ''
frame = pandas.read_csv('./data/french_words.csv')
words = frame.to_dict(orient='records')


def reset():
    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(title, fill='black')
    canvas.itemconfig(word, fill='black')


def flip_card(dic):
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=dic['English'], fill='white')


def gen_word():
    reset()
    global tim
    """Generates a word to display on the canvas"""
    new_key = choice(words)
    canvas.itemconfig(title, text='French')
    canvas.itemconfig(word, text=new_key['French'])
    tim = window.after(3000, flip_card, new_key)


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file='./images/card_front.png')
back = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front)
title = canvas.create_text(400, 190, text='', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 283, text='', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

wrong = PhotoImage(file='./images/wrong.png')
w_bt = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=gen_word)
w_bt.grid(column=0, row=1)

right = PhotoImage(file='./images/right.png')
r_bt = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=gen_word)
r_bt.grid(column=1, row=1)

gen_word()

window.mainloop()
