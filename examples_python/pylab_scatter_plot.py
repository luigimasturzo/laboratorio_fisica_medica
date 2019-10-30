import pylab

# Load the data from the file.
t, s, ds = pylab.loadtxt('data/scatter_plot.txt', unpack = True)

# Create the scatter plot.
pylab.errorbar(t, s, ds)

# Save the plot to a pdf file for later use (maybe in a writeup?).
pylab.savefig('scatter_plot.pdf')

# Finally: show the plot on the screen.
pylab.show()
