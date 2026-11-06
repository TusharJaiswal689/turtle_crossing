from car_manager import CarManager
from turtle_object import TurtlePlayer
from ui import UIManager
from screen import screen

class GameEngine:
    def __init__(self):
        self.turtle = TurtlePlayer()
        self.car = CarManager()
        self.ui = UIManager()
        self.current_level = 1
        self.is_game_on = True

        self.setup_game()

    def setup_game(self):
        self.ui.write_menu("Press SPACE to start the game.")
        screen.listen()
        screen.onkey(None, "w")
        screen.onkey(self.start_game, "space")

    def start_game(self):
        self.ui.menu_writer.clear()
        self.ui.write_level(self.current_level)
        screen.onkey(None, "space")

        self.is_game_on = True
        self.game_loop()

    def game_loop(self):
        if not self.is_game_on:
            return

        screen.tracer(0)
        self.car.spawn_car()
        self.car.move_car()
        screen.onkey(self.turtle.move_turtle, "w")

        if self.turtle.has_finished():
            self.current_level += 1
            self.turtle.reset_turtle()
            self.ui.write_level(self.current_level)
            self.car.increase_speed()

        if self.turtle.has_collided(self.car.cars):
            self.is_game_on = False
            self.ui.write_game_over("GAME OVER!", "Press 'r' to restart the game.")
            screen.onkey(None, "w")
            screen.onkey(self.restart_game, "r")
            screen.update()
            return

        screen.update()
        screen.ontimer(self.game_loop, 100)

    def restart_game(self):
        screen.tracer(0)
        screen.onkey(None, "r")
        self.ui.game_over_writer.clear()
        self.car.reset_cars()

        self.turtle.reset_turtle()
        self.current_level = 1
        self.car.current_speed = 10
        screen.update()
        self.setup_game()