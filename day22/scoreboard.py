from ctypes import alignment
from turtle import Turtle
alignment = "center"
FONT = ("Atiel", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0,270)
        self.write(f"score: {self.score}",align=alignment,font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", align=alignment,  font=FONT)
        
        # the red fox jumpes over the yellow fance 