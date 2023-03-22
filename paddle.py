from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')

        self.penup()
        # self.resizemode('user')
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.goto(350, 0)
        # self.setheading(90)
        self.speed(1)

    def move_down(self):
        # self.setheading(270)
        # self.forward(20)
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)

    def move_up(self):
        # self.setheading(90)
        # self.forward(20)
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)
