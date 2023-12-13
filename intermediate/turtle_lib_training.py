from turtle import Turtle, Screen

alex = Turtle()
alex.shape("arrow")
alex.color("red")

def draw_shape(num_of_side):
    angle = 360 / num_of_side
    for _ in range(num_of_side):
        alex.forward(100)
        alex.left(angle)

for shape_side in range(3,50):
    draw_shape(shape_side)


screen = Screen()
screen.exitonclick()
