from hashlib import new
from turtle import Turtle, Screen
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Origin Snakes")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect eat food or not
    if snake.head.distance(food) < 25:
        food.refresh_location()
        snake.extend_snake()
        scoreboard.plus_score()

    # Detect collision with border
    if snake.head.xcor() > 400 or snake.head.xcor() < -400 or snake.head.ycor() > 400 or snake.head.ycor() < -400:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for body in snake.bodys[1:]:
        if snake.head.distance(body) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
