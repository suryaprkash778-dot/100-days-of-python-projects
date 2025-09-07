from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
random_x =[]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_car = []
        self.create_car()
        self.car_speed = 0.1

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300,random_y)

            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            self.all_car.append(new_car)




    def move_car(self):
        for car in self.all_car:
            car.bk(STARTING_MOVE_DISTANCE)
