import numpy

# Create a 1-dimensional array of 8-bit integers.
a = numpy.array([0, 0, 0], 'int8')

# Oops... this is only holding integers from -128 to 127!
a[0] = 100
a[1] = 200
a[2] = 300

print(a)
