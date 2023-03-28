BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
from tkinter import *

# UI SETUP

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
wrong_button_image = PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")

card_canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_canvas.create_image(400, 263, image=card_front_image)
card_canvas.grid(column=0, row=0, columnspan=2)

language_label = card_canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT, fill="black")
word_label = card_canvas.create_text(400, 263, text="trouve", font=WORD_FONT, fill="black")

wrong_button = Button(image=wrong_button_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
right_button = Button(image=right_button_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)

wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

window.mainloop()