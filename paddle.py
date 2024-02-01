from turtle import Turtle
import time
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.penup()
        self.speed("fastest")
        x_cor = 350
        if side == "left":
            x_cor *= -1
        else:
            pass
        self.goto(x_cor, 0)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.setheading(UP)

    def move_up(self):
        time.sleep(.01)
        self.setheading(UP)
        self.forward(50)

    def move_down(self):
        time.sleep(.01)
        self.setheading(DOWN)
        self.forward(50)
