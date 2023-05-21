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
        self.Left_score = 0
        self.Right_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        
        self.goto(-100,200)
        self.write(self.Left_score,align=alignment,font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.Right_score,align=alignment,font=("Courier",80,"normal"))

    def Left_point(self):
        self.Left_score += 1
        self.update_scoreboard()


    def Right_point(self):
        self.Right_score += 1
        self.update_scoreboard()