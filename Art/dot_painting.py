from turtle import *
from random import choice

rgb_list = [(124, 180, 210), (198, 174, 16), (29, 119, 167), (176, 14, 45), (235, 150, 76), (145, 171, 219),
            (236, 204, 90), (217, 124, 163), (26, 144, 74), (215, 80, 123), (9, 171, 210), (212, 61, 27)]

draw = Turtle()
draw.hideturtle()
draw.speed("fastest")
colormode(255)


def draw_dot(x, y):
    """Draws a single dot, each with different colors, at the given coordinates."""
    draw.pu()
    draw.goto(x, y)
    draw.pd()
    draw.dot(50, choice(rgb_list))


def draw_grid():
    """Draws a grid of dots."""
    x_start = -500
    y_start = 500
    gap = 50

    for row in range(10):
        for col in range(10):
            draw_dot(x_start + col * 100, y_start - row * gap)
        y_start -= gap


display = Screen()
display.setup(2048, 1152, 100, 100)

draw_grid()

display.exitonclick()
