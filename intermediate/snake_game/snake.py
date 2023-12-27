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
    """Snake class. Creation parameterss -> segment number, screen width and height for accurate results
    and good user experience.
    Head will be assigned as first segment.
    """
    def __init__(self, segment_number, screen_width, screen_heigth):
        self.segment_number = segment_number
        self.screen_width = screen_width
        self.screen_heigth = screen_heigth
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.move_speed = 0.1


    def check_collision(self):
        """Controls if there is any collison between the segments.
        Snake cannot touch itself(its segments).
        Returns:
            _bool_: Did one of the segment touch another segment?
        """
        for segment in self.segments[1:]:
            if self.head.distance(segment) < COLLISION_DISTANCE:
                return True


    def check_wall(self):
        """Calculates the difference between the coordinates of snakes's head
        and screens width and height.
        If distance is smaller than a wall distance constant(10 unit), returns this function True.
        Returns:
            _bool_: Is snake touch the border of screen? True, if yes.
        """
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
        """Moves all the segments out of the screen and clear the segments from the screen.
        Creates a new snake add asign the 0 element of segments to the head of the snake.
        """
        for segment in self.segments:
            segment.goto(self.screen_width + 100, self.screen_heigth + 100)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        """Puts a segment, slide to the left in negative 
        x direction as segment size unit and add another segment.
        """
        coordinate_x = 0
        coordinate_y = 0
        for segment in range (self.segment_number):
            self.add_segment((coordinate_x, coordinate_y))
            coordinate_x -= SEGMENT_SIZE
        

    def extend(self):
        """Adds segment to snake with help of last segments position and increase the number of segment by 1.
        """
        self.add_segment(self.segments[-1].position())
        self.segment_number += 1


    def move(self):
        """Starts from the end of the snake.
        From end to the beginning to the snake, the former segment takes place of the next segment.
        At the end second segment will take the position of first segment(head of snake).
        Finally, head of snake will move forward and loop will be over and snake would be moved.
        """
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