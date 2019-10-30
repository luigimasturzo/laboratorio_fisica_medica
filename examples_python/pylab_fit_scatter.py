import pylab
import numpy
from scipy.optimize import curve_fit


def fit_function(x, m, q):
    """ Definition of the fit function.

    This is a simple straight line of the form y = m*x + q.
    Mind that the x argument, here, is a numpy array, and the whole thing
    works because you can multiply an array by a scalar and you can add a
    scalar to an array.
    """
    return m*x + q


# Load the data from the file.
x, y, dy = pylab.loadtxt('data/scatter_plot.txt', unpack = True)

# Set the initial values for the fit parameters and fit the data.
initial_values = (1., 1.)
pars, covm = curve_fit(fit_function, x, y, initial_values, dy)

# Retrieve the best-fit parameters and related quantities, and print
# them on the terminal.
m0, q0 = pars
dm, dq = numpy.sqrt(covm.diagonal())
chisq = (((y - fit_function(x, m0, q0))/dy)**2).sum()
ndof = len(x) - 2
print('m = %f +- %f' % (m0, dm))
print('q = %f +- %f' % (q0, dq))
print('Chisquare/ndof = %f/%d' % (chisq, ndof))

# Format the plot.
pylab.rc('font', size = 18)
pylab.title('Law of motion', y = 1.02)
pylab.xlabel('t [s]')
pylab.ylabel('s [m]', labelpad = 25)
pylab.xlim(0, 10)
pylab.ylim(0, 18)
pylab.grid(color = 'gray')

# Create the scatter plot.
pylab.errorbar(x, y, dy, linestyle = '', color = 'black', marker = 'o')

# Create a one-dimensional grid and draw the fit function.
func_grid = numpy.linspace(0, 10, 100)
pylab.plot(func_grid, fit_function(func_grid, m0, q0), color = 'black')

# Save the plot to a pdf file for later use (maybe in a writeup?).
pylab.savefig('fit_scatter.pdf')

# Finally: show the plot on the screen.
pylab.show()
