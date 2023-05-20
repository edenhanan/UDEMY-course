from turtle import Screen,  Turtle, ycor
import time  as tm


from snake import Snake
from food import Food
from scoreboard import Scoreboard

distance_from_end = 290
sleep_time = 0.3


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()
screen.listen()
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
# screen.onkey(key="R", fun=snake.restart)

game_is_on=True
while game_is_on:
    screen.update()
    tm.sleep(sleep_time/(scoreboard.score+0.5))
    snake.move()

    if snake.head.distance(food) < 15: # eat the food
        food.refresh()
        scoreboard.add_point()
        snake.extend()

#  detect collisions with the wall
    if snake.head.xcor() > distance_from_end or snake.head.ycor() > distance_from_end or snake.head.xcor() < -distance_from_end or snake.head.ycor() < -distance_from_end :
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()

