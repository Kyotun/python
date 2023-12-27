from turtle import Turtle, Screen
import random

def create_turtles(width, height, color_list):
    """
    For given height and width of the screen as parameter turtles will be created in different colors
    in order to given color list.
    Placing of turtles will be arranged for given width and height of screen.
    
    Returns:
    _List_: Created turtles as list.
    """
    turtles = []
    y_axis = (height / 4) * -1
    for clr in color_list:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(clr)
        new_turtle.penup()
        new_turtle.goto(x= -(width/2-20), y=y_axis)
        turtles.append(new_turtle)
        y_axis += 50
    return turtles

def turtle_race(turtle_list, user_bet, width):
    """
    If there is no bet, returns void.
    Turtles(given turtle_list) will be moved forward one by one randomly in range [0,20]
    If one turtle is at end point, race is over that turtle will win.
    
    Args:
        turtle_list (_List_): Created turtles as list.
        user_bet (_String_): Users bet for guessing, which turtle will win.
        width (_Integer_): Width of the screen to calculate which turtle close to the end of screen.
    """
    is_race_on = False
    if user_bet:
        is_race_on = True
    else:
        print(f"Invalid user bet: {user_bet}")
        return
    
    while is_race_on:
        for turtle in turtle_list:
            # Select the next turtle in given turtle list and moves it forward with random distance
            # selected between [0,20]
            if turtle.xcor() > (width / 2) - 20:
                # If this statement is true, current turtle has fnished the race and 
                # close to the end of the right edge of screen.
                # Save its color and announce its color as winner.
                is_race_on = False
                winning_color = turtle.pencolor()
                if user_input == winning_color:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost :c The {winning_color} turtle won...")
                break
            rand_distance = random.randint(0,20)
            turtle.forward(rand_distance)
    

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "black", "green", "blue", "pink"]
user_input = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ").lower()

turtle_list = create_turtles(width=500, height=400, color_list=colors)
turtle_race(turtle_list=turtle_list, user_bet=user_input, width=500)



screen.exitonclick()

