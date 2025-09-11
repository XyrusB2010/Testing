# Snake game using turtle library.
import turtle
import random
import subprocess
import os

def antiCheat(input):
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

name = input("Enter your name: ").strip()
if not name:
    name = "Player"

userindex = 0
scoreFile = os.path.expanduser("~/.turtle-snake")
if os.path.exists(scoreFile):
    with open(scoreFile, "r") as file:
        contents = file.read().splitlines()
    for index, item in enumerate(contents):
        if name in item:
            userindex = index
            print("User found, loading...")
            break
    else:
        print("New user, adding...")
        contents.insert(0, f"0,{antiCheat('0')},{name},{antiCheat(name)}")
        with open(scoreFile, "w") as file:
            file.write("\n".join(contents))
            userindex = 0
    scorehash = contents[userindex].split(",")[1]
    namehash = contents[userindex].split(",")[3]
    if scorehash != antiCheat(contents[userindex].split(",")[0]) or namehash != antiCheat(contents[userindex].split(",")[2]):
        choice = input("WARNING: High score has been tampered with! Do you wish to reset it? (y/N): ").strip().lower()
        if choice == "y":
            with open(scoreFile, "w") as file:
                contents[userindex] = f"0,{antiCheat('0')},{name},{antiCheat(name)}"
                file.write("\n".join(contents))
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

controls = turtle.textinput("Controls", """Do you prefer WASD or Arrow Keys? (Enter "WASD" for WASD, "Arrow" for Arrow Keys, Default: Arrow Keys):""").lower()
if controls == "":
    controls = "arrow"

speed = int(turtle.numinput("Speed", "Enter speed from 0-10 (0 = Slowest, 10 = Fastest):")) + 1
if speed == 11:
    speed = 0

while True:
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
        with open(scoreFile, "r") as file:
            print("High score detected, loading...")
            contents = file.read().splitlines()
            for index, item in enumerate(contents):
                if name in item:
                    userindex = index
                    best = int(contents[userindex].split(",")[0])
                    break
    except FileNotFoundError:
        with open(scoreFile, "w") as file:
            print("Failed to detect high score, loading...")
            best = 0
            contents = []
            contents.insert(0, f"0,{antiCheat('0')},{name},{antiCheat(name)}")
            with open(scoreFile, "w") as file:
                file.write("\n".join(contents))
                userindex = 0

    score = 0
    hashscore = antiCheat(str(score))
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.speed("fastest")
    text.color("black")
    text.goto(-DIM * TEXT_OFFSET_X, DIM * TEXT_OFFSET_Y)
    text.write(f"Best: {best}", align="left", font=("Arial", 24, "normal"))
    text.goto(DIM * TEXT_OFFSET_X, DIM * TEXT_OFFSET_Y)
    text.write(f"Score: {score}", align="right", font=("Arial", 24, "normal"))

    if controls == "arrow":
        wn.onkey(snake_up, "Up")
        wn.onkey(snake_down, "Down")
        wn.onkey(snake_left, "Left")
        wn.onkey(snake_right, "Right")
    else:
        wn.onkey(snake_up, "w")
        wn.onkey(snake_down, "s")
        wn.onkey(snake_left, "a")
        wn.onkey(snake_right, "d")
    wn.listen()

    while True:
        snake.append(snake[HEAD].clone())
        snake[HEAD].setheading(direction)
        snake[HEAD].forward(move)
        if snake[HEAD].distance(apple) < move:
            apple.goto(random.randrange(0,DIM,25) - HALF, random.randrange(0,DIM,25) - HALF)
            score += 1
            hashscore = antiCheat(str(score))
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

    if best < score:
        best = score
        with open(scoreFile, "w") as file:
            print("Saving new high score...")
            with open(scoreFile, "w") as file:
                contents[userindex] = f"{str(score)},{antiCheat(str(score))},{name},{antiCheat(name)}"
                file.write("\n".join(contents))
        play_again = wn.textinput('New High Score!', f'New Best: {best}\nPlay again? (y/N):')
    else:
        play_again = wn.textinput('Game over', f'Score: {score}\nPlay again? (y/N):')

    if play_again == "" or play_again.lower() == "n":
        break
    else:
        wn.clear()
wn.bye()
showleaderboard = input("Do you wish to see the leaderboard? (y/N): ").strip().lower()
if showleaderboard == "y":
    try:
        with open(scoreFile, "r") as file:
            contents = file.read().splitlines()
            scores = []
            for item in contents:
                parts = item.split(",")
                if len(parts) >= 4:
                    scores.append((int(parts[0]), parts[2]))
            scores.sort(reverse=True, key=lambda x: x[0])
            print("Leaderboard:")
            for rank, (score, player) in enumerate(scores, start=1):
                print(f"{rank}. {player} - {score}")
    except FileNotFoundError:
        print("No leaderboard data found.")