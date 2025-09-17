import turtle
import pandas
data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("Name The States")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
score = 0
guess = []
while len(guess) < 50:
    answer_state = screen.textinput(title=f"{len(guess)}/50 States Correct",
                                    prompt="what's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in data.state.tolist():
            if state not in guess:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if  answer_state in data.state.tolist():
        guess.append(answer_state)
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        state_data = data[data.state == answer_state]
        pen.goto(state_data.x.item(),state_data.y.item())
        pen.write(answer_state)
        
screen.exitonclick()
