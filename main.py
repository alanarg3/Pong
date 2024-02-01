# project breakdown:
# 1. class for paddles
# 2. class for the ball
# 3. class for the score
# 4. class for the lines on the display

from turtle import Screen
import paddle
import ball
import scorekeeper
import random
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
paddle_1 = paddle.Paddle("right")
paddle_2 = paddle.Paddle("left")
ball = ball.Ball()
UP = 90
DOWN = 180
screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")
score_p1 = scorekeeper.Scorekeeper(1, 100)
score_p2 = scorekeeper.Scorekeeper(2, -100)
playing = True

while score_p2.score <= 9 and score_p1.score <= 9:
    screen.update()
    ball.move()
    # something is up?
    if ball.ycor() > 280 or ball.ycor() < -280:
        if ball.heading() >= 330:
            ball.setheading(360 - ball.heading())
        else:
            ball.setheading(360-ball.heading())
    if ball.xcor() >= 340 or ball.xcor() <= -340:
        if ball.distance(paddle_1) <= 55 or ball.distance(paddle_2) <= 55:
            if ball.heading() <= 180:
                ball.setheading(180-ball.heading())
            else:
                ball.setheading((180-ball.heading())+360)
    if ball.xcor() >= 345:
        ball.reset(2)
        score_p2.keep_score()
        score_p2.write_score()
        time.sleep(1)
    elif ball.xcor() <= -345:
        ball.reset(1)
        score_p1.keep_score()
        score_p1.write_score()
        time.sleep(1)

if score_p1.score >= score_p2.score:
    winner = "PLAYER 1"
else:
    winner = "PLAYER 2"

result = scorekeeper.Winning()
result.win(winner)

screen.exitonclick()
