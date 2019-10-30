import math

def f(x):
    # Evaluation of f(x).
    return math.exp(x) - x**2.0

# Variable initialization.
precision = 1e-6
x1 = -1
x2 = 1
x = (x1 + x2)/2.0
y = f(x)
n = 0

# While loop: we exit when the difference from zero of the function value
# is whithin the predefined precision.
while abs(y) > precision:
    if y > 0:
        x2 = x
    else:
        x1 = x
    x = (x1 + x2)/2.0
    y = f(x)
    n += 1

# Print out the numeber of iteration, x and f(x).
print(n, x, f(x))
