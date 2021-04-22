import turtle as t
import random

# setup screen
my_screen = t.Screen()
my_screen.setup(width=500, height=400)
race_is_on = False

# create turtles
turtle_colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]
y_pos = -100
turtles = []
for color in turtle_colors:
    turtle = t.Turtle(shape="turtle")
    turtle.speed(100)
    turtle.penup()
    turtle.color("black", color)
    turtle.goto(x=-230, y=y_pos)
    y_pos += 40
    turtles.append(turtle)

# ask user for winner turtle
user_bet = my_screen.textinput(title="Guess the winner",
                               prompt="Which turtle will win the race? Enter a color.\n"
                                      "(red/green/blue/yellow/magenta/cyan): ").lower()

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 2))
        if turtle.xcor() > 225:
            race_is_on = False
            if user_bet == turtle.fillcolor():
                print(f"You win! The {turtle.fillcolor()} turtle won the race!")
            else:
                print(f"You loose! The {turtle.fillcolor()} turtle won the race!")












my_screen.exitonclick()







