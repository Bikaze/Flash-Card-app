from tkinter import *
import pandas
from random import choice

frame = pandas.read_csv('./data/french_words.csv')
words = frame.to_dict(orient='records')


def gen_word():
    """Generates a word to display on the canvas"""
    new_key = choice(words)
    title['text'] = 'French'
    word['text'] = new_key['French']


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=front)
canvas.grid(column=0, row=0, columnspan=2)

title = Label(text='', font=('Arial', 40, 'italic'), bg='white')
title.place(x=330, y=120)

word = Label(text='', font=('Arial', 60, 'bold'), bg='white')
word.place(x=290, y=223)

wrong = PhotoImage(file='./images/wrong.png')
w_bt = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=gen_word)
w_bt.grid(column=0, row=1)

right = PhotoImage(file='./images/right.png')
r_bt = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=gen_word)
r_bt.grid(column=1, row=1)

gen_word()

window.mainloop()
