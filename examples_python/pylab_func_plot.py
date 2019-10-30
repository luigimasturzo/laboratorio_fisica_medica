import pylab
import numpy

# Create a grid of x-values (from 0 to 10 in 100 steps).
x = numpy.linspace(0, 10, 100)

# Calculate the y values. Note x and y are both arrays!
y = x**2

# Some formatting.
pylab.rc('font', size = 18)
pylab.title('A function', y = 1.02)
pylab.xlabel('x')
pylab.ylabel('f(x)')
pylab.grid(color = 'gray')

# Plot the graph.
pylab.plot(x, y, color = 'black')

# Save the plot to a pdf file for later use (maybe in a writeup?).
pylab.savefig('square.pdf')

# And show the plot.
pylab.show()
