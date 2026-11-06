from turtle import Turtle

STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POINT)
        self.setheading(90)

    def move_turtle(self) -> None:
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self) -> None:
        self.goto(STARTING_POINT)

    def has_collided(self, cars) -> bool:
        player_width = 20
        player_height = 20
        car_width = 40
        car_height = 20

        for car in cars:
            overlaps_horizontally = abs(self.xcor() - car.xcor()) < (
                player_width + car_width
            ) / 2
            overlaps_vertically = abs(self.ycor() - car.ycor()) < (
                player_height + car_height
            ) / 2

            if overlaps_horizontally and overlaps_vertically:
                return True

        return False

    def has_finished(self) -> bool:
        if self.ycor() >=280:
            return True
        return False
