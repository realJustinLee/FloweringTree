import turtle
import random
from turtle import *
from time import sleep

static_turtle = turtle.Turtle()
frame = turtle.Screen()


def tree(branch_len, inner_turtle):
    if branch_len > 3:
        if 8 <= branch_len <= 12:
            if random.randint(0, 2) == 0:
                inner_turtle.color('snow')
            else:
                inner_turtle.color('lightcoral')
            inner_turtle.pensize(branch_len / 3)
        elif branch_len < 8:
            if random.randint(0, 1) == 0:
                inner_turtle.color('snow')
            else:
                inner_turtle.color('lightcoral')
            inner_turtle.pensize(branch_len / 2)
        else:
            inner_turtle.color('sienna')
            inner_turtle.pensize(branch_len / 10)

        inner_turtle.forward(branch_len)
        angle_elem = 1.5 * random.random()
        inner_turtle.right(20 * angle_elem)
        length_elem = 1.5 * random.random()
        tree(branch_len - 10 * length_elem, inner_turtle)
        inner_turtle.left(40 * angle_elem)
        tree(branch_len - 10 * length_elem, inner_turtle)
        inner_turtle.right(20 * angle_elem)
        inner_turtle.up()
        inner_turtle.backward(branch_len)
        inner_turtle.down()


def petal(maxim, inner_turtle):
    for i in range(maxim):
        right_branch = 200 - 400 * random.random()
        left_branch = 10 - 20 * random.random()
        inner_turtle.up()
        inner_turtle.forward(left_branch)
        inner_turtle.left(90)
        inner_turtle.forward(right_branch)
        inner_turtle.down()
        inner_turtle.color("lightcoral")
        inner_turtle.circle(1)
        inner_turtle.up()
        inner_turtle.backward(right_branch)
        inner_turtle.right(90)
        inner_turtle.backward(left_branch)



if __name__ == '__main__':
    static_turtle = turtle.Turtle()
    my_frame = turtle.Screen()
    getscreen().tracer(5, 0)
    turtle.screensize(bg='wheat')
    static_turtle.left(90)
    static_turtle.up()
    static_turtle.backward(150)
    static_turtle.down()
    static_turtle.color('sienna')
    tree(60, static_turtle)
    petal(100, static_turtle)
    my_frame.exitonclick()
