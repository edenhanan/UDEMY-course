from turtle import Turtle,Screen, exitonclick, position
import random
import turtle

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle would win this race? Enter a color: ")
colors = ["red", "green", "orange","yellow", "blue", "purple"]
race_turtle = []
position = -150

finishline = Turtle(shape="turtle")
finishline.penup()
finishline.goto(460,position)
finishline.pd()
finishline.left(90)
finishline.forward(300)


for i in range(6):
    race_turtle.append(Turtle(shape="turtle"))
    race_turtle[i].color(colors[i])
    race_turtle[i].penup()
    race_turtle[i].goto(-450,position)
    position += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for i in race_turtle:
        rand_distance = random.randint(1,10)
        i.forward(rand_distance)
        if i.xcor() > 460:
            is_race_on = False
            wining_turtle = i.pencolor()
            if user_bet == wining_turtle:
                print(f"You've won! the {wining_turtle} turtle is the winner")
            else:
                print(f"You've lost! the {wining_turtle} turtle is the winner")
screen.exitonclick()