import turtle
import random
import time

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Turtle Star Collector")
screen.bgcolor("navy")

player = turtle.Turtle()
player.shape("turtle")
player.color("#134983")
player.penup()

def draw_star(t, size):
    t.begin_poly()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_poly()
    return t.get_poly()


star_shape = draw_star(turtle.Turtle(), 20)
screen.register_shape("star", star_shape)

star = turtle.Turtle()
star.shape("star")
star.color("#fbaf3c")
star.penup()

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-280, 260)
score_display.color("white")

timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(200, 260)
timer_display.color("white")

score = 0
game_duration = 60
start_time = time.time()


def move_up():
    player.setheading(90)
    player.forward(10)


def move_down():
    player.setheading(270)
    player.forward(10)


def move_left():
    player.setheading(180)
    player.forward(10)


def move_right():
    player.setheading(0)
    player.forward(10)


def quit_game():
    screen.bye()


def move_star():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    star.goto(x, y)


def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))


def update_timer():
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, game_duration - elapsed_time)
    timer_display.clear()
    timer_display.write(f"Time: {remaining_time}s", font=("Arial", 16, "normal"))
    if remaining_time > 0:
        screen.ontimer(update_timer, 1000)
    else:
        game_over()


def game_over():
    player.hideturtle()
    star.hideturtle()
    screen.clear()
    screen.bgcolor("navy")
    game_over_turtle = turtle.Turtle()
    game_over_turtle.hideturtle()
    game_over_turtle.color("white")
    game_over_turtle.write(f"Game is now Over!\nFinal Score: {score}", align="center", font=("Arial", 24, "normal"))


# It is used to bind keyboard keys in order to move the pen to up or down
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(quit_game, "q")
screen.listen()

move_star()
update_timer()

while True:
    screen.update()

    if player.distance(star) < 20:
        move_star()
        update_score()

    if time.time() - start_time >= game_duration:
        game_over()
        break

turtle.done()