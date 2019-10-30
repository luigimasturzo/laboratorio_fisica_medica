import math

# A couple of mathematical functions.
a = math.sin(math.pi/4)
b = math.log(100, 10)

# This will give the integral of a standard gaussian between 0 and 1,
# i.e., a half of the usual ~68%.
c = 0.5*math.erf(1/math.sqrt(2.))

print(a, b, c)
