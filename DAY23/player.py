from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.penup()
        self.shape("turtle")
        self.color("dark green")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.fd(MOVE_DISTANCE)

    def move_backward(self):
        self.bk(MOVE_DISTANCE)

    def turn_left(self):
        self.left(90)
        self.fd(MOVE_DISTANCE)
        self.right(90)

    def turn_right(self):
        self.right(90)
        self.fd(MOVE_DISTANCE)
        self.left(90)
