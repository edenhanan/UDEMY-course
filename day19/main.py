from turtle import Turtle,Screen, exitonclick
import turtle

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(15)
def move_backward():
    tim.backward(10)
def turnright():
    tim.right(5)
def turnleft():
    tim.left(5)
def clear_c():
    tim.clear()
    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turnright)
screen.onkey(key="a", fun=turnleft)
screen.onkey(key="c", fun=clear_c)
screen.exitonclick()
