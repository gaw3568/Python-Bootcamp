from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score : 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=1)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Question Text", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=true_image, highlightthickness=0, command=self.true_btn_click)
        self.false_btn = Button(image=false_image, highlightthickness=0, command=self.false_btn_click)
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            # return 값은 string
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Game is quit!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_btn_click(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_btn_click(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right:bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)