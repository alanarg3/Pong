from turtle import Turtle
import time
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(random.randint(15,75))

    def move(self):
            self.forward(.5)

    def reset(self, who1):
        self.setpos(0,0)
        if who1 == 1:
            self.setheading(random.randint(15,75))
        else:
            self.setheading(random.randint(195,255))