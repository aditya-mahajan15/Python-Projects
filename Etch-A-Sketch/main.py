from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.bgcolor("white")
def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def left():
    tim.left(10)

def right():
    tim.right(10)

def clear():
    tim.clear()
    tim.reset()

screen.listen()
screen.onkey(key="Up", fun=forward)
screen.onkey(key="Down", fun=backward)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()