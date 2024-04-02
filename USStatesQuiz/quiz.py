import turtle

import pandas

from write import Write

screen = turtle.Screen()
screen.setup(width=800, height=600, startx=875, starty=400)
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = Write()

state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()

correct_guesses = []
while len(correct_guesses) < 50:
    user_answer = screen.textinput(title=f"{len(correct_guesses)}/50 States", prompt="Enter a state name:").title()

    if user_answer in all_states:
        correct_guesses.append(user_answer)
        answer_info = state_data[state_data.state == user_answer]
        writer.write_state(user_answer, answer_info.x, answer_info.y)
    elif user_answer == "Quit" or user_answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("states_to_learn.csv")

        break

turtle.mainloop()
