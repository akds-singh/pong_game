from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

turtle = Turtle()
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle()
right_paddle.goto(350, 0)
left_paddle = Paddle()
left_paddle.goto(-350, 0)
ball = Ball()

right_paddle_score = ScoreBoard()
right_paddle_score.goto(200, 250)
left_paddle_score = ScoreBoard()
left_paddle_score.goto(-200, 250)

screen_divider = ScoreBoard()
screen_divider.screen_divider()

screen.listen()
screen.onkeypress(fun=right_paddle.move_down, key='Down')
screen.onkeypress(fun=right_paddle.move_up, key='Up')
screen.onkeypress(fun=left_paddle.move_down, key='s')
screen.onkeypress(fun=left_paddle.move_up, key='w')

is_game_on = True
up_wall_touched = False
down_wall_touched = False
ball_hit_left_paddle = False
ball_hit_right_paddle = False
while is_game_on:
    screen.update()

    time.sleep(ball.ball_speed)
    ball.move()

    # Detection when ball cross up and down screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_from_wall()
        print('from wall')

    # Detecting te collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_from_paddle()
        print('from paddle')
        print('ball speed:', ball.ball_speed)
        print('x:', ball.x_cor)
        print('y:', ball.y_cor)

        # ball.increase_speed()
        print(ball.ball_speed)

    # Displaying the score of the players
    if ball.xcor() > 400 or ball.xcor() < -400:
        print('ball over boudry')
        if ball.xcor() > 400:
            left_paddle_score.count_score()
            left_paddle_score.clear()
            left_paddle_score.display()
        if ball.xcor() < -400:
            right_paddle_score.count_score()
            right_paddle_score.clear()
            right_paddle_score.display()

        ball.refresh()

    # # another ways to do it
    # if not up_wall_touched and not ball_hit_right_paddle:
    #
    #     time.sleep(0.1)
    #     ball.move()
    #     print('ball is moving')
    #     if ball.ycor() > 280:
    #         up_wall_touched = True
    # elif up_wall_touched and not ball_hit_right_paddle:
    #     print('ball is from up bouncing')
    #     time.sleep(0.1)
    #     ball.bounce_from_wall()
    #     if ball.distance(right_paddle) < 40 and ball.xcor() > 320:
    #         print('ball touched right paddle')
    #         ball_hit_right_paddle = True
    #
    # elif up_wall_touched and ball_hit_right_paddle and not down_wall_touched:
    #     print('ball hits right paddle')
    #     time.sleep(0.1)
    #     ball.bounce_from_paddle()
    #     if ball.ycor() < -280:
    #         print('ball touched down wall')
    #         down_wall_touched = True
    # elif down_wall_touched and not ball_hit_left_paddle:
    #     time.sleep(0.1)
    #     ball.bounce_from_down_wall()
    #     if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
    #         print('ball hit left paddle')
    #         ball_hit_left_paddle = True
    # elif ball_hit_left_paddle:
    #     print('testing')
    #     time.sleep(0.1)
    #     ball.move()
    #     if ball.ycor() > 290:
    #         print('up wall touched')
    #         up_wall_touched = True
    #         ball_hit_right_paddle = False

    # # another way to do it
    # if not ball.ycor() > 200 or not ball.ycor() <-200:
    #     time.sleep(0.1)
    #     ball.move()
    # if ball.ycor() > 280 :
    #
    #     ball.bounce_from_up_wall()
    #
    # if ball.ycor() < -280:
    #     ball.bounce_from_down_wall()
    #     print('hit wall')
    # if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
    #     ball.bounce_from_right_paddle()
    #     print('hit paddle')
    #
    # if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
    #     ball.bounce_from_left_paddle()
    #     print('hit paddle')


print(right_paddle.shapesize())
screen.exitonclick()

