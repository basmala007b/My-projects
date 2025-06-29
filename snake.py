import turtle
from turtle import Screen
import random

gif = "D:/Me/ai project/ha.gif"
s = Screen()
s.addshape(gif)
gif1 = "D:/Me/ai project/bod.gif"
s = Screen()
s.addshape(gif1)
class Snake:
    def __init__(self):
        self.body = []  # main list of Z snake
        self.create_snake()  # call Z main function in Z constructor
        self.head = self.body[0]  # define Z head
        self.head.color("cyan")  # define Z snake color
        self.head.shape(gif)

    def create_snake(self):
        positions = [(0, 0), (20, 0)]  # length of the snake in the beginning
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):  # create new segment
        segment = turtle.Turtle("circle")
        segment.color("green1")
        turtle.colormode(1.0)  # Set color mode to accept RGB values

        # Continuously changing RGB colors
        def dynamic_color_change():
            r, g, b = random.random(), random.random(), random.random()
            segment.color((r, g, b))
            turtle.ontimer(dynamic_color_change, 50)  # Change color every 50ms

        #dynamic_color_change()

        segment.penup()
        segment.goto(position)
        self.body.append(segment)

    def extend(self):  # just update or grow z snake
        self.add_segment(self.body[-1].position())

    def move(self, path):
        if path:
            next_position = path[0]
            for i in range(len(self.body) - 1, 0, -1):  # len(x)-1 , 0 for z end , -1 for reverse
                self.body[i].goto(self.body[i - 1].position())
            self.head.goto(next_position)
        else:
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].goto(self.body[i - 1].position())
            self.head.forward(20)

    def get_positions(self):
        return [segment.position() for segment in self.body]
