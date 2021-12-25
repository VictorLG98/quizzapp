import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzier")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quote_text = self.canvas.create_text(150,
                                                  125,
                                                  width=280,
                                                  text="Keep squares out yo circle",
                                                  fill=THEME_COLOR,
                                                  font=("Arial", 20, "italic")
                                                  )
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.green_img = PhotoImage(file="images/true.png")
        self.red_img = PhotoImage(file="images/false.png")
        self.green_btn = Button(image=self.green_img, highlightthickness=0, command=self.true_pressed)
        self.red_btn = Button(image=self.red_img, highlightthickness=0, command=self.false_pressed)
        self.green_btn.grid(row=2, column=0, pady=30)
        self.red_btn.grid(row=2, column=1, pady=30)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text,
                                   text=f"Has llegado al final del test!\nTú puntuación final es de: {self.quiz.score}")
            self.green_btn.config(state="disabled")
            self.red_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
