from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    if snake.head.distance(food) < 15:
        food.random_location()
        scoreboard.update_score()
        snake.grow_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for s in snake.snakes[1:]:
        if snake.head.distance(s) < 15:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
