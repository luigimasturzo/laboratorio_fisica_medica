import pylab
import numpy
import scipy.stats

# Create a grid of x-values (from 0 to 10 in 100 steps).
x = numpy.linspace(-5, 5, 100)

# Grab the normal distribution from the scipy.stats module.
rv = scipy.stats.norm()

# Calculate the y values. Note x and y are both arrays (Mind here you
# want the probability density function of the distribution).
y = rv.pdf(x) 

# Some formatting.
pylab.rc('font', size = 18)
pylab.title('A standard gaussian', y = 1.02)
pylab.xlabel('x')
pylab.ylabel('pdf(x)')
pylab.xlim(-5, 5)
pylab.ylim(0, 0.5)
pylab.grid(color = 'gray')

# Plot the graph.
pylab.plot(x, y, color = 'black')

# Save the plot to a pdf file for later use (maybe in a writeup?).
pylab.savefig('gauss.pdf')

# And show the plot.
pylab.show()
