from turtle import Turtle

class Snake:
    def __init__(self):
        self.segment_number = 0
        self.segments = []
    

    def create_snake(self):
        if self.segment_number > 0:
            for _ in range (self.segment_number):
                new_segment = Turtle(shape="square")
                new_segment.color("white")
                new_segment.penup()
                self.segments.append(new_segment)
            
            for index in range(len(self.segments)-1):
                self.segments[index+1].goto(self.segments[index].xcor()+20,self.segments[index].ycor())
