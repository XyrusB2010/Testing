"""Snake game using turtle libray."""
import turtle
import random
import subprocess
import os

def sha256Hash(input):
    output = subprocess.run(
        ['python3', '/workspaces/Testing/Python/sha256.py', input],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if output.returncode == 0:
        return output.stdout.strip()
    else:
        raise RuntimeError(f"Error executing sha256.py: {output.stderr}")

filename = os.path.expanduser("~/.turtle-snake")
if os.path.exists(filename):
    with open(filename, "r") as file:
        contents = file.read()
        hash = contents.split()[1]
    if hash != sha256Hash(contents.split()[0]):
        choice = input("Warning: High score file has been tampered with! Do you wish to reset it? (y/N): ").strip().lower()
        if choice == "y":
            with open(filename, "w") as file:
                file.write("0 " + sha256Hash("0"))
            print("High score has been reset.")
        else:
            print("Exiting without changes.")
            exit()

def snake_up():
    global direction
    if direction != south:
        direction = north
        snake[HEAD].setheading(direction)
def snake_down():
    global direction
    if direction != north:
        direction = south
        snake[HEAD].setheading(direction)
def snake_left():
    global direction
    if direction != east:
        direction = west
        snake[HEAD].setheading(direction)
def snake_right():
    global direction
    if direction != west:
        direction = east
        snake[HEAD].setheading(direction)

wn = turtle.Screen()
DIM = 800
HALF = DIM / 2
TEXT_OFFSET_X = 0.325
TEXT_OFFSET_Y = 0.4
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

try:
    with open(filename, "r") as file:
        print("High score detected, loading...")
        contents = file.read()
        best = int(contents.split()[0])
except FileNotFoundError:
    with open(filename, "w") as file:
        print("Failed to detect high score, loading...")
        file.write("0 " + sha256Hash("0"))
        best = 0

score = 0
hashscore = sha256Hash(str(score))
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.speed("fastest")
text.color("black")
text.goto(-DIM * TEXT_OFFSET_X, DIM * TEXT_OFFSET_Y)
text.write(f"Best: {best}", align="left", font=("Arial", 24, "normal"))
text.goto(DIM * TEXT_OFFSET_X, DIM * TEXT_OFFSET_Y)
text.write(f"Score: {score}", align="right", font=("Arial", 24, "normal"))

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
        hashscore = sha256Hash(str(score))
        text.clear()
        text.goto(-DIM * TEXT_OFFSET_X, DIM * TEXT_OFFSET_Y)
        text.write(f"Best: {best}", align="center", font=("Arial", 24, "normal"))
        text.goto(DIM * TEXT_OFFSET_X, DIM * TEXT_OFFSET_Y)
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
if best < score:
    best = score
    with open(filename, "w") as file:
        print("Saving new high score...")
        file.write(str(best) + " " + hashscore)
    wn.textinput('New High Score!', f'New Best: {best}\nClick OK to quit')
else:
    wn.textinput('Game over', f'Score: {score}\nClick OK to quit')
wn.bye()