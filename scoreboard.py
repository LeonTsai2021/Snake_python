from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.color("yellow")
        self.penup()
        self.goto(0, 350)
        self.write(f"SCORE: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT,
                   font=FONT)
        self.hideturtle()

    def plus_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT,
                   font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT,
                   font=FONT)
