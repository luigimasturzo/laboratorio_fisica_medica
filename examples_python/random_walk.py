import random
random.seed(1)

import math

# This is simple module of the python standard library for generating
# graphics.
import turtle
turtle.title('2-d random walk')
turtle.setup(350, 650, 0, 0)

# Loop and generate a random walk in two dimension with fixed step.
x = 0.
y = 0.
step = 5.
for i in range(1000):
    angle = random.uniform(0, 2*math.pi)
    x += step*math.cos(angle)
    y += step*math.sin(angle)
    turtle.setposition(x, y)

# Save the canvas to file
#screen = turtle.getscreen()
#screen.getcanvas().postscript(file = "random_walk.eps")
