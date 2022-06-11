from turtle import Turtle,Screen
from Paddle import Paddle
from Ball import Ball

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(1000,600)
screen.title("PingPong")
screen.tracer(0)

leftPaddle = Paddle(-450,0)
rightPaddle = Paddle(450,0)

ball = Ball()

screen.listen()
screen.onkeypress(rightPaddle.goUp,"Up")
screen.onkeypress(rightPaddle.goDown,"Down")
screen.onkeypress(leftPaddle.goUp,"w")
screen.onkeypress(leftPaddle.goDown,"s")


gameIsOn = True

while gameIsOn:
    time.sleep(.025)
    screen.update()
    ball.move()

    if(ball.ycor() >280 or ball.ycor() <-280):
        ball.bounceY()
    
    if( ball.distance(rightPaddle) <50 and ball.xcor() > 425):
        ball.bounceX()
    elif( ball.distance(leftPaddle) <50 and ball.xcor() <-425):
        ball.bounceX()













