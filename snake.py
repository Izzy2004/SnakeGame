from turtle import Turtle
MOVE_DISTANCE = 20
INITIAL_SNAKE_SIZE = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.initialize_snake()
        self.head = self.segments[0]
        self.move()
        self.up()
        self.down()
        self.left()
        self.right()

    def initialize_snake(self):
        y_position = 0
        x_position = 0
        position = (x_position, y_position)

        for segment in range(1, INITIAL_SNAKE_SIZE):
            box = Turtle(shape="square")
            box.penup()
            box.goto(position)
            box.color("white")
            x_position += -20
            self.segments.append(box)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)