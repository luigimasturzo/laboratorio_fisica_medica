import numpy

# Create a python list and a numpy array with the same content.
l = [0., 1., 3., 4., 8.]
a = numpy.array([0., 1., 3., 4., 8.])

# Now try and append a string. Ouch...
l.append('howdy?')
a = numpy.insert(a, len(a), 'howdy?')
print(l)
print(a)
