from turtle import Turtle, Screen
import random

def create_turtles(width, height, color_list):
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
    is_race_on = False
    if user_bet:
        is_race_on = True
    else:
        print(f"Invalid user bet: {user_bet}")
        return
    
    while is_race_on:
        for turtle in turtle_list:
            if turtle.xcor() > (width / 2) - 20:
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

