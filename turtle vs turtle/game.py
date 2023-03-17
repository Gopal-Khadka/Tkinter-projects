from turtle import Turtle,Screen
from tortoise import Tortoise
from random import randint
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.title("Turtle Move Game By Gopal Khadka")
screen.setup(600,600)
screen.tracer(0)
def main():


    # red turtle definition
    red_turtle=Tortoise(color="red")
    red_turtle.initial_pos((30,0))
    red_score=ScoreBoard(color="red", pos=(-200,240))
    # blue turtle definition
    blue_turtle=Tortoise(color="blue")
    blue_turtle.initial_pos((-30,0))
    blue_score=ScoreBoard(color="blue", pos=(200,240))

    is_game_on=True

    while is_game_on:
        time.sleep(0.1)
        screen.update()
        attempt=randint(0, 1)
        if attempt==0:
            blue_turtle.move()
            blue_score.update_score()
            blue_score.prompt()
        else:
            red_turtle.move()
            red_score.update_score()
            red_score.prompt()

        if  blue_turtle.xcor()>280 or blue_turtle.xcor()<-280 or blue_turtle.ycor()>280 or blue_turtle.ycor()<-280:
            is_game_on=False
            red_score.game_over(winner="Red")

        if red_turtle.xcor()>280 or red_turtle.xcor()<-280 or red_turtle.ycor()>280 or red_turtle.ycor()<-280:
            is_game_on=False
            blue_score.game_over(winner="Blue")

   

        

main()
time.sleep(3)
repetition=screen.textinput(title="Do you want to play again?  ", prompt="Type Yes(Y) or No(N)")
while repetition.lower() in ["y","yes"]:
    screen.clear()
    main()

print("Come back soon!")
screen.exitonclick()






