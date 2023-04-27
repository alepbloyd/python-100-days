from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
RED_COLOR = "#eb4034"
GREEN_COLOR = "#07a357"
SCORE_FONT = ("Arial", 14, "normal")
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Testing", fill="black", font=QUESTION_FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=30)

        self.score = 0

        self.score_label = Label(text=f"Score: {self.score}", font=SCORE_FONT, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button_click)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button_click)
        
        self.true_button.grid(column=0,row=2, padx=20, pady=20)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def true_button_click(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_click(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="~End of Quiz~")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)