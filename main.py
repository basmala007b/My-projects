import turtle
import time
from collections import deque
from snake import Snake
from food import Food
from obs import Obs

#---------------------------
screen = turtle.Screen()
screen.title("Z Smart Snake")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

#---------------------------------
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))


#---------------------------------
def update_score():  #***********
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))
# التحكم في سرعة العرض وإخفاء marker
marker_visible = False
mv = False
s=False
def toggle_marker_visibility():
    global marker_visible
    marker_visible = True
    screen.update()
def b():
    global mv
    mv = True
    screen.update()

def sl():
    global s
    s = True


# BFS Algorithm
def bfs(start, goal, obs):
    queue = deque([start])
    visited = {start: None}
    directions = [(20, 0), (-20, 0), (0, 20), (0, -20)]
    screen.tracer(0)
    while queue:
        current = queue.popleft()  #طول ما عندنا اماكن بنسحب اول مكان
        # ---------------------------------------------------------------------------
        marker = turtle.Turtle("square")
        marker.color("green")
        marker.shapesize(0.5, 0.5)
        marker.penup()
        marker.goto(current)
        if marker_visible:
            print("marker.showturtle()")
        else :
            marker.hideturtle()
            marker.clear()

        # ----------------------------------------------
        m = turtle.Turtle("square")
        m.color("green1")
        m.shapesize(0.5)
        m.penup()
        m.goto(current)
        if mv:
            m.showturtle()
        else:
            m.hideturtle()
            m.clear()

        # ----------------------------------------------
        if s:
            time.sleep(0.5)
            m.shapesize(1)
            m.shape("circle")
            m.color("red")

        screen.update() ###########################################################
        m.hideturtle()
        #-------------------------------------------------------------
        if current == goal:  #هل وصلنا لل goal ??
            marker.hideturtle()  # Hide the turtle's outline
            screen.update()
            path = []
            while current:
                path.append(current)  # add node in list to draw our path
                current = visited[current]  #بنحطه ف ال visited
            return path[::-1]  # reversed path

        for direction in directions:
            x_new = current[0] + direction[0]  # current[{0}=ur pos in x ,{1}=ur pos in y ]
            y_new = current[1] + direction[1]  # direction[{0}=ur new pos in x ,{1}=ur new pos in y ]
            neighbor = (x_new, y_new)
            if neighbor not in visited and neighbor not in obs and -300 < neighbor[0] < 300 and -300 < neighbor[
                1] < 300:
                queue.append(neighbor)
                visited[neighbor] = current

    return None


def show_path(path):  #*************
    path_turtles = []
    for step in (path[2:-1]):
        path_shape = turtle.Turtle("circle")
        path_shape.color("white")
        path_shape.penup()
        path_shape.goto(step)
        path_shape.shapesize(0.5, 0.5)
        path_turtles.append(path_shape)
    return path_turtles


def clear_path(path_turtles):
    for shape in path_turtles:
        shape.hideturtle()


#------------------------------------
snake = Snake()
obs = Obs()
food = Food(obs, snake)


#------------------------------------
def game():
    obs_positions = set(obs.get_positions())  # set to prevent dublication
    snake_positions = set(snake.get_positions())
    all_obs = obs_positions | snake_positions  # union
    food_position = food.position()
    snake_head_position = snake.head.position()

    path = bfs(snake_head_position, food_position, all_obs)
    if path:
        path_turtles = show_path(path)

        screen.update()
        screen.ontimer(lambda: clear_path(path_turtles))  # :) lambda

    if path and len(path) > 1:
        snake.move(path[1:2])  ###########
    else:
        snake.move()

    if snake.head.distance(food.food) < 20:
        food.appear()
        snake.extend()
        update_score()

    if snake.head.position() in all_obs:
        print("Game Over")
        return

    screen.update()
    screen.ontimer(game)

screen.listen()
screen.onkey(toggle_marker_visibility, "x")
screen.onkey(b, "z")
screen.onkey(sl, "c")

screen.ontimer(game)
screen.mainloop()
