from turtle import Turtle
FONT = ("Courier", 16, "normal")
ALING ='right'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        
        self.penup()
        self.goto(x=-150,y=260)
        self.score_num = 0
        self.score()

    def score(self):
        """prints out the altered score (score_num)"""
        self.clear()
        self.write(arg=f" Level: {self.score_num}",align=ALING,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER',align='center',font=FONT)