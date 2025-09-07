from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_scoreboard()


    def create_scoreboard(self):
        self.clear()
        self.color("black")
        self.penup()
        self.goto(-210, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.hideturtle()

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER\nFINAL SCORE: {self.level}", align="center", font=FONT)
