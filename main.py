import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")

img = "images/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct.", "What's another state's name?")
    if answer_state != None:
        answer_state = answer_state.title()

    if answer_state == "Exit" or answer_state == None:
        missing_states = [s for s in all_states if s not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states-to-learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_info = states_data[states_data.state == answer_state]

        t.goto(int(state_info.x), int(state_info.y))
        t.write(state_info.state.item())
