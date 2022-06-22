from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.setx(x)
            self.snakes.append(snake)
            x -= 20

    def grow_snake(self):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.setx(self.snakes[len(self.snakes) - 1].pos()[0])
        snake.sety(self.snakes[len(self.snakes) - 1].pos()[1])
        self.snakes.append(snake)

    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake - 1].pos()[0]
            new_y = self.snakes[snake - 1].pos()[1]
            self.snakes[snake].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]
