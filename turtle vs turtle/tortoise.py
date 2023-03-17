from turtle import Turtle
from random import randrange

MOVE_DISTANCE=40

class Tortoise(Turtle):
    def __init__(self,color):
        super().__init__()
        self.pencolor(color)
        self.shape("turtle")
        self.pensize(4)
    def initial_pos(self,position):
        self.penup()
        self.goto(position)
        self.pendown()
    def move(self):
        rand_num=randrange(0, 4)
        self.setheading(rand_num*90)
        self.fd(MOVE_DISTANCE)
