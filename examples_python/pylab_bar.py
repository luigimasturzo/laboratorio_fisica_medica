import pylab
import numpy
numpy.random.seed(1)

# Load the input data.
x, y = pylab.loadtxt('data/plasduino_dice.txt', unpack = True)

# Format the plot.
pylab.rc('font', size = 18)
pylab.title('A bar plot', y = 1.02)
pylab.xlabel('Sum')
pylab.ylabel('Counts')
pylab.xlim(0, 15)
pylab.ylim(0, 200)
pylab.grid(color = 'gray')

# Create the histogram. Note that we offset the x values by 1/2
# times the width of the bars.
w = 0.25
pylab.bar(x - w/2., y, width = w, color = 'white')

# Save the plot to a pdf file for later use (maybe in a writeup?).
pylab.savefig('bar.pdf')

# Finally: show the plot on the screen.
pylab.show()

