from turtle import Screen, Turtle, color
import random
import turtle

color_bank = ["red", "green", "blue", "dark green", "light blue", "LightGreen"]
timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(10)
timmy.speed(0)
turtle.colormode(255)
# timmy.color("darkorchid")
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# for i in range(50):
#     if i % 2 == 0:
#         timmy.pendown()
#     else:
#         timmy.penup()
#     timmy.forward(10)
# for i in range(3,10):
#     current_color = random.choice(color_bank)
#     timmy.color(current_color)
#     angle = 360/i
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(angle)
def random_walk():
    diraction = random.choice([1, 2, 3, 4])
    timmy.right(90*diraction)
    timmy.forward(50)

n_random = random.randint(10, 100)

for i in range(n_random):
    random_walk()
    R_random = random.randint(0,255)
    G_random = random.randint(0,255)
    B_random = random.randint(0,255)
    timmy.color(R_random, G_random, B_random)










screen = Screen()
screen.exitonclick()