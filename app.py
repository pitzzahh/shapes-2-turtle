import turtle
import random

pen = turtle.Turtle()
screen = turtle.Screen()

def random_color():
    return random.random(), random.random(), random.random()

def move_left():
    pen.up()
    pen.setheading(180)
    pen.forward(100)

def move_right():
    pen.up()
    pen.setheading(0)
    pen.forward(100)

def move_up():
    pen.up()
    pen.setheading(90)
    pen.forward(100)

def move_down():
    pen.up()
    pen.setheading(270)
    pen.forward(100)

def draw_square():
    pen.down()
    pen.fillcolor(random_color())
    pen.begin_fill()
    for _ in range(4):
        pen.forward(50)
        pen.right(90)
    pen.end_fill()
    pen.up()

def draw_circle():
    pen.down()
    pen.fillcolor(random_color())
    pen.begin_fill()
    pen.circle(25)
    pen.end_fill()
    pen.up()

def draw_triangle():
    pen.down()
    pen.fillcolor(random_color())
    pen.begin_fill()
    for _ in range(3):
        pen.forward(50)
        pen.left(120)
    pen.end_fill()
    pen.up()

def reset_screen(x, y):
    pen.clear()
    pen.up()
    pen.goto(x,y)
    pen.home()

def create_reset_button():
    button = turtle.Turtle()
    button.hideturtle()
    button.up()
    button.goto(screen.window_width() / 2 - 60, screen.window_height() / 2 - 40)
    button.down()
    for _ in range(2):
        button.forward(60)
        button.right(90)
        button.forward(30)
        button.right(90)
    button.up()
    button.goto(screen.window_width() / 2 - 30, screen.window_height() / 2 - 33)
    button.write("Reset", align="center", font=("Arial", 12, "normal"))
    screen.onclick(reset_screen)

screen.listen()

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.onkey(draw_square, "s")
screen.onkey(draw_square, "S")
screen.onkey(draw_circle, "c")
screen.onkey(draw_circle, "C")
screen.onkey(draw_triangle, "t")
screen.onkey(draw_triangle, "T")

create_reset_button()

turtle.done()