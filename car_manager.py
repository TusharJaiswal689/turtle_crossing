from turtle import Turtle
from screen import screen
import random

SPEED_INCREMENT = 5
COLORS = ["red", "green", "yellow", "blue", "purple", "orange"]

class CarManager():
    def __init__(self):
        self.cars = []
        self.car_pool = []
        self.current_speed = 10
        
    def spawn_car(self):
        if random.randint(1, 6) != 1:
            return
        if self.car_pool:
            car = self.car_pool.pop()
        else:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()

        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-230, 230))
        car.setheading(180)
        car.showturtle()
        self.cars.append(car)
            

    def move_car(self):
        active_cars = []

        for car in self.cars:
            car.forward(self.current_speed)

            if car.xcor() <-300:
                car.hideturtle()
                self.car_pool.append(car)
            else:
                active_cars.append(car)

        self.cars[:] = active_cars

    def increase_speed(self):
        self.current_speed += SPEED_INCREMENT

    def reset_cars(self):
        for car in self.cars:
            car.hideturtle()
            self.car_pool.append(car)
        self.cars.clear()


