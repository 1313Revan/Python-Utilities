# A script I made real quick for my girlfriend's birthday :)

# Heart functions and loop are by "2kCreator"

import math
from random import choice
from turtle import *

colors = [(233, 27, 28), (178, 18, 179), (255, 138, 154), (255, 255, 69), (255, 200, 22)]


def heart_a(k):
    return 15 * math.sin(k) ** 3


def heart_b(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)


def write_text():
    penup()
    goto(0, 300)
    color((255, 130, 140))
    write("Happy Birthday Kateleen", False, "center", ("Georgia", 64, "normal"))
    goto(0, -450)
    write("I love you!", False, "center", ("Georgia", 64, "normal"))
    goto(0, 0)
    pendown()


hideturtle()
speed("fastest")
colormode(255)
bgcolor((255, 220, 225))

write_text()

for i in range(6000):
    goto(heart_a(i) * 20, heart_b(i) * 20)
    for j in range(5):
        color(choice(colors))
    goto(0, 0)

done()
