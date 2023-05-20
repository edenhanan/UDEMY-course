from turtle import Screen,  Turtle

from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")

player_1 = Paddle()
screen.listen()
screen.onkeypress(fun=player_1.move_up, key="Up")
screen.onkeypress(fun=player_1.move_down, key="Down")

screen.exitonclick()

