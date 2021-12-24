from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(-260, 260)
        self.write(arg=f"Level: {self.level}", font=FONT, align="left")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=FONT, align="center")

    def inc_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

