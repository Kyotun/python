from turtle import Turtle
import random

MOVE_DISTANCE = SEGMENT_SIZE = 20
WALL_DISTANCE = 10
COLLISION_DISTANCE = 10
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
        self.move_speed = 0.1


    def check_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < COLLISION_DISTANCE:
                return True


    def check_wall(self):
        coordinate_x = self.segments[0].xcor()
        coordinate_y = self.segments[0].ycor()
        distance_x = abs(abs(coordinate_x) - self.screen_width/2)
        distance_y = abs(abs(coordinate_y) - self.screen_heigth/2)
        if distance_x < WALL_DISTANCE or distance_y < WALL_DISTANCE:
            return True


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.speed("fastest")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def reset(self):
        for segment in self.segments:
            segment.goto(self.screen_width + 100, self.screen_heigth + 100)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        coordinate_x = 0
        coordinate_y = 0
        for segment in range (self.segment_number):
            self.add_segment((coordinate_x, coordinate_y))
            coordinate_x -= SEGMENT_SIZE
        

    def extend(self):
        self.add_segment(self.segments[-1].position())
        self.segment_number += 1


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