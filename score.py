from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

with open("data.txt") as data:
    legacy_score = int(data.read())

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.high_score = legacy_score
        self.penup()
        self.color("yellow")
        self.ht()
        self.post_score()
        self.update_score()


    def post_score(self):
        self.goto(x=0, y=265)

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} | High Score = {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        self.score += 1

    def reset(self):
        final_score = self.score - 1
        if final_score > self.high_score:
            self.high_score = final_score
            with open("data.txt", mode='w') as new_score_data:
                new_score_data.write(str(final_score))
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER! FINAL SCORE: {self.score - 1}", align=ALIGNMENT, font=FONT)
