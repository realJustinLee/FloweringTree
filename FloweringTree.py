# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:18:10 2018

@author: lixin
"""
import random
from turtle import *

DEBUG = False
BRANCH_LENGTH = 60
SUN_RADIUS = 40
MAGIC = 12


def tree(branch_len, _turtle):
    global petal_count
    global petal_left_border
    global petal_right_border
    if branch_len > 3:
        if 8 <= branch_len <= 12:
            if random.randint(0, 2) == 0:
                _turtle.color('snow')
            else:
                _turtle.color('lightcoral')
            _turtle.pensize(branch_len / 3)
        elif branch_len < 8:
            petal_count += 1
            cur_x = _turtle.pos()[0]
            if cur_x < 0:
                petal_left_border = min(petal_left_border, cur_x)
            else:
                petal_right_border = max(petal_right_border, cur_x)
            if random.randint(0, 1) == 0:
                _turtle.color('snow')
            else:
                _turtle.color('lightcoral')
            _turtle.pensize(branch_len / 2)
        else:
            _turtle.color('sienna')
            _turtle.pensize(branch_len / 10)

        # Draw the branch/leaf
        _turtle.forward(branch_len)

        random_angle = 3 + 2 * MAGIC * random.random()
        random_length = MAGIC * random.random()

        _turtle.right(random_angle)
        tree(branch_len - random_length, _turtle)
        _turtle.left(2 * random_angle)
        tree(branch_len - random_length, _turtle)
        _turtle.right(random_angle)

        # return to the root of this chile tree
        _turtle.up()
        _turtle.backward(branch_len)
        _turtle.down()


def petal_field(_turtle, count, left_border=-100, right_border=100):
    middle = (right_border + left_border) / 2
    width = (right_border - left_border) / 3
    depth = int(sqrt(width))
    start_pos = _turtle.pos()
    _turtle.up()
    start_pos = [middle, start_pos[1] + depth / 2]
    _turtle.goto(start_pos)
    _turtle.down()

    for _ in range(count):
        random_width = width - 2 * width * random.random()
        random_depth = depth - 2 * depth * random.random()
        _turtle.up()
        _turtle.forward(random_depth)
        _turtle.left(90)
        _turtle.forward(random_width)
        _turtle.down()
        _turtle.pensize(3 * random.random())
        if random.randint(0, 1) == 0:
            _turtle.color("snow")
        else:
            _turtle.color("lightcoral")
        _turtle.circle(1)
        _turtle.up()
        _turtle.right(90)
        _turtle.goto(start_pos)
        _turtle.down()


def the_sun(_turtle, radius=30):
    start_pos = _turtle.pos()
    _turtle.up()
    _turtle.forward(500)
    _turtle.left(90)
    _turtle.forward(300)
    _turtle.down()
    _turtle.color('red')
    _turtle.begin_fill()
    _turtle.circle(radius)
    _turtle.end_fill()
    _turtle.color('lightcoral')
    _turtle.up()
    _turtle.right(90)
    _turtle.goto(start_pos)
    _turtle.down()


if __name__ == '__main__':
    try:
        my_turtle = Turtle()
        my_frame = Screen()
        if DEBUG:
            my_frame.tracer(0, 0)
        else:
            my_frame.tracer(5, 0)
        my_frame.screensize(bg='wheat')
        my_turtle.left(90)
        my_turtle.up()
        my_turtle.backward(250)
        my_turtle.down()
        my_turtle.color('sienna')
        the_sun(my_turtle, SUN_RADIUS)

        petal_count = 0
        petal_left_border = 0
        petal_right_border = 0
        tree(BRANCH_LENGTH, my_turtle)

        if petal_count > 4900:
            petal_count = int(sqrt(petal_count)) + 200
        else:
            petal_count = petal_count / MAGIC + 50
        petal_field(my_turtle, petal_count, petal_left_border, petal_right_border)

        my_frame.exitonclick()
    except KeyboardInterrupt:
        print 'KeyboardInterrupt'
