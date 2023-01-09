COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager():
    
    def __init__(self):
        self.all_cars = []

    
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            create_car = Turtle('square')
            create_car.shapesize(stretch_wid = 1, stretch_len=2)
            create_car.color(random.choice(COLORS))
            create_car.penup()
            create_car.setheading(180)
            random_y = random.randint(-250, 250)
            create_car.goto(x=300, y=random_y)
            self.all_cars.append(create_car)
            
    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
            
    def update_speed(self):
        for car in self.all_cars:
            new_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
            car.forward(new_speed)