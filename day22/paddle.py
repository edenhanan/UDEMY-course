from turtle import Screen,  Turtle

class Paddle(Turtle):
    def __init__(self,player_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(player_position)
        self.paddle_speed = 30

    def move_up(self):
        self.goto(self.xcor(), (self.ycor() + self.paddle_speed))

    def move_down(self):
       self.goto(self.xcor(), (self.ycor() - self.paddle_speed))