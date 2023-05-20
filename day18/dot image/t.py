from turtle import Screen, Turtle, color
import turtle
import random
import colorgram

colors = colorgram.extract("R.jpg",12)
# tim=Turtle()
# tim.speed(0)
# turtle.colormode(255)
color1 = colors[0]
rgb = color1.rgb
print(rgb[0])



# for i in range(360):
#     R_random = random.randint(0,255)
#     G_random = random.randint(0,255)
#     B_random = random.randint(0,255)
#     tim.color(R_random, G_random, B_random)
#     tim.circle(30)
#     tim.setheading(i)

#
# screen = Screen()
# screen.exitonclick()

