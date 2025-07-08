from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from centerline import draw_center_line
import time

screen = Screen()
screen.title("PONG!")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle1 = Paddle((-390, 0))
paddle2 = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

WINNING_SCORE = 5

draw_center_line()

left_up = False
left_down = False
right_up = False
right_down = False

def left_up_press():
    global left_up
    left_up = True

def left_up_release():
    global left_up
    left_up = False

def left_down_press():
    global left_down
    left_down = True

def left_down_release():
    global left_down
    left_down = False

def right_up_press():
    global right_up
    right_up = True

def right_up_release():
    global right_up
    right_up = False

def right_down_press():
    global right_down
    right_down = True

def right_down_release():
    global right_down
    right_down = False

def move_paddles():
    if left_up:
        paddle1.go_up()
    if left_down:
        paddle1.go_down()
    if right_up:
        paddle2.go_up()
    if right_down:
        paddle2.go_down()
    screen.ontimer(move_paddles, 20)

screen.listen()
screen.onkeypress(left_up_press, "w")
screen.onkeyrelease(left_up_release, "w")
screen.onkeypress(left_down_press, "s")
screen.onkeyrelease(left_down_release, "s")
screen.onkeypress(right_up_press, "Up")
screen.onkeyrelease(right_up_release, "Up")
screen.onkeypress(right_down_press, "Down")
screen.onkeyrelease(right_down_release, "Down")
move_paddles()

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (350 < ball.xcor() < 380 and ball.distance(paddle2) < 50) or \
       (-350 > ball.xcor() > -380 and ball.distance(paddle1) < 50):
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
        if scoreboard.left_score >= WINNING_SCORE:
            scoreboard.game_over("Left Player")
            game_on = False
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
        if scoreboard.right_score >= WINNING_SCORE:
            scoreboard.game_over("Right Player")
            game_on = False

screen.exitonclick()