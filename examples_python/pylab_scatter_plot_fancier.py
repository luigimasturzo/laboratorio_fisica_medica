import pylab

# Load the data from the file.
t, s, ds = pylab.loadtxt('data/scatter_plot.txt', unpack = True)

# Format the plot.
pylab.rc('font', size = 18)
pylab.title('Law of motion', y = 1.02)
pylab.xlabel('t [s]')
pylab.ylabel('s [m]', labelpad = 25)
pylab.xlim(0, 10)
pylab.ylim(0, 18)
pylab.grid(color = 'gray')

# Create the scatter plot.
pylab.errorbar(t, s, ds, linestyle = '', color = 'black', marker = 'o')

# Save the plot to a pdf file for later use (maybe in a writeup?).
pylab.savefig('scatter_plot_fancier.pdf')

# Finally: show the plot on the screen.
pylab.show()
