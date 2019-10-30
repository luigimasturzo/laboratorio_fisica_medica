import numpy

# Create a python list and a numpy array with the same content.
l = [0., 1., 3., 4., 8.]
a = numpy.array([0., 1., 3., 4., 8.])

# Append a floating point number to both.
# (Note the syntax is slightly different in the two cases.)
l.append(16.)
a = numpy.insert(a, len(a), 16.)
print(l)
print(a)
