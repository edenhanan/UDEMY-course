from turtle import Screen,  Turtle

moving_speed = 15
starting_position = [(0,0), (-20,0), (-40,0), (-60,0)]
up = 90
down = 270
right = 0
left = 180
snake_color = "white"

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_segment(self, position):
        self.seg_n = len(self.segments) -1
        self.segments.append(Turtle("square"))
        self.segments[self.seg_n].color(snake_color)
        self.segments[self.seg_n].penup()

    def create_snake(self):
        for i in starting_position:
            self.create_segment(i)
            # self.segments[i].goto(starting_position[i])

    def extend(self):
        self.create_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1, 0 ,-1):
            x_cor = self.segments[seg-1].xcor()
            y_cor = self.segments[seg-1].ycor()
            self.segments[seg].goto(x_cor, y_cor)
        self.head.forward(moving_speed)

    def move_left(self):
        self.head.left(90)

    def move_right(self):
        self.head.right(90)

    # def restart(self):
    #     self.