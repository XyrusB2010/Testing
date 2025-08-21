"""Snake game using turtle libray."""
import turtle
import random


def snake_up():
    global direction
    direction = north
    snake[HEAD].setheading(direction)
def snake_down():
    global direction
    direction = south
    snake[HEAD].setheading(direction)
def snake_left():
    global direction
    direction = west
    snake[HEAD].setheading(direction)
def snake_right():
    global direction
    direction = east
    snake[HEAD].setheading(direction)

wn = turtle.Screen()
DIM = 800
HALF = DIM / 2
wn.setup(DIM, DIM)
HEAD = -1
TAIL = 0

speed = int(turtle.numinput("Speed", "Enter speed from 0-10 (0 = Slowest, 10 = Fastest):")) + 1
if speed == 11:
    speed = 0

apple = turtle.Turtle()
apple.shape("square")
apple.color("green")
apple.speed(speed)
apple.turtlesize(2, 2)
apple.penup()
snake = []
length = 7
move = 25
east, south, west, north = 0, 270, 180, 90
direction = east
for body in range(length):
    snake.append(apple.clone())
    snake[body].forward(move * body)
apple.shape("circle")
apple.color("black", "red")

score = 0
best = 0
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.speed("fastest")
text.color("black")
text.goto(0, 300)
text.write(f"Best: {best}", align="center", font=("Arial", 24, "normal"))
text.goto(300, 300)
text.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

wn.onkey(snake_up, "Up")
wn.onkey(snake_down, "Down")
wn.onkey(snake_left, "Left")
wn.onkey(snake_right, "Right")
wn.listen()
#
while True:
    snake.append(snake[HEAD].clone())
    snake[HEAD].setheading(direction)
    snake[HEAD].forward(move)
    if snake[HEAD].distance(apple) < move:
        apple.goto(random.randrange(DIM) - HALF, random.randrange(DIM) - HALF)
        score += 1
        text.clear()
        text.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    else:
        snake[TAIL].reset()
        snake.pop(TAIL)
    same = 0
    for body in snake:
        if body.distance(snake[HEAD]) < move / 2:
            same += 1
    if same > 1:
        break
    if snake[HEAD].xcor() > HALF:
        snake[HEAD].setx(-HALF)
    if snake[HEAD].xcor() < -HALF:
        snake[HEAD].setx(HALF)
    if snake[HEAD].ycor() > HALF:
        snake[HEAD].sety(-HALF)
    if snake[HEAD].ycor() < -HALF:
        snake[HEAD].sety(HALF)
#
wn.textinput('Game over', f'Score: {score}\nClick OK to quit')
wn.bye()