from turtle import Turtle
from screen import screen

STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        screen.tracer(0)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POINT)
        self.setheading(90)
        screen.update()
        screen.tracer(1)

    def move_turtle(self) -> None:
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self) -> None:
        self.goto(STARTING_POINT)

    def has_collided(self, cars) -> bool:
        for car in cars:
            distance = self.distance(car)
            if distance < 15:
                return True
        return False

    def has_finished(self) -> bool:
        if self.ycor() >=280:
            return True
        return False
