from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=340, height=500)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=20)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="sone Question here ", fill=THEME_COLOR,
                                                     font=("Arial", 16, "italic"))
        self.cross_image = PhotoImage(file="images/false.png")
        self.cross_btn = Button(image=self.cross_image, highlightthickness=0, command=self.press_false)
        self.cross_btn.grid(row=2, column=1, pady=20, padx=(20, 50))
        self.check_image = PhotoImage(file="images/true.png")
        self.check_btn = Button(image=self.check_image, highlightthickness=0, command=self.press_true)
        self.check_btn.grid(row=2, column=0, pady=20, padx=(50, 20))
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1, pady=20, padx=50)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.check_btn.config(state="disabled")
            self.cross_btn.config(state="disabled")

    def press_true(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)

    def press_false(self):
        is_right = self.quiz.check_answer(False)
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")


        self.window.after(1000, self.get_next_question)