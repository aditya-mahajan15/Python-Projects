from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make a bet", prompt="Who are you betting on ? Enter a color:  ")
colors = ["red", "green", "orange", "blue", "purple", "yellow"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
is_race_on = False

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winner = turtle.pencolor()
                if winner == user_guess:
                    print(f"You win!\n{winner} has won the race")
                else:
                    print(f"You Loose!\n{winner} has won the race")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
screen.exitonclick()
