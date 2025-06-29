from turtle import Turtle, Screen
import random

gif = "D:/Me/ai project/Av.gif"
s = Screen()
s.addshape(gif)


class Food:
    def __init__(self, obs_pos, snake_pos):
        self.obs_pos = obs_pos
        self.snake_pos = snake_pos
        self.food = Turtle(gif)
        self.food.penup()
        self.appear()

    def appear(self):
        while True:
            #x = random.randint(-150, 150) // 20 * 20
            #y = random.randint(-150, 150) // 20 * 20  # to reach to the near point to our division =20 convert 126 -> 120
            x = random.randint(-70, 70) // 20 * 20  # 20,40,60,80,100,120
            y = random.randint(-70, 70) // 20 * 20
            new_position = (x, y)
            obs_positions = self.obs_pos.get_positions()
            snake_positions = self.snake_pos.get_positions()

            if new_position not in obs_positions and new_position not in snake_positions:
                self.food.goto(new_position)
                break

    def position(self):
        return self.food.position()







