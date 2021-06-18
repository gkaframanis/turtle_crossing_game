from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.game_over = False
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        if not self.game_over:
            self.goto(-280, 250)
            self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "normal"))
        else:
            self.goto(0, 0)
            self.write("GAME OVER", align="center", font=("Courier", 15, "normal"))

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def display_game_over(self):
        self.game_over = True
        self.update_scoreboard()
