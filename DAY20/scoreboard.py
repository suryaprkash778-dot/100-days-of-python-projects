from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=True, align="center", font=("courier", 16, "normal"))


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg="GAME OVER", move=True, align="center", font=("courier", 16, "normal"))



    def increase_score(self):
        self.score +=1
        self.clear()
        self.goto(0,270)
        self.update_scoreboard()
