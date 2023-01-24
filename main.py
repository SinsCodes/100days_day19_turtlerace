from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(height=400,width=500)
is_race_on=False
user_bet=screen.textinput(title="make your color",prompt="which turtle will win the race?enter a color? ")
print(user_bet)
colors=["red","orange","yellow","purple","green","blue"]
y_position=[-100,-70,-40,-10,20,50]
all_turtles=[]
for i in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you won,{winning_color} turtle is the winner")
            else:
                print(f"you lose,{winning_color} turtle,is the winner")

        ran_dist=random.randint(0,10)
        turtle.forward(ran_dist)


screen.exitonclick()