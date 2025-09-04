from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for coordinate in STARTING_POSITION:
            self.add_segment(coordinate)


    def add_segment(self,coordinate):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(coordinate)
        self.turtles.append(turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for turt_num in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[turt_num-1].xcor()
            new_y = self.turtles[turt_num-1].ycor()
            self.turtles[turt_num].goto(new_x,new_y)
        self.turtles[0].forward(MOVING_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

