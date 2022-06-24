from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.penup()
        self.color("yellow")
        self.ht()
        self.post_score()
        self.update_score()

    def post_score(self):
        self.goto(x=0, y=265)

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER! FINAL SCORE: {self.score - 1}", align=ALIGNMENT, font=FONT)
