from turtle import Turtle
from screen import screen

VISUAL_LOS = 280

class UIManager():
    def __init__(self):
        self.writer_turtles = []
        screen.tracer(0)
        self.menu_writer = Turtle()
        self.writer_turtles.append(self.menu_writer)
        self.game_over_writer = Turtle()
        self.writer_turtles.append(self.game_over_writer)
        self.level_writer = Turtle()
        self.writer_turtles.append(self.level_writer)
        for turtle in self.writer_turtles:
            turtle.hideturtle()
            turtle.penup()
            turtle.color("black")
        screen.update()
        screen.tracer(1)
        self.draw_boundary()

    def draw_boundary(self):
        screen.tracer(0)

        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        writer.color("black")
        writer.goto(-VISUAL_LOS, -VISUAL_LOS)
        writer.setheading(90)
        writer.pendown()

        screen.update()
        screen.tracer(1)

        for _ in range(4):
            writer.forward(VISUAL_LOS * 2)
            writer.setheading(writer.heading() - 90)
        writer.penup()

    def write_menu(self, msg: str):
        self.menu_writer.goto(0, 200)
        self.menu_writer.write(msg, align="center", font=("Courier", 12, "normal"))

    def write_level(self, level: int):
        self.level_writer.clear()
        self.level_writer.goto(0, 280)
        self.level_writer.write(f"Level: {level}", align="center", font=("Courier", 8, "normal") )

    def write_game_over(self, msg1: str, msg2: str):
        self.game_over_writer.goto(0, 180)
        self.game_over_writer.color("red")
        self.game_over_writer.write(msg1, align="center", font=("Courier", 24, "normal"))
        self.game_over_writer.goto(0, 150)
        self.game_over_writer.color("black")
        self.game_over_writer.write(msg2, align="center", font=("Courier", 12, "normal"))