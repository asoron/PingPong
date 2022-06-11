from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xMove = 5
        self.yMove = 5

    def move(self):
        new_x = self.xcor() + self.xMove
        new_y = self.ycor() + self.yMove
        self.goto(new_x,new_y)

    def bounceY(self):
        self.yMove *= -1

    def bounceX(self):
        self.xMove *= -1