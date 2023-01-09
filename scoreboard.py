FONT  = ("Courier", 24, 'normal')

from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("DarkGoldenRod4")
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.update_score()
        
    
    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}",  align='left', font=FONT)
        
    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER😪😪😪", align='center', font=FONT)