from turtle import Screen,  Turtle

class Paddle(Turtle):
    def __init__(self,player_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(player_position)

    def move_up(self):
        self.goto(self.xcor(), (self.ycor() + 20))

    def move_down(self):
       self.goto(self.xcor(), (self.ycor() - 20))