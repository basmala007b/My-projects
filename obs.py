import turtle
import random


class Obs:
    def __init__(self, obs_num=10):
        self.obs = []
        self.create_obs(obs_num)
        #self.start_color_change()

    def create_obs(self, n):
        for _ in range(n):
            obstacle = turtle.Turtle("square")
            obstacle.color("gray")
            obstacle.shapesize(0.75)
            obstacle.penup()
            obstacle.speed(0)
            obstacle.goto(random.randint(-300, 300) // 20 * 20, random.randint(-300, 300) // 20 * 20)
            self.obs.append(obstacle)

    def get_positions(self):
        return [obstacle.position() for obstacle in self.obs]

    def start_color_change(self):
        for obstacle in self.obs:
            self.toggle_color(obstacle)

    def toggle_color(self, obstacle):
        current_color = obstacle.color()[0]
        new_color = "black" if current_color == "gray" else "gray"
        obstacle.color(new_color)
        turtle.ontimer(lambda: self.toggle_color(obstacle), 1500)
    #def update_number_of_obs(self):
