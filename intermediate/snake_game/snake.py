from turtle import Turtle
import random

MOVE_DISTANCE = 20
COLORS = ["red", "purple", "blue", "pink", "orange", "green"]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, segment_number, screen_width, screen_heigth):
        self.segment_number = segment_number
        self.screen_width = screen_width
        self.screen_heigth = screen_heigth
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def check_wall(self):
        coordinate_x = self.head.xcor()
        coordinate_y = self.head.ycor()
        distance_x = abs(coordinate_x - self.screen_width/2)
        distance_y = abs(coordinate_y - self.screen_heigth/2)
        if distance_x < 20 or distance_y < 20:
            return True


    def create_snake(self):
        coordinate_x = 0
        coordinate_y = 0
        for segment in range (self.segment_number):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(coordinate_x, coordinate_y)
            self.segments.append(new_segment)
            coordinate_x -= 20


    def move(self):
        for seg_num in range (len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
            self.segments[seg_num].color(random.choice(COLORS))
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)