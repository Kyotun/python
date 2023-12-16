from turtle import Turtle
import random

COLORS = ["red", "green", "purple", "pink", "yellow", "orange"]
SPEEDS = ["fastest", "fast", "slow", "normal", "slowest"]
SCREEN_WIDTH = SCREEN_HEIGTH = 600
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.car_speed = MOVE_INCREMENT
        self.coordinates = []
        self.all_cars = []
        self.create_coordinates()
        


    def create_coordinates(self):
        half_of_heigth = int(SCREEN_HEIGTH/2)
        for i in range(-half_of_heigth + 10*STARTING_MOVE_DISTANCE, half_of_heigth - 10*STARTING_MOVE_DISTANCE, 20):
            self.coordinates.append(i)


    def create_car(self):
        random_integer = random.randint(1,6)
        if random_integer <= 4:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=0.5, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.speed(random.choice(SPEEDS))
            new_car.goto(SCREEN_WIDTH/2, random.choice(self.coordinates)) 
            self.all_cars.append(new_car)


    def delete_car(self):
        self.clear()
        self.reset()
        self.cars.remove(self)


    def move_car(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT