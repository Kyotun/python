from turtle import Turtle, Screen
from player import Player
from car import CarManager
from scoreboard import ScoreBoard
import time

UP = "Up"
DOWN = "Down"
RIGHT = "Right"
LEFT = "Left"

SCREEN_WIDTH = SCREEN_HEIGTH = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGTH)


def game():
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)
    player = Player()
    car_manager = CarManager()
    scoreboard = ScoreBoard()
    cars = car_manager.all_cars

    screen.listen()
    screen.onkey(player.move_up, UP)
    screen.onkey(player.move_down, DOWN)
    screen.onkey(player.move_right, RIGHT)
    screen.onkey(player.move_left, LEFT)

    is_on = True
    while is_on:
        screen.update()
        time.sleep(0.1)
        car_manager.create_car()
        car_manager.move_car()


        for car in cars:
            if player.distance(car) < 20:
                scoreboard.game_over()
                is_on = False

        
        if player.is_at_finish():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_score()

user_input = ""
while user_input != "q":
    user_input = screen.textinput(title="GAME STATEMENT", 
                              prompt="Press Q for ending, G for starting the game.").lower()
    
    if user_input != "q":
        game()

