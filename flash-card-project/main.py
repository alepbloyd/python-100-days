FRONT_BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
from tkinter import *
import pandas
from card import Card
import random


# UI SETUP
cards = []
right_cards = []
wrong_cards = []
current_card = Card(french_word="Ready?", english_word="Ready?")

word_data = pandas.read_csv("data/french_words.csv")

word_dict = word_data.to_dict(orient="records")

for word_pair in word_dict:
  new_card = Card(french_word = word_pair["French"], english_word = word_pair["English"])
  cards.append(new_card)

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=FRONT_BACKGROUND_COLOR)

def draw_new_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  card_canvas.itemconfig(card_canvas_image, image=card_front_image)
  card_canvas.itemconfig(language_label, fill="black")
  card_canvas.itemconfig(word_label, fill="black")
  current_card = random.choice(cards)
  card_canvas.itemconfig(language_label, text="French")
  card_canvas.itemconfig(word_label, text=current_card.french_word)
  window.after(3000, flip_card, current_card)
  cards.remove(current_card)

def flip_card(card):
  card_canvas.itemconfig(language_label, text="English")
  card_canvas.itemconfig(word_label, text=card.english_word)
  card_canvas.itemconfig(card_canvas_image, image=card_back_image)
  card_canvas.itemconfig(language_label, fill="white")
  card_canvas.itemconfig(word_label, fill="white")

flip_timer = window.after(3000, flip_card, current_card)


card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
wrong_button_image = PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")

card_canvas = Canvas(width=800, height=526, highlightthickness=0, background=FRONT_BACKGROUND_COLOR)
card_canvas_image = card_canvas.create_image(400, 263, image=card_front_image)
card_canvas.grid(column=0, row=0, columnspan=2)

language_label = card_canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT, fill="black")
word_label = card_canvas.create_text(400, 263, text="Ready?", font=WORD_FONT, fill="black")

wrong_button = Button(image=wrong_button_image, highlightthickness=0, highlightbackground=FRONT_BACKGROUND_COLOR, command=draw_new_card)
right_button = Button(image=right_button_image, highlightthickness=0, highlightbackground=FRONT_BACKGROUND_COLOR, command=draw_new_card)

wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

window.mainloop()