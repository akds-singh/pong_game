from turtle import Turtle, Screen


class Padle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')

        self.penup()
        # self.resizemode('user')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(350, 0)
        self.setheading(90)
        self.speed(speed='fastest')

    def move_down(self):
        self.setheading(270)
        self.forward(20)

    def move_up(self):
        self.setheading(90)
        self.forward(20)