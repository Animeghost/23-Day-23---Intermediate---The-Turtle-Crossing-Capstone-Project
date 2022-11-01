from turtle import Turtle
from random import Random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self):
        
        self.rand = Random()
        self.cars = []
        self.ki = 5
        self.car_creator()
        
    def car_creator(self):
        if self.rand.randint(1,6) == 6:
        
            color = self.rand.choice(COLORS)
            car=Turtle()
            car.shape('square')
            car.penup()
            car.color(color)
            car.resizemode('user')
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.goto(x=290, y=self.rand.randint(-250,250))
            
            self.cars.append(car)
       
            
    def car_move(self):
        for item in self.cars:
            
            item.back(self.ki)
        
    def more_cars(self):
         
        self.car_creator()
        
    
    def refresh(self):
        self.ki += MOVE_INCREMENT