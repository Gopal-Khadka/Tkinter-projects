from turtle import Turtle
FONT=("Courier",15,"normal")
ALIGN="center"
GAME_FONT=("Ubuntu",50,"bold")
MOVE_DISTANCE=30


class ScoreBoard(Turtle):
    def __init__(self,color,pos):
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.position=pos
        self.goto(self.position)
        self.moves=0
        self.dist=0
        self.update_score()
    
    def update_score(self):
        self.moves+=1
        self.dist=self.moves*MOVE_DISTANCE

    def prompt(self):
        self.clear()
        self.write(f"Moves: {self.moves} ",font=FONT,align=ALIGN)
        self.goto(self.position[0],self.position[1]-20)
        self.write(f"Distance: {self.dist}",font=FONT,align=ALIGN)
        self.goto(self.position)

    def game_over(self,winner):
        self.home()
        self.color("black")
        self.write("Game Over",font=GAME_FONT,align=ALIGN)
        self.goto(0,-60)
        self.write(f"{winner} wins!!",font=GAME_FONT,align=ALIGN)