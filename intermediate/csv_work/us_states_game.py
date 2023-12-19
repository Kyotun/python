import turtle
import pandas as pd

def game():
    # Setup the screen
    screen = turtle.Screen()
    screen.title("U.S. State Game")
    image = "intermediate/csv_work/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    data = pd.read_csv("intermediate/csv_work/50_states.csv")

    # Create turtle
    alex = turtle.Turtle()
    alex.penup()
    alex.hideturtle()
    alex.color("black")

    # Setup the game
    score = 0
    all_states = data["state"].tolist()
    states_number = len(all_states)
    known_states = []
    while score < 50:
        if score == 0:
            answer_state = screen.textinput(title="Guess the State", prompt="Can you guess a State?").title()
        else:
            answer_state = screen.textinput(title=f"{score}/{states_number} States Correct", prompt="Can you guess an another State?").title()

        if answer_state.lower() == "quit" or answer_state.lower() == "exit":
            learn_states = []
            for state in all_states:
                if state not in known_states:
                    learn_states.append(state)

            # Save the states which should be learned in .csv format.
            write_data = pd.DataFrame()
            write_data["states_to_learn"] = learn_states
            write_data.to_csv("intermediate/csv_work/states_to_learn.csv")
            break

        if answer_state in all_states:
            corresponding_row = data[data["state"] == answer_state]
            x_cor = int(corresponding_row["x"].iloc[0])
            y_cor = int(corresponding_row["y"].iloc[0])
            known_states.append(answer_state)
            alex.goto(x=x_cor, y=y_cor)
            alex.write(answer_state)
            score += 1
    
game()

