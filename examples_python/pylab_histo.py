import pylab
import numpy
numpy.random.seed(1)

# Generate a sample of 100000 gaussian-distributed values.
sample = numpy.random.normal(0., 1., 100000)

# Format the plot.
pylab.rc('font', size = 18)
pylab.title('A histogram', y = 1.02)
pylab.xlabel('x')
pylab.ylabel('Counts', labelpad = -5)
pylab.ylim(0, 10000)
pylab.grid(color = 'gray')

# Create the histogram.
pylab.hist(sample, bins = 50, range = (-5, 5), histtype = 'step',
           color = 'black')

# Save the plot to a pdf file for later use (maybe in a writeup?).
pylab.savefig('histogram.pdf')

# Finally: show the plot on the screen.
pylab.show()

