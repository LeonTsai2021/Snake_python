from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("red")
        self.speed("fastest")
        self.refresh_location()
        
    def refresh_location(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x, random_y)
