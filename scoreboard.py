from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 270)
        self.write(f"Score: {self.score}   High Score: {self.highscore}", move=False, align="center", font=('Arial', 15, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}   High Score: {self.highscore}", move=False, align="center", font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", move=False, align="center", font=('Arial', 15, 'normal'))
