from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,posX,posY):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.shape ("square")
        self.color ("white")
        self.shapesize (stretch_wid=5, stretch_len=1)
        self.penup ()
        self.goto (self.posX, self.posY)

    def goUp (self):
        newY = self.ycor () + 20
        if (newY < 250 and newY > -250):
            self.goto (self.xcor (), newY)

    def goDown (self):
        newY = self.ycor () - 20
        if (newY < 250 and newY > -250):
            self.goto (self.xcor (), newY)