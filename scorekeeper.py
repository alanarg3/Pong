from turtle import Turtle
FONT = "bauhaus 93"
SIZE = 100
TYPE = "bold"


class Scorekeeper(Turtle):

    def __init__(self, player_num, x_of_score):
        super().__init__()
        self.penup()
        self.color("white")
        self.sety(150)
        self.setx(x_of_score)
        self.score = 0
        self.name = f"PLAYER {player_num}"
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score}", False, "center", (FONT, SIZE, TYPE))

    def keep_score(self):
        self.score += 1


class Winning(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.sety(0)
        self.setx(0)

    def win(self, winning_player):
        self.write(f"     GAME OVER\n  {winning_player} WINS!", False, "center", (FONT, 32, TYPE))
