from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.speed('slowest')
        self.penup()
        self.ball_speed = 0.1
        self.x_cor = 10
        self.y_cor = 10

    def move(self):
        new_xcor = self.xcor() + self.x_cor
        new_ycor = self.ycor() + self.y_cor
        self.goto(new_xcor, new_ycor)

    def bounce_from_wall(self):
        # self.x_cor = 20
        # self.y_cor = -20
        self.y_cor *= -1

    def bounce_from_paddle(self):
        # new_xcor = self.xcor() - 20
        # new_ycor = self.ycor() - 20
        # self.goto(new_xcor, new_ycor)
        self.x_cor *= -1
        self.ball_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.x_cor *= -1
        self.ball_speed = 0.1


    # def bounce_from_left_paddle(self):
    #     # new_xcor = self.xcor() - 20
    #     # new_ycor = self.ycor() - 20
    #     # self.goto(new_xcor, new_ycor)
    #     self.x_cor = +20
    #     self.y_cor = +20

    # def bounce_from_down_wall(self):
    #     self.x_cor = -20
    #     self.y_cor = +20



    # def increase_speed(self):
    #     self.ball_speed += 1
    #     self.x_cor = self.ball_speed
    #     self.y_cor = self.ball_speed
