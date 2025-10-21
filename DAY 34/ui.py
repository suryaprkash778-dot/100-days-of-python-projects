from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
green = "#90EE90"
red = "#ee2400"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()


        self.window.title("Quizler")

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(height=250,width=300,bg="white")
        self.question_text = self.canvas.create_text(150,125,
                                                     width=280,
                                                     text="some question text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial",18,"italic")
                                                     )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image,highlightthickness=0,height=70,width=70,command=self.right_button_pressed)
        self.right_button.grid(row=2,column=0)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image,highlightthickness=0,height=70,width=70,command=self.wrong_button_pressed)
        self.wrong_button.grid(row=2, column=1)
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def wrong_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def change_colour(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg=green)
        else:
            self.canvas.config(bg=red)


        self.canvas.config(bg="white")



    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg=green)
        else:
            self.canvas.config(bg=red)

        self.window.after(1000, self.get_next_question)



