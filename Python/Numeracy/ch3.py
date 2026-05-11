# EX1 - Perimeter
# Imports
import turtle, random

# Square
def square(size):
    for i in range(4):
        pencil.forward(size / 2)
        pencil.right(90)
        pencil.forward(CHECK1)
        pencil.back(CHECK1 * 2)
        pencil.forward(CHECK1)
        pencil.left(90)
        pencil.forward(size / 2)
        pencil.left(90)

# Turtle
wn = turtle.Screen()
pencil = turtle.Turtle()
CHECK1 = 8
SCALE = 40
for i in range(4):
    pencil.color('gray')
    pencil.forward(SCALE)
    pencil.left(90)
SIDE = random.randint(3, 10)
square(SIDE * SCALE)
units = random.choice([' cm', ' m'])
label = str(SIDE) + units
pencil.penup()
pencil.forward(SIDE * SCALE / 2)
pencil.sety(pencil.ycor() - SCALE)
pencil.write(label)
pencil.sety(pencil.ycor() - SCALE)

# Input
response = wn.numinput('Input perimeter', 'Please enter the perimeter')
if response == SIDE * 4:
    pencil.write('Well done', font=('Arial', 18, 'normal'))
else:
    pencil.write('No', font=('Arial', 18, 'normal'))
wn.exitonclick()