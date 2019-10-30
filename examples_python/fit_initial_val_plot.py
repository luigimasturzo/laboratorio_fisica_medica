import pylab

# Load the data from the file.
t, s, ds = pylab.loadtxt('data/fit_initial_val.txt', unpack = True)

# Format the plot.
pylab.rc('font', size = 18)
pylab.title('Law of motion', y = 1.02)
pylab.xlabel('t [s]')
pylab.ylabel('s [m]', labelpad = 5)
pylab.xlim(0, 20)
pylab.ylim(-1.5, 1.5)
pylab.grid(color = 'gray')

# Create the scatter plot.
pylab.errorbar(t, s, ds, linestyle = '', color = 'black', marker = 'o')

# Save the plot to a pdf file for later use (maybe in a writeup?).
pylab.savefig('fit_initial_val_plot.pdf')

# Finally: show the plot on the screen.
pylab.show()
