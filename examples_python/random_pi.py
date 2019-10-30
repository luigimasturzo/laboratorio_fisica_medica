import math
import random
random.seed(1)

# Generate a lot of points in a square of side 2 and count how many
# of them fall into the inscribed circle of radius one.
N = 0
n = 0
for i in range(100000):
    x = random.uniform(-0.5, 0.5)
    y = random.uniform(-0.5, 0.5)
    N += 1
    if (x**2 + y**2) < 0.25:
        n += 1

# Calculate our estimate of pi and the relative error (mind in
# python 2x this works because 4*n is executed first and returns
# a float, while n/N would return 0).
pi = 4.*n/N
err = abs((pi - math.pi)/math.pi)
print(pi)
print('%.3e' % err)
