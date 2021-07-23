# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:18:10 2018

@author: lixin (Justin Lee)
"""
import random
from math import sqrt
from turtle import *

DEBUG = False
BRANCH_LENGTH = 60
SUN_RADIUS = 40
MAGIC = 12


class FloweringTree:
    def __init__(self):
        self.petal_count = 0
        self.petal_left_border = 0.0
        self.petal_right_border = 0.0
        self.turtle = Turtle()
        self.frame = Screen()
        if DEBUG:
            self.frame.tracer(0, 0)
        else:
            self.frame.tracer(3, 0)
        self.frame.bgcolor('wheat')
        self.turtle.up()

    def tree(self, branch_len):
        if branch_len > 3:
            if 8 <= branch_len <= 12:
                if random.randint(0, 2) == 0:
                    self.turtle.color('snow')
                else:
                    self.turtle.color('lightcoral')
                self.turtle.pensize(branch_len / 3)
            elif branch_len < 8:
                self.petal_count += 1
                cur_x = self.turtle.pos()[0]
                if cur_x < 0:
                    self.petal_left_border = min(self.petal_left_border, cur_x)
                else:
                    self.petal_right_border = max(self.petal_right_border, cur_x)
                if random.randint(0, 1) == 0:
                    self.turtle.color('snow')
                else:
                    self.turtle.color('lightcoral')
                self.turtle.pensize(branch_len / 2)
            else:
                self.turtle.color('sienna')
                self.turtle.pensize(branch_len / 10)

            # Draw the branch/leaf
            self.turtle.down()
            self.turtle.forward(branch_len)
            self.turtle.up()

            random_angle = 3 + 2 * MAGIC * random.random()
            random_length = MAGIC * random.random()

            self.turtle.right(random_angle)
            self.tree(branch_len - random_length)
            self.turtle.left(2 * random_angle)
            self.tree(branch_len - random_length)
            self.turtle.right(random_angle)

            # return to the root of this chile tree
            self.turtle.up()
            self.turtle.backward(branch_len)

    def petal_field(self, count, left_border=-100.0, right_border=100.0):
        middle = (right_border + left_border) / 2
        frame_width = (right_border - left_border) / 3
        depth = int(sqrt(frame_width))
        _start_pos = self.turtle.pos()
        start_pos = (middle, _start_pos[1] + depth / 2 - BRANCH_LENGTH / 10)
        self.turtle.goto(start_pos)

        for _ in range(count):
            random_width = frame_width - 2 * frame_width * random.random()
            random_depth = depth - 2 * depth * random.random()
            self.turtle.forward(random_depth)
            self.turtle.left(90)
            self.turtle.forward(random_width)
            self.turtle.down()
            if random.randint(0, 1) == 0:
                self.turtle.color("snow")
            else:
                self.turtle.color("lightcoral")
            rand_size = random.random()
            self.turtle.pensize(2.5 * rand_size)
            self.turtle.begin_fill()
            self.turtle.circle(rand_size)
            self.turtle.end_fill()
            self.turtle.up()
            self.turtle.right(90)
            self.turtle.goto(start_pos)
        # Repaint the covered branch
        self.turtle.goto(_start_pos)
        self.turtle.color('sienna')
        self.turtle.pensize(BRANCH_LENGTH // 10)
        self.turtle.down()
        self.turtle.forward(BRANCH_LENGTH)
        self.turtle.up()

    def the_sun(self, radius=30):
        start_pos = self.turtle.pos()
        self.turtle.forward(500)
        self.turtle.left(90)
        self.turtle.forward(300)
        self.turtle.down()
        self.turtle.color('red')
        self.turtle.begin_fill()
        self.turtle.circle(radius)
        self.turtle.end_fill()
        self.turtle.color('lightcoral')
        self.turtle.up()
        self.turtle.right(90)
        self.turtle.goto(start_pos)

    def signature(self):
        start_pos = self.turtle.pos()
        self.turtle.color('sienna')
        self.turtle.write("Made with ❤ by Justin Lee!", font=("Futura", 16, "normal"))
        self.turtle.goto(start_pos)

    def draw(self):
        try:
            self.turtle.left(90)
            self.turtle.backward(250)
            self.the_sun(SUN_RADIUS)
            self.tree(BRANCH_LENGTH)
            self.petal_count = self.petal_count // (int(sqrt(2 * MAGIC)))
            self.petal_field(self.petal_count, self.petal_left_border, self.petal_right_border)
            self.turtle.backward(100)
            self.signature()
            self.turtle.color('wheat')
            self.turtle.down()
            self.turtle.forward(20)
            self.frame.exitonclick()
        except KeyboardInterrupt:
            print('Keyboard Interrupt.')


if __name__ == '__main__':
    flowering_tree = FloweringTree()
    flowering_tree.draw()
