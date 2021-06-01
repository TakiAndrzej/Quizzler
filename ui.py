from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface(Tk):

    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        self.quiz = quiz_brain
        self.user_answer = False
        self.title("Quizzler")
        self.config(padx=20, pady=20, bg=THEME_COLOR)

        # Labels
        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 12, "normal"))
        self.score.grid(column=1, row=0)


        # Canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.text = self.canvas.create_text(150, 125, text="test", fill=THEME_COLOR,
                                            font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")
        self.f_button = Button(image=false_image, highlightthickness=0, command=self.no)
        self.f_button.grid(column=0, row=2)
        self.r_button = Button(image=true_image, highlightthickness=0, command=self.yes)
        self.r_button.grid(column=1, row=2)

        self.change_text()

        self.mainloop()

    def change_text(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.text, text=self.quiz.ask_question(), fill=THEME_COLOR, font=("Arial", 20, "italic"))
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quizz")
            self.r_button.config(state="disabled")
            self.f_button.config(state="disabled")

    def yes(self):
        self.check_feedback("True")
        self.change_text()
        self.score.config(text=f"Score: {self.quiz.score}")

    def no(self):
        self.check_feedback("False")
        self.change_text()
        self.score.config(text=f"Score: {self.quiz.score}")

    def default_color(self):
        self.canvas.config(bg="white")

    def check_feedback(self, answer):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green")
            self.after(1000, self.default_color)
        else:
            self.canvas.config(bg="red")
            self.after(1000, self.default_color)

