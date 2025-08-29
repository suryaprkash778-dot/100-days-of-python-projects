import random
import turtle as t
color_list = [(235, 240, 246), (240, 246, 243), (133, 164, 202), (225, 150, 101),
 (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161),
 (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73),
 (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219),
 (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209), (65, 66, 56),
 (103, 140, 129), (164, 200, 214), (130, 129, 122)]

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)
tim.width(15)
tim.hideturtle()
tim.speed("fastest")


y = tim.ycor()
x = tim.xcor()


in_motion = True
while in_motion:

    for _ in range(10):
        tim.pencolor(random.choice(color_list))
        tim.forward(1)
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.penup()
    y += 50
    tim.goto(x, y)
    tim.pendown()
    if y == 500:
        in_motion = False

screen.exitonclick()

