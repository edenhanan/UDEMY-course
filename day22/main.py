from turtle import Screen,  Turtle
from scoreboard import Scoreboard

from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

player_1 = Paddle((370,0))
player_2 = Paddle((-370,0))
scoreboard = Scoreboard() 

ball = Ball()
screen.listen()
screen.onkeypress(fun=player_1.move_up, key="Up")
screen.onkeypress(fun=player_1.move_down, key="Down")
screen.onkeypress(fun=player_2.move_up, key="w")
screen.onkeypress(fun=player_2.move_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.movment_speed)
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bouncey()

    if ball.distance(player_1) < 50 and ball.xcor() > 350 or ball.distance(player_2) < 50 and ball.xcor() < -350:
        ball.bouncex()


    if ball.xcor() > 390:
        ball.point()
        scoreboard.Left_point()

    if ball.xcor() < -390:
        ball.point()
        scoreboard.Right_point()

screen.exitonclick()

